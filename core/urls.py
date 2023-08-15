from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('settings', views.settings, name='settings'),

]