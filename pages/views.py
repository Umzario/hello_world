from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# The guru is reviewing your code 
def homepageView(request):
    return HttpResponse("Hello, World!")
