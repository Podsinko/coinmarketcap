from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'page1/index.html')
    if 'coin' in request.POST:
        coin = request.POST['coin']
        return render(request, 'page1/index.html', {'coin': coin})
