from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {   #Dictionary
    "name" : "Nijal",
    "age" : 18,
    "nation" : "India",
  }
  print(type(context))
  return render(request,'index.html',context)

def count(request):
  text=request.POST['text']
  word=len(text.split())
  return render(request,'count.html',{'word':word})