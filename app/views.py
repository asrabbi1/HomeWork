from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from .pagination import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    person1={
        'name':'salam',
        'age': 18,
        'height':5.5
    }
    person2={
        'name':'Rabbi',
        'age': 20,
        'height':5.6
    }
    persons=[person1,person2]
    return Response(persons)
@api_view(['GET','POST'])
def todo_list(request):
    todos=Todo.objects.all()
    if request.method == 'GET':
        paginator=TodoPagination()
        page=paginator.paginate_queryset(todos, request)
        if page is not None:
            serializer=TodoListSerializer(todos, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer=TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data=request.data
        serializer=TodoCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PATCH','DELETE'])
def todo_detail(request, id):
    todo=get_object_or_404(Todo, id=id)
    if request.method == 'GET':
        serializer=TodoDetailSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data=request.data
        serializer=TodoDetailSerializer(todo, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, sttaus=status.HTTP_400_BAD_REQUEST)
   
   
    if request.method == 'DELETE':
        todo.delete()
        message={"success:Todo has been deleted successfully"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)