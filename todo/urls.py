from django.urls import path
from .views import StatusList, TodoList, TodoDetail

urlpatterns = [
    path('status/', StatusList.as_view(), name='status-list'),
    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]