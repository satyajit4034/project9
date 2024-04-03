from django.shortcuts import render

# Create your views here.
def send_data(request):
    return render(request,'send_data.html',context={'name':'SATYAJIT','age':23})

