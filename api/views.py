from rest_framework import status
from rest_framework.views import APIView,Response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class Todocrud(APIView):
    def get(self,request):
        task=Task.objects.all()
        task_data=TaskSerializer(task,many=True).data
        response_data={"datas":task_data}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def post(self,request):
        title = request.data.get('title')
        completed=request.data.get('completed')
        Task.objects.create(title=title,completed=completed)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        title = request.data.get('title')
        completed=request.data.get('completed')
        task = Task.objects.filter(id=id)
        
        if task is None:
            response_data = {"response":"Item doesnot exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        task.title = title
        task.completed = completed
        for i in task:
            i.title = title
            i.completed = completed
            i.save()
            
        
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        id=request.data.get('id')
        task=Task.objects.filter(id=id).first()
        if task is None:
            response_data={"response":"item doesnt exist"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        task.delete()
        response_data={"response":"deleted"}
        return Response(response_data,status=status.HTTP_200_OK)
        
           
    
   



