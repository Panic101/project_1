from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def homePage(request):
	return HttpResponse("This will be my home page, with about us and that crap that can come in later")
	
def AbourUsPage(request):
	return HttpResponse("This will be the official about us page")
	
def ContactUsPage(request):
	return HttpResponse("This will be the official contact us page")

def catalogView(request):
    return HttpResponse("In this page, the different catalogs will be listed")
    
def catalogViewItem(request, directory_id):
    return HttpResponse("Im not firm on the details yet, but this displays catalog directory%s." % directory_id)

def productView(request):			#product_id
    response = "Once the user selected a category, they will view the products here"
    return HttpResponse(response)
    
def productViewItem(request, product_id):			
    return HttpResponse("Again, not so sure how yet, but this will display product%s" % product_id)


