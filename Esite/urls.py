from django.urls import path
from . import views

app_name = 'Esite'

urlpatterns = [

    path('test/',views.test, name="test"),    
    
    path('',views.index,name='index'),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('tacker/',views.tracker, name='tracker'),
    path('cart/',views.cart,name='cart'),
    path("product/<int:myid>", views.product, name="product"),
    path('checkout/',views.checkout,name='checkout'),

] 