from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render

import uuid

from .forms import CustomerAppForm
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
        app = CustomerApp()

    if request.method == 'POST':
        form = CustomerAppForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            token = form.cleaned_data['token']
            client = form.cleaned_data['client']
            status = form.cleaned_data['status']

            app.name = name
            app.token = token
            app.client = client
            app.status = status
            app.save()

            return HttpResponseRedirect(f'/apps/')
        else:
            return  HttpResponse(form.errors.values())


    else:
        initial = {
            "name": app.name,
            "token": app.token,
            "status": app.status
        }
        form = CustomerAppForm(initial=initial)
        return render(
            request, 'app.html',
            {
                'form': form,
                'app': app,
                'statuses': dict(CustomerApp.Status.choices)
            }
        )

def add_app(request):
    app = CustomerApp(token=str(uuid.uuid4().hex)[:20])
    form = CustomerAppForm()
    return render(
        request, 'app.html',
        {
            'form': form,
            'app': app,
            'statuses': dict(CustomerApp.Status.choices)
        }
    )

def delete_app(request, token):
    try:
        app = CustomerApp.objects.get(token=token)
        app.delete()
    except CustomerApp.DoesNotExist:
        pass
    return HttpResponseRedirect('/apps/')