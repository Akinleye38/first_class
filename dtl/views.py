from django.shortcuts import render

# Create your views here.

def new_view(request):
    #context data (can include variables, list, e.t.c)
    context = {
        'page_title': 'dtl',
        'items': ['Apple', 'Banana', 'Cherry'],
        'show_message': True,
        'message': 'Welcome to the DTL page!'
    }
    return render(request, 'dtl/dtl.html', context)
