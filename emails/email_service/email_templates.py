from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
import django
import requests

class Email():
    
    def __init__(self, inputs):
        
        self.inputs = inputs

    def send(self):
        
        print('Send Email')
        address = '2818 67th Ave SE'
        emailTemplate = loader.render_to_string(
            'testEmail.html',
            {
                'permitNumber': self.inputs['permitNumber'],
                'projectName': self.inputs['projectName'],
                'address': self.inputs['address'],
                'submissionNumber': self.inputs['submissionNumber'],
                'planningStatus': self.inputs['planningStatus'],
                'buildingStatus': self.inputs['buildingStatus'],
                'engineeringStatus': self.inputs['engineeringStatus'],
                'treeStatus': self.inputs['treeStatus'],
                'fireStatus': self.inputs['fireStatus'],
            }
        )
        sendTo = str(self.inputs['contactEmail']+'; '+self.inputs['reviewerEmail'])
        print(sendTo)

        url = 'https://api.mailgun.net/v3/{}/messages'.format('sandboxf29bbdf6a07246b8b96099d769e570d5.mailgun.org')
        auth = ('api', 'key-11dbb88fd203333af892beaa9f408005')
        data = {
            'from': 'Mercer Island Permits <mailgun@{}>'.format('sandboxf29bbdf6a07246b8b96099d769e570d5.mailgun.org'),
            'to': sendTo,
            'subject': 'Building Review Comments for '+ address,
            'text': 'Plaintext content',
            'html': emailTemplate
        }
        response = requests.post(url, auth=auth, data=data)
        response.raise_for_status()