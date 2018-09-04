from django.shortcuts import render


def list(request):
    return render(request, 'blog/list.html', {})

def detail(request, pk):
    return render(request, 'blog/detail.html', {})