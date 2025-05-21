from django.urls import path
from .views import NewPost, text,Task

urlpatterns = [
    path('post/', text),
    path('task/', Task.as_view(), name='task'),
    path('test/', NewPost.as_view(), name='test')
    
]