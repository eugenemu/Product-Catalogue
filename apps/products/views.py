from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from apps.products.models import Product


def index(request):
	context = {'products': Product.objects.all()}

	return render(request, 'products/index.html', context)

def back(request):

	return redirect('/')

def show(request, product_id):
	context = {'product': Product.objects.get(id=product_id)}

	return render(request, 'products/product.html', context)

def add(request):
	product = request.POST['product']
	manufacturer = request.POST['manufacturer']
	price = request.POST['price']
	description = request.POST['description']
	errors = 0

	if manufacturer == "Select a Brand...":
		messages.add_message(request, messages.INFO, 'Please select a brand')
		errors += 1
	if len(product) < 3:
		messages.add_message(request, messages.INFO, 'Product has to be longer than 3 characters')
		errors += 1
	if price <= 0:
		messages.add_message(request, messages.INFO, 'Price has to be more than $0')
		errors += 1
	if len(description) > 50:
		messages.add_message(request, messages.INFO, 'Description has to be shorter than 50 characters')
		errors += 1
	
	if errors == 0:
		Product.objects.create(product=product, manufacturer=manufacturer, price=price, description=description, date=datetime.now())

	return redirect('/')

def remove(request, product_id):
	Product.objects.get(id=product_id).delete()

	return redirect('/')

def update(request, product_id):
	product = request.POST['product']
	manufacturer = request.POST['manufacturer']
	price = request.POST['price']
	description = request.POST['description']
	errors = 0

	if manufacturer == "Select a Brand...":
		messages.add_message(request, messages.INFO, 'Please select a brand')
		errors += 1
	if len(product) < 3:
		messages.add_message(request, messages.INFO, 'Product has to be longer than 3 characters')
		errors += 1
	if price <= 0:
		messages.add_message(request, messages.INFO, 'Price has to be more than $0')
		errors += 1
	if len(description) > 50:
		messages.add_message(request, messages.INFO, 'Description has to be shorter than 50 characters')
		errors += 1

	if errors == 0:
		product = Product.objects.get(id=product_id)
		product.product = request.POST['product']
		product.manufacturer = request.POST['manufacturer']
		product.price = request.POST['price']
		product.description = request.POST['description']
		product.save()
		return redirect('/')
	else:
		return redirect('/show/'+product_id)