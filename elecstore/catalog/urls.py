from django.conf.urls import url

from . import views

urlpatterns = [
	
	#HOME PAGE
	url(r'^$', views.homePage, name='homePage'),
	
	#ABOUT US
	url(r'^about/$', views.AbourUsPage, name='AbourUsPage'),
	
	#CONTACT US
	url(r'^contact/$', views.ContactUsPage, name='ContactUsPage'),

	#CATALOG/
    # ex: /catalog/
    url(r'^catalog/$', views.catalogView, name='catalogView'),
    # ex: /catalog/directory_id/
	url(r'^catalog/(?P<directory_id>[0-9]+)/$', views.catalogViewItem, name='catalogViewItem'),
	
	#PRODUCTS/
	# ex: /catalog/products/
	url(r'^catalog/products/$', views.productView, name='productView'),
	# ex: /catalog/products/product_id
	url(r'^catalog/products/(?P<product_id>[0-9]+)/$', views.productViewItem, name='productViewItem'),
	

    
]
