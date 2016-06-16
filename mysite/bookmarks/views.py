from django.shortcuts import render
from . models import user
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
def index(request):
	variable = user.objects.all()
	context = {'variable' : variable}
	return render(request,'bookmarks/index.html',context)

def login(request):
	variable = user.objects.all()
	context = {'variable':variable}
	return render(request,'bookmarks/login.html',context)
def newuser(request):
	variable = user.objects.all()
	context = {'variable':variable}
	return render(request, 'bookmarks/new_user.html',context)
def authenticate(request):
	uname = request.POST['username']
	email = request.POST['emailid']
	passwrd = request.POST['password']
	passwrd1 = request.POST['password1']
	if(passwrd != passwrd1 ):
		variable = user.objects.all()
	        context = {'variable':variable}
       		return render(request, 'bookmarks/new_user.html',context)

	else:
		q = user(username = uname, emailid = email, password = passwrd) 
		q.save()
		return HttpResponseRedirect(reverse('bookmarks:login'))
def welcome(request):
	q = user.objects.get(username = request.POST['username'])
	if(q.password == request.POST['password']):
		context = {'q':q}
		return render(request,'bookmarks/welcome.html',context)
	else:
		variable = user.objects.all()
		context = {'variable': variable}
		return HttpResponseRedirect(reverse('bookmarks:login'))
def passwordupdate(request):
	return HttpResponse("yo")	
# Create your views here.

