from django.urls import path
from .views import  Todocrud


urlpatterns = [
    path('', Todocrud.as_view(),),
    path('create', Todocrud.as_view()),
    path('update/<int:id>',Todocrud.as_view()),
    path('delete/<int:id>',Todocrud.as_view()),
    
    
	
]