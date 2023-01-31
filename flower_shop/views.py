from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    rendere_page = template.render(context, request)
    return HttpResponse(rendere_page)
