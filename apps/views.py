from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("This is home page")
    return render(request,"index.html")

def chatWithOpenAI(request):
    return HttpResponse("This is openAI chatbot Page")