from parser import coinmarket

from django.shortcuts import render

# Create your views here.


def index(request):
    if 'coin' in request.POST:
        data = coinmarket(request.POST['coin'])
        if data:
            return render(request, 'page1/index.html',
                          {'coin': data})
        else:
            return render(request, 'page1/index.html',
                          {'coin': "NO COIN FOUND!"})
    return render(request, 'page1/index.html')
