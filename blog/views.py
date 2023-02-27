from django.shortcuts import render
#from django.http import HttpResponse


posts = [
    {
        'author': 'Ikechukwu',
        'title': 'How I Love Jesus',
        'content': 'I cannot tell it all',
        'date_posted': 'February 26, 2053',
    },
    {
        'author': 'Austine',
        'title': 'How I Love Momo',
        'content': 'I cannot tell it all Yhello',
        'date_posted': 'February 26, 2043',  
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})