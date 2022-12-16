from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'base/errors/404-page.html')


def server_error(request):
    return render(request, 'base/errors/500-page.html')
