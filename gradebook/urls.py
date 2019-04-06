from django.urls import path
from . import views

urlpatterns = [
	path('cs2150/', views.cs2150, name='cs2150'),	
	path('cs2150_result/', views.cs2150_result, name='cs2150_result')
]
