from parser import coinmarket

from django.shortcuts import render

# Create your views here.


def index(request):
    if 'coin' in request.POST:
        data = coinmarket(request.POST['coin'])
        if data:
            for d in data:
                d.update({'price_usd': float(d['price_usd'])})
            return render(request, 'page1/index.html',
                          {'coin': data})
    return render(request, 'page1/index.html')
