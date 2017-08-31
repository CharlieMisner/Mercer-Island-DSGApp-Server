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
        address = self.inputs['address']
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
        sendToReviewer = str(self.inputs['reviewerEmail'])
        sendToContact = str(self.inputs['contactEmail'])
        print(sendToContact)

        url = 'https://api.mailgun.net/v3/{}/messages'.format('sandboxd306d296f1724c9380f0d87f2c9e160e.mailgun.org')
        auth = ('api', 'key-52cf3a9108594d34c127c1ad7def07d5')
        dataReviewer = {
            'from': 'Mercer Island Permits <mailgun@{}>'.format('sandboxd306d296f1724c9380f0d87f2c9e160e.mailgun.org'),
            'to': sendToReviewer,
            'subject': 'Building Review Comments for '+ address,
            'text': 'Plaintext content',
            'html': emailTemplate
        }
        dataContact = {
            'from': 'Mercer Island Permits <mailgun@{}>'.format('sandboxd306d296f1724c9380f0d87f2c9e160e.mailgun.org'),
            'to': sendToContact,
            'subject': 'Building Review Comments for '+ address,
            'text': 'Plaintext content',
            'html': emailTemplate
        }
        response = requests.post(url, auth=auth, data=dataReviewer)
        response.raise_for_status()
        response1 = requests.post(url, auth=auth, data=dataContact)
        response1.raise_for_status()