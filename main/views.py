from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q  # search
from .models import Property, Favorite, Review, FAQ
from .forms import NewUserForm, AddPropertyForm, ReviewForm, FAQForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import DetailView


def index(request):
    data = Property.objects.all().order_by("-date")
    reviews = Review.objects.all()
    form = ReviewForm()
    form1 = FAQForm()

    latest_property = Property.objects.all().order_by("-date")[:1]

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form1 = FAQForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('index')
        if form1.is_valid():
            faq = form1.save(commit=False)
            faq.user = request.user
            faq.save()
            return redirect('index')

    else:
        form = ReviewForm()
        form1 = FAQForm()

    return render(request, 'index.html', {
        "data": data,
        "latest_property": latest_property,
        "reviews": reviews,
        "form": form,
        "form1": form1,
    })


def rent(request):
    rentProperties = Property.objects.filter(isRent=True)

    return render(request, 'rent.html', {
        'rentProperties': rentProperties
    })


# def rent_property(request, property_id):
#     rent = get_object_or_404(Property, pk=property_id)
#
#     if request.method == 'POST':
#         form = RentForm(request.POST)
#         if form.is_valid():
#             rent_history = form.save(commit=False)
#             rent_history.property = rent
#             rent_history.price = rent.price
#             rent_history.username = request.user
#             rent_history.save()
#             return redirect('productDetail', pk=property_id)
#
#     else:
#         form = RentForm()
#
#     return render(request, 'product-detail.html', {'rent': rent, 'form': form})


def buy(request):
    properties = Property.objects.all()

    return render(request, 'buy.html', {
        'properties': properties
    })


def sell(request):
    if request.user.is_authenticated:
        sellProperties = Property.objects.filter(owner=request.user)
    else:
        sellProperties = []

    return render(request, 'sell.html', {
        "sellProperties": sellProperties
    })


def favorite(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user)

        return render(request, 'favorites.html', {'favorites': favorites})
    else:
        return render(request, 'favorites.html', {'favorites': None})


@login_required
def add_to_favorites(request, pk):
    property = get_object_or_404(Property, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, property=property)
    return redirect('productDetail', pk=property.pk)


@login_required
def remove_from_favorites(request, pk):
    favorite = get_object_or_404(Favorite, user=request.user, property_id=pk)
    favorite.delete()
    return redirect('favorite')


def faq(request):
    faqs = FAQ.objects.all()

    return render(request, "FAQ.html", {
        "faqs": faqs,
    })












class ProductDetail(DetailView):
    model = Property
    template_name = 'product-detail.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            property = self.get_object()

            is_favorite = Favorite.objects.filter(user=self.request.user, property=property).exists()

            context['is_favorite'] = is_favorite

        return context



def addProperty(request):
    error = ''
    form = AddPropertyForm()

    if request.method == 'POST':
        form = AddPropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Error"

    return render(request, 'addProperty.html', {
        'form': form,
        'error': error
    })



@login_required
def editProperty(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.user == property.owner:
        form = AddPropertyForm(request.POST or None, instance=property)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('productDetail', pk=property.pk)

        return render(request, 'editProperty.html', {
            'property': property,
            'form': form,
        })
    else:
        return render(request, 'notOwner.html', {
            'property': property
        })


@login_required
def deleteProperty(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == "POST":
        property.delete()
        return redirect("index")
    return render(request, "deleteProperty.html", {
        'property': property,
    })










def authPage(request):
    if request.method == "POST":
        sform = NewUserForm(request.POST)
        lform = AuthenticationForm(request, data=request.POST)
        if sform.is_valid():
            sform.save()
            return redirect("authPage")
        if lform.is_valid():
            username = lform.cleaned_data.get('username')
            password = lform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        sform = NewUserForm()
        lform = AuthenticationForm()
    return render(request, "authPage.html", {
        'lform': lform,
        'sform': sform
    })


def logoutUser(request):
    logout(request)
    return redirect("index")
