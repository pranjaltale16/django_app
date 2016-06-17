from django.conf.urls import url
from .import views
app_name = 'bookmarks'
urlpatterns = [
	url(r'^$', views.index, name ='index'),
	url(r'^login/$', views.login , name = 'login'),
	url(r'^newuser/$',views.newuser, name = 'newuser'),
	url(r'^authenticate/$',views.authenticate , name = 'authenticate'),
	url(r'^welcome/$',views.welcome, name = 'welcome'),
	url(r'^passwordupdate/$',views.passwordupdate, name = 'passwordupdate'),
	url(r'^changepassword/$',views.changepassword, name = 'changepassword'),
	url(r'^redirect/$', views.redirect, name = 'redirect'),
]
