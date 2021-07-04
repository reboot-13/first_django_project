from django.shortcuts import render
# Create your views here.

def say_hi (request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'name': 'Roman'
        }
    }
    return render (request, 'main/index.html', data )

def about (request):

    return render(request, 'main/about.html')

def contact_info (request):
    return render(request, 'main/contacts.html')

def django_master (request):
    data = {
        'title': 'Джанго мастер',
        'anonimouses': [{
            'name': 'Dungeoner'
        }, {
            'name': 'Ricardo'
    }, {
            'name': 'Cumill'
    }, {
            'name': 'Dickon'
    }]
    }
    return render(request, 'main/django_boy.html', data)