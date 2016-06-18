from django.shortcuts import render
from . models import user
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
def redirect(request):
	return HttpResponseRedirect(reverse('polls:index'))
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
		request.session['username'] = q.username
		context = {'q':q}
		return render(request,'bookmarks/welcome.html',context)
	else:
		variable = user.objects.all()
		context = {'variable': variable}
		return HttpResponseRedirect(reverse('bookmarks:login'))
def passwordupdate(request):
	return render(request,'bookmarks/passwordupdate.html')
def changepassword(request):
	uname = request.POST['username']
	password = request.POST['oldpassword']
	newpass = request.POST['newpassword']
	newpass1 = request.POST['newpassword1']
	q = user.objects.get(username = uname)
	if(q.password == password):
		if(newpass == newpass1):
			q.password = newpass
			q.save()
			return render(request,'bookmarks/index.html')
	else:
		return HttpResponse("Details does not match")
def logout(request):
	del request.session['username']
	return HttpResponseRedirect(reverse('bookmarks:index'))	
		
		
# Create your views here.

