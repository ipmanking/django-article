from django.shortcuts import render

# Create your views here.
def view_index(request):
    # from django.http import HttpResponse
    # return HttpResponse('hello')
    return render(request, 'index.html')

def view_about(request):
    return render(request, 'about.html')

def view_listpic(request):
    return render(request, 'listpic.html')

def view_newslistpic(request):
    return render(request, 'newslistpic.html')


