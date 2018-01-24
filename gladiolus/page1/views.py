from parser import coinmarket, localtime

from django.shortcuts import render

# Create your views here.


def index(request):
    if 'coin' in request.POST:
        data = coinmarket(request.POST['coin'])
        if data:
            for d in data:
                d.update({'percent_change_24h': float(
                    d['percent_change_24h']),
                    'last_updated': localtime(d['last_updated']),
                    'price_usd': float(d['price_usd'])})
            return render(request, 'page1/index.html',
                          {'coin': data,
                           'datalinks': [float(d['price_usd']) for d in data],
                           'names': '/'.join([d['name'] for d in data]),
                           'changes': [float(d['percent_change_24h']
                                             ) for d in data],
                           'supplies': [float(d['total_supply']
                                              ) for d in data]})
    return render(request, 'page1/index.html')
