from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from django.views import View
from datetime import datetime
from .models import PostModel

def text (request):
    return HttpResponse('this is test')

class Task(View):
    def get(self,request):
        return HttpResponse('this is my task')
    
    def get(self,request):
        context=PostModel.objects.order_by('name').all()
        # context=[
        #     {
        #     'firstname': 'Nurana',
        #     'surname': 'Aliyarli',
        #     'age': '18'
        # },
        # {
        #     'firstname': 'Shahin',
        #     'surname': 'Aliyarli',
        #     'age': '22'
        # } 
        # ]
        return render(request, "article.html", {'context':context})
    
class NewPost(View):
     def get(self,request):
      return render(request,'create_articles.html')
     
     def post(self,request):
         name=request.POST.get('name', 'unknown')
         surname=request.POST.get('surname', 'unknown')
         age=request.POST.get('age', 'unknown')
         faculty=request.POST.get('faculty', 'unknown')

         PostModel.objects.create(
             name=name,
             surname=surname,
             age=age,
             faculty=faculty
         )
         return redirect('task')
    
    
