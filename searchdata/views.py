import json
import subprocess
from threading import Thread

from django.http import HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template import Context, loader
from django.shortcuts import render
from django.forms import ModelForm
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.serializers.json import DjangoJSONEncoder

from searchdata.models import Question
# from searchdata.task import assimlilate_starting



# Create your views here.

def index(request):
	return render(request, 'searchdata/index.html')

def index1(request):
	return render(request, 'searchdata/index1.html')

def search_quarantine(request):
	return render(request, 'searchdata/search_quarantine.html')

def unquarantine_factory(request):
	return render(request, 'searchdata/unquarantine_factory.html')

def machines(request):
	machines = json.load(open('./machines.json','r'))
	return HttpResponse(json.dumps({"data":machines}))

@list_route(methods=["GET","POST" ])
# @api_view(['GET', 'POST'])
def start_assimilate(request):

    machines = request.POST.getlist('hostname[]')

    # output = "Please add a hostname to run the assimilate"
    for machine in machines:
        assimilate_details = Question.objects.filter(dns_name=machine)
        for machine_name in assimilate_details:
            if machine_name.assimilate_status =='running':
                return HttpResponse('Already assimilate is running for {}'.format(machine))
                # return output = "Already assimilate is running for {}" machine
        #     else:
        #         Question.objects.filter(dns_name=machine).update(assimilate_status="running", ran_date=timezone.now())
        # assimilate_start = ticket = Question(dns_name=machine, assimilate_status="running", ran_date=timezone.now())
        # assimilate_start.save()

        try:
            process = subprocess.Popen('python2.7 manage.py unqu -q -m {}'.format(machine) , shell=True, stdout=subprocess.PIPE)
            # output = process.communicate()[0]
            output = "Started assimilate script for {}".format(machine)
        except Exception as e:
            output =  e
            # Question.objects.filter(dns_name=machine).update(assimilate_status="NotGood", assimilate_error=str(e))
    return HttpResponse(output)

def assimilate_running_status(request):
    return render(request, 'searchdata/assimilate_running.html')


def assimilate_status_json(request):
    try:
        assimilate_details =    Question.objects.all().values()
        structure = json.dumps(list(assimilate_details), cls=DjangoJSONEncoder)
        # form = ArticleForm(instance=assimilate_details)
        #assimilate_details_json =serializers.serialize('json', [assimilate_details])
    except Exception as e:
        return HttpResponse(json.dumps(e))
    return HttpResponse(structure)






