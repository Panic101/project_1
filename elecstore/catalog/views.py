from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import ProductDirectory, ProductItem


# Create your views here.

def homePage(request):					#home page(old index function)
	return render(request, 'catalog/home_page.html')
	
def AboutUsPage(request):				#about us page
	return render(request, 'catalog/about_us.html')
	
def ContactUsPage(request):				#contact us page
	return render(request, 'catalog/contact_us.html')

def catalogView(request):				#displays catalog of electronic items
	directory_list = ProductDirectory.objects.all()
	template = loader.get_template('catalog/catalog_view.html')
	context = RequestContext(request, {
		'directory_list': directory_list,
	})
	return HttpResponse(template.render(context))
    
def catalogViewItem(request, directory_id):		#displays list of products for respected category selected in the catalog
	product_list = ProductItem.objects.filter(id=directory_id)
	template = loader.get_template('catalog/catalog_view_item.html')
	context = RequestContext(request, {
		'product_list': product_list,
	})
	return HttpResponse(template.render(context))


def productView(request):			#product_id #this function is in all probability redundant
    response = "Once the user selected a category, they will view the products here"
    return HttpResponse(response)
    
def productViewItem(request, product_id):	#displays the details of the product selected in product list
	description_list = ProductItem.objects.filter(id=product_id)
	template = loader.get_template('catalog/product_view_item.html')
	context = RequestContext(request, {
		'description_list': description_list,
	})
	return HttpResponse(template.render(context))
	


