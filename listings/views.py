from django.shortcuts import render, get_object_or_404 #step 28.2
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator # step 26.2
from .choices import price_choices, bedroom_choices, state_choices # step 29.6

from .models import Listing # step 24.2

# Create your views here.
def index(request): # Step 13.8
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) #step 24.4 & 26.8 & 26.9

    paginator = Paginator(listings, 6) # 26.1
    page = request.GET.get('page')# 26.1
    paged_listings = paginator.get_page(page) # 26.1

    context = {
        'listings': paged_listings    # listings #step 24.4 & 26.1
    }
    return render(request, 'listings/listings.html', context) #step 24.3 

def listing(request, listing_id): # Step 13.8 & 25.4
    listing = get_object_or_404(Listing, pk=listing_id) # step 28.2

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request): # Step 13.8
    queryset_list = Listing.objects.order_by('-list_date') #step 30.1

    # Keywords step 30.2
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords: 
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City step 30.3
    if 'city' in request.GET:
        city = request.GET['city']
        if city: 
            queryset_list = queryset_list.filter(city__iexact=city)

    # state step 30.4
    if 'state' in request.GET:
        state = request.GET['state']
        if state: 
            queryset_list = queryset_list.filter(state__iexact=state)

    # state step 30.5
    if 'bedrooms' in request.GET:
        bedroom = request.GET['bedrooms']
        if bedroom: 
            queryset_list = queryset_list.filter(bedroom__lte=bedroom)

    # state step 30.5
    if 'price' in request.GET:
        price = request.GET['price']
        if price: 
            queryset_list = queryset_list.filter(price__lte=price)
    

    context = {
        'state_choices': state_choices, # step 29.6
        'bedroom_choices': bedroom_choices, # step 29.6
        'price_choices': price_choices, # step 29.6
        'listings': queryset_list,
        'values': request.GET, # step 31.1
    }

    return render(request, 'listings/search.html', context)