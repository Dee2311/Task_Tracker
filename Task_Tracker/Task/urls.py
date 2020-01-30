from django.urls import path
from . import views


urlpatterns = [
    
    path('login/',views.user_login, name='login' ),
    path('addTask/',views.addTask, name='addTask'),
    path('viewTask/',views.viewTask, name='viewTasK'),
    path('addList/',views.addList, name='addList'),
    path('viewList/',views.viewList, name='viewList'),
    path('api/list',views.list,name='list'),
    path('api/task',views.task,name='task'),

    
]