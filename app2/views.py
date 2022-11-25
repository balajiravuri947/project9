from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d3={'a':100,'b':200,'c':300}
    return render(request,'a2_first.html',d3)
def a2_second(request):
    d4={'a':'hello'}
    return render(request,'a2_second.html',d4)