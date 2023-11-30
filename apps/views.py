from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is home page")

def chatBot_openAI(request):
    return HttpResponse("This is openAI chatbot Page")