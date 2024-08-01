from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from .pagination import *
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
@api_view(['GET'])
def todo_list(request):
    todos=Todo.objects.all()
    paginator=TodoPagination()
    page=paginator.paginate_queryset(todos, request)
    if page is not None:
        serializer=TodoListSerializer(todos, many=True)
        return paginator.get_paginated_response(serializer.data)
    serializer=TodoListSerializer(todos, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def todo_detail(request, id):
    todo=get_object_or_404(Todo, id=id)
    serializer=TodoDetailSerializer(todo)
    return Response(serializer.data)