from django.shortcuts import render



def Index(request):
    
    return render(request,"projects/index.html")