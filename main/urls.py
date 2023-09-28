from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/faq', views.faq, name='faq'),
    path('/rent', views.rent, name='rent'),
    path('/buy', views.buy, name='buy'),

    path('/sell', views.sell, name='sell'),

    path('/favorite', views.favorite, name='favorite'),
    path('add_to_favorites/<int:pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:pk>/', views.remove_from_favorites, name='remove_from_favorites'),

    path('/authPage', views.authPage, name='authPage'),
    path('/logout', views.logoutUser, name='logout'),

    path('/addProperty', views.addProperty, name='addProperty'),
    path('/editProperty/<int:pk>', views.editProperty, name='editProperty'),
    path('/deleteProperty/<int:pk>', views.deleteProperty, name='deleteProperty'),
    path('/product-detail/<int:pk>', views.ProductDetail.as_view(), name='productDetail'),

]
