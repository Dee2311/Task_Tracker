from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, ListForm, TaskForm
from .models import AddList, AddTask
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, ListSerializer, LoginSerializer
from django.core import serializers

# login

def user_login(request):

    # print(request, request.method)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            # print(user)
            if user is not None:
                login(request, user)
                print("redirect to viewList")
                return redirect('viewList')
        else:
            return render(request, 'Task/login.html', {'form': form})
    else:
        return render(request, 'Task/login.html', {'form': LoginForm()})

# adding list 

def addList(request):
    
    if request.method == 'POST':
        listName = request.POST["listName"]
        listView = AddList(listName=listName)
        listView.save()
        return redirect('viewList')
    else:
        print("i'm in addList")
        return render(request, 'Task/addList.html', {'add': ListForm()})

# view list

def viewList(request):
    # return HttpResponse("List of Task")
    list_view = AddList.objects.all()
    print("i'm in view",list_view)
    return render(request,'Task/viewList.html',{'lists': list_view}) 
    # return HttpResponse("List of Task")

# add task 

def addTask(request):

    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        expected_time = request.POST["expected_time"]
        due_date = request.POST["due_date"]
        status = request.POST.get('status')
        tasklist = AddTask(title=title, description=description, expected_time=expected_time, due_date=due_date, status=status)
        tasklist.save()
        return redirect(viewTask)
    else:
        return render(request, 'Task/addTask.html', {'form': TaskForm()})

# view task

def  viewTask(request):
    list_task = AddTask.objects.all()
    return render(request,'Task/viewTask.html',{'tasks': list_task}) 

# write the api view using REST framework

def list(request):
    
    if request.method == 'GET':
        article = AddList.objects.all()
        serializer = ListSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

def task(request):
    
    if request.method == 'GET':
        article = AddTask.objects.all()
        serializer = TaskSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ListView(APIView):
    def get(self,request):
        listView = AddList.objects.all()
        listData = ListSerializer(listView, many = True)
        return Response(listData.data)

    def post(self,request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(APIView):
    def get(self,request):
        task_list = AddTask.objects.all()
        data = TaskSerializer(task_list, )
        return Response(serializer.data)

class LoginView(APIView):

     def get(self,request):
        login = User.objects.all()
        loginData = LoginSerializer(login, many = True)
        return Response(loginData.data)

     def post(self, request, format=None):
         serializer = LoginSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)