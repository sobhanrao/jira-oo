import sys
import requests

from st2common.runners.base_action import Action

class OOFlowExecutionAction(Action):
    def run(self, flowid,flowname):
         print(flowid)
         print(flowname)
         # r = requests.post('http://hpoo.demodxc.com:8080/oo/rest/v2/executions', auth=('svc_hpoo','ph00$Vc'), json={'flowUuid':'9307a65d-a4c2-4495-9bee-9c77413b6baa','runname':'Smart Store transaction failure for user'})
         # print(r.status_code) # HTTP 201 is ok
         # print(r.json()) # Prints the Run-ID
         # return (True, r.json())  
         return (True," OO Action "+datetime.datetime.now())