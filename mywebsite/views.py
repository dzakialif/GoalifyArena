from django.shortcuts import render

def index(request):
    context = {'page_title': 'Welcome'}
    print(request.user)
    return render(request, 'index.html', context)