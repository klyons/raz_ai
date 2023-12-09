from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, DeleteView, TaskUpdate

# youtube tutorial
# https://www.youtube.com/watch?v=llbtoQTt4qw 41 minutes in


urlpatterns = [
	path('', TaskList.as_view(), name='tasks'),
	path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
	path('task-create/', TaskCreate.as_view(), name='task-create'),
	path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
	path('task-delete/<int:pk>/',DeleteView.as_view(),name='task-delete'),
]