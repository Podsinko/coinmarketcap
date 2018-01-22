from django.shortcuts import render

# Create your views here.


def index(request):
    if 'coin' in request.POST:
        return render(request, 'page1/index.html',
                      {'coin': request.POST['coin']})
    return render(request, 'page1/index.html')
