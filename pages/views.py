from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing #step 27.2
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request): # this is the view created for index.
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] #step 27.3

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    } #step 27.3
    return render(request, 'pages/index.html', context) # step8.8

def about(request): # step 8.7
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context) # step 8.8