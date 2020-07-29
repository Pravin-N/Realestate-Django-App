from django.urls import path # step 7 (iv) import the path to use the path package. See other urls file.

from . import views # step 7 (v)

urlpatterns = [
    path('', views.index, name='listings'), #step 13.5
    path('<int:listing_id>', views.listing, name='listing'), #step 13.5
    path('search', views.search, name='search'), #step 13.5
]
