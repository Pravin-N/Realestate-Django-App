from django.urls import path # step 7 (iv) import the path to use the path package. See other urls file.

from . import views # step 7 (v)

urlpatterns = [
    path('', views.index, name='index'), # step 7 (vi) '' refers to the root path. second parameter is the views method that needs to be connected to. Third is the name that is used to access this path.
    path('about', views.about, name='about'), # step 8.6
]
