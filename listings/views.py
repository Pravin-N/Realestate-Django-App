from django.shortcuts import render

# Create your views here.
def index(request): # Step 13.8
    return render(request, 'listings/listings.html')

def listing(request): # Step 13.8
    return render(request, 'listings/listing.html')

def search(request): # Step 13.8
    return render(request, 'listings/search.html')