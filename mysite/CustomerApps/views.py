from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import CustomerApp


def index(request):
    context = {
        'apps': CustomerApp.objects.all(),
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def app(request, token):
    try:
        app = CustomerApp.objects.get(token=token)
    except CustomerApp.DoesNotExist:
        app = None
    context = {
        'app': app
    }
    template = loader.get_template('app.html')
    return HttpResponse(template.render(context, request))

def add_app(request):
    context = {
        'apps': CustomerApp.objects.all(),
    }
    template = loader.get_template('app.html')
    return HttpResponse(template.render(context, request))