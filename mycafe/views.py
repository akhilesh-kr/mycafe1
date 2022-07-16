from multiprocessing import context
# from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views import View
from .models import MenuItems,category,OrderModel

def index(request):
	return render(request,'mycafe/index.html',{'name':'akhilesh'})
def reservations(request):
	if request.method=='POST':
		name=request.POST['Name']
		email=request.POST['E_Mail']
		date=request.POST['Date']
		time=request.POST['Time']
		no_of_people=request.POST['no_of_people']

		# user=User.objects.create_user(username=username,password=password,email=email)
		# user.save()
		context = {
			'name': name,
			'no_of_people':no_of_people,
			'date':date,
			'time': time
		}

		return render(request,'mycafe/table_confirmation.html',context)
		
	else:
		return render(request,'mycafe/reservations.html',{'name':'Akhilesh'})
def aboutus(request):
	return render(request,'mycafe/aboutus.html',{'name':'name'})
def contact(request):
	return render(request,'mycafe/contact.html',{'name':'name'})
def menu(request):
	return render(request,'mycafe/menu.html',{'name':'name'})

class Order(View):
	def get(self,request,*args,**kwargs):
		appetizers = MenuItems.objects.filter(category__name__contains='Appetizer')
		entres = MenuItems.objects.filter(category__name__contains='Entre')
		desserts = MenuItems.objects.filter(category__name__contains='Dessert')
		drinks = MenuItems.objects.filter(category__name__contains='Drink')

		context = {
			'appetizers': appetizers,
			'entres': entres,
			'desserts':desserts,
			'drinks': drinks,
		}

		return render(request,'mycafe/order.html',context)
	def post(self,request,*args,**kwargs):
		name = request.POST.get('name')
		email = request.POST.get('email')
		street = request.POST.get('street')
		city = request.POST.get('city')
		state = request.POST.get('state')
		pin = request.POST.get('pin')
		order_items = {
			'items' : []
		}

		items = request.POST.getlist('items[]')

		for item in items:
			menu_item = MenuItems.objects.get(pk = int(item))
			item_data = {
				'id':menu_item.pk,
				'name': menu_item.name,
				'price': menu_item.price
			}

			order_items['items'].append(item_data)

			price =0
			item_ids = []
			
		for item in order_items['items']:
			price += item['price']
			item_ids.append(item['id'])
		
		# order = OrderModel.objects.create(
		# 	price=price,
		# 	name = name,
		# 	email = email,
		# 	street = street,
		# 	city = city,
		# 	state = state,
		# 	pin = pin
		# 	)
		# order.items.add(*item_ids)

		context = {
			'items': order_items['items'],
			'price':price
		}

		return render(request,'mycafe/order_confirmation.html',context)

