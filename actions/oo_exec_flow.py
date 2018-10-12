import sys
import requests
import datetime

from st2common.runners.base_action import Action

class OOFlowExecutionAction(Action):
    def run(self, oo_flow_id,oo_flow_name):
         self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
         self._logger.info("OOFlowExecutionAction triggered "+ str(datetime.datetime.now()));
         self._logger.info(oo_flow_id)
         self._logger.info(oo_flow_name)
         # r = requests.post('http://hpoo.demodxc.com:8080/oo/rest/v2/executions', auth=('svc_hpoo','ph00$Vc'), json={'flowUuid':'9307a65d-a4c2-4495-9bee-9c77413b6baa','runname':'Smart Store transaction failure for user'})
         # print(r.status_code) # HTTP 201 is ok
         # print(r.json()) # Prints the Run-ID
         # return (True, r.json())  
         return (True," OO Action "+ str(datetime.datetime.now()))