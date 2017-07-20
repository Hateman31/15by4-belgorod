from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're on the page by Belgorod branch of 15x4.")
