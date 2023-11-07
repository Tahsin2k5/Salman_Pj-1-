from django.shortcuts import HttpResponse, render


def CO_fun(request):
    
    return render(request,'user/CO.html')