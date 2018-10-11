from jira.client import JIRA

from st2reactor.sensor.base import PollingSensor


class JiraOOSensor(PollingSensor):
    def setup(self):
        # Setup stuff goes here. For example, you might establish connections
        # to external system once and reuse it. This is called only once by the system.
		self._jira_client = JIRA('http://jira-ams.demodxc.com',auth=('autoresolver', 'password'))
        pass

    def poll(self):
       	for issue in jira.search_issues('project = ATMTDEMO and created >= -1d and (description ~ sobhan or  description ~glsr)', maxResults=30):
			self._dispatch_issues_trigger(issue)
	    pass

    def cleanup(self):
        # This is called when the st2 system goes down. You can perform cleanup operations like
        # closing the connections to external system here.
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass

    def _dispatch_issues_trigger(self, issue):
        trigger = 'jira_oo.oo_issues_tracker'
        payload = {}
        payload['issue_name'] = issue.key
        payload['issue_url'] = issue.self
        payload['issue_browse_url'] = self._jira_url + '/browse/' + issue.key
        payload['project'] = self._project
        payload['created'] = issue.raw['fields']['created']
        payload['assignee'] = issue.raw['fields']['assignee']
        payload['summary'] = issue.raw['fields']['summary']
		payload['description'] = issue.raw['fields']['description']
        payload['issue_type'] = issue.raw['fields']['issuetype']['name']
        self._sensor_service.dispatch(trigger, payload)