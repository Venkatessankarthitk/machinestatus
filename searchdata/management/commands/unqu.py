# coding=utf-8
import json
import subprocess
import sys

from django.core.management.base import NoArgsCommand, BaseCommand, CommandError
from django.utils import timezone
from optparse import make_option
from searchdata.models import Question

ASSIMILATE_SCRIPT = "/e2e/quarantine/fs/test/e2e/lib/tintri/assimilate.py"
REMEDIATOR = "/e2e/repos/fs/test/e2e/lib/tintri/remediator.py"

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option( '-q', '--unQuarantine', action='store_true', default= False, dest='unQuarantine', help='unQuarantine help'),
        make_option( '-m', '--machineName', action='store', type='str', dest='machineName', help='Host / Machine Name'),
    )

    def handle(self, *args, **options):

        if not options['machineName']:
            raise CommandError("Please provide atleast one machineName")

        machineNames = options['machineName'].split(',')
        self.run(machineNames, options['unQuarantine'])


    def run(self, machineNames, unQuarantine):
        try:
            for machine in machineNames:
                #result = subprocess.run('python2.7 {} {}'.format(ASSIMILATE_SCRIPT, machine), stdout=subprocess.PIPE)
                #result = subprocess.call(['pwd'], stdout=subprocess.PIPE)
                process = subprocess.Popen('{} --ignore_owner --ignore_quarantine {}'.format(ASSIMILATE_SCRIPT, machine) , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # import pdb
                # pdb.set_trace()


                assimilate_details = Question.objects.filter(dns_name=machine)
                if assimilate_details:
                    Question.objects.filter(dns_name=machine).update(assimilate_status="running",
                     ran_date=timezone.now(),assimilate_error="",remeditor_status="",remeditor_error="")
                else:
                    assimilate_start = Question(dns_name=machine, assimilate_status="running", ran_date=timezone.now())
                    assimilate_start.save()

                assimilate_out = process.communicate()
                #result = subprocess.Popen('tail -n 1 /tmp/{}_assimilate.log '.format(machine), shell=True, stdout=subprocess.PIPE)
                result_output = assimilate_out[0].splitlines()[-1]
                if 'successfully' in result_output:
                    Question.objects.filter(dns_name=machine).update(assimilate_status="Good")
                else:
                    Question.objects.filter(dns_name=machine).update(assimilate_status="NotGood", assimilate_error=str(result_output))
                    remediator = subprocess.Popen('python2.7 {} --target_machine {}'.format(REMEDIATOR, machine) , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    remediate_out = remediator.communicate()
                    if remediate_out[1] != '':
                        remediator_msg = remediate_out[1]
                    else:
                        remediator_msg = remediate_out[0]
                    remediator_output = remediator_msg.splitlines()[-1]
                    if 'successfully' in remediator_output:
                        Question.objects.filter(dns_name=machine).update(remeditor_status="Good")
                    else:
                        Question.objects.filter(dns_name=machine).update(remeditor_status="NotGood", remeditor_error=str(remediator_output))
        except Exception as e:
            Question.objects.filter(dns_name=machine).update(assimilate_status="NotGood", assimilate_error=str(e))

