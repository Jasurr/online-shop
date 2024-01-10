from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'About us',
        'text_on_page': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do'
    }
    return render(request, 'main/about.html', context)
