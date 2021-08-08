from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.http import  HttpResponse
from django.contrib import messages
from .models import Item
from django.contrib.auth.decorators import login_required
from .form import ItemForm

def home(request):
	return render(request, 'home.html')

def loginuser(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username, password=password)

		if user is not None:
			login(request,user)
			print('login sucess')
			return redirect('dashboard')
			
		else:
			messages.info(request,'Username or Password is incorrect')
			print("login credential wrong")
			return redirect('login')
			
	else:
		print("get request")
		return render(request, 'login.html')
		
def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def dashboard(request):
	items=Item.objects.filter(user=request.user)
	return render(request, 'dashboard.html',{'items':items})

def register(request):
	if request.method=='POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')

		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username already taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email already taken')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username,password=password, email=email,first_name=first_name, last_name=last_name)
				user.save();
				print('user created')
		else:
			messages.info(request,'both password are not same')
			return redirect('register')
			print('password not matching')
		return redirect('login')

	else:
		return render(request, 'register.html')

@login_required(login_url='login')
def add(request):
	if request.method=='POST':
		fm = ItemForm(request.POST)
		if fm.is_valid():
			obj=fm.save(commit=False)
			obj.user=request.user
			obj.save()
			return redirect('dashboard')
		else:
			messages.info(request,'both password are not same')
			return redirect('add')
	else:
		fm = ItemForm()
	return render(request, 'add.html',{'form':fm})

@login_required(login_url='login')
def delete_data(request,id):
	if request.method=='POST':
		obj= Item.objects.get(pk=id)
		obj.delete()
		return HttpResponseRedirect('/dashboard')

@login_required(login_url='login')
def update_data(request,id):
	if request.method=='POST':
		obj= Item.objects.get(pk=id)
		fm = ItemForm(request.POST,instance=obj)
		if fm.is_valid():
			fm.save()
		return HttpResponseRedirect('/dashboard')
	else:
		obj= Item.objects.get(pk=id)
		fm = ItemForm(instance=obj)
		return render(request, 'update.html',{'form':fm})