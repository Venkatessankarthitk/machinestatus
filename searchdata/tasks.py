import json
import subprocess


from django.utils import timezone
from searchdata.models import Question
from __future__ import absolute_import, unicode_literals
from celery import shared_task



@shared_task
def assimlilate_starting(machines):
    for machine in machines:
        assimilate_details = Question.objects.filter(dns_name=machine)
        for machine_name in assimilate_details:
            if machine_name.assimilate_status =='running':
                return 'Already assimilate is running for {}'.format(machine)
                # return output = "Already assimilate is running for {}" machine
            else:
                Question.objects.filter(dns_name=machine).update(assimilate_status="running", ran_date=timezone.now())
        assimilate_start = ticket = Question(dns_name=machine, assimilate_status="running", ran_date=timezone.now())
        assimilate_start.save()
        try:
            process = subprocess.Popen('python2.7 manage.py unqu -q -m {}'.format(','.join(machines)) , shell=True, stdout=subprocess.PIPE)
            output=process.communicate()[0]
            output = "Started assimilate script for {}".format(machines)
        except Exception as e:
            output =  e
        return json.dumps(output)