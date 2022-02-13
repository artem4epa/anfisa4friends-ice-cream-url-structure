from django.shortcuts import render


def index(request):
    template = 'ice_cream/index.html'
    text = 'Ночь, <br> улица, <br>фонарь, <br>аптека, <br>бессмысленный и тусклый свет,<br> живи еще хоть четверть ' \
           'века<br> все будет так<br> исхода ' \
           'нет, <br>умрешь и вновь начнешь с начала <br>и повторится все как в старь: <br>ночь,<br> ледяная рябь канала,<br> аптека, улица,' \
           'фонарь'
    title = 'Пипец'
    context = {
        'text': text,
        'title': title
    }
    return render(request, template, context)

def first(request):
    template = 'ice_cream/first.html'
    text = 'Это первая страница'
    title = 'Жара'
    context = {
        'text': text,
        'title': title
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = ''
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
