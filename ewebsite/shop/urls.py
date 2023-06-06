from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="shophome"),
    path("about/",views.about,name="shopabout"),
    path("contact/",views.contact,name="shopcontact"),
    path("tracking/",views.tracking,name="shoptracking"),
    path("products/<int:id>",views.product,name="shopproduct"),
    path("checkout/",views.checkout,name="shopcheckout"),
    path("search/",views.search,name="shopsearch")

]