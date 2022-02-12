from django.shortcuts import render


def index(request):
    template = 'ice_cream/index.html'
    text = 'Ворона'
    title = 'Пипец'
    context = {
        'text': text,
        'title': title
    }
    return render(request, template, context)

def first(request):
    template = 'ice_cream/first.html'
    return render(request, template, context)


def ice_cream_list(request):
    template = ''
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
