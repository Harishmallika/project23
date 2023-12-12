from django.shortcuts import render

# Create your views here.



def card17(request):
    return render(request,'card17.html')



def parent(request):
    return render(request,'parent.html')  

def child(request):
    return render(request,'child.html')      