from django.shortcuts import render

# Create your views here.
def run(request, *args, **kwargs):
    return render(request, "Algorithm/hello.html")