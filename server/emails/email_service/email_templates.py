from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
import django
import requests

class TestEmail():

    def send(self):
        print('test email')
        address = '2818 67th Ave SE'
        emailTemplate = loader.render_to_string(
            'testEmail.html',
            {
                'permitNumber': '1612-159',
                'projectName': 'Chen',
                'address': address,
                'submissionNumber': 'SUB1',
                'planningStatus': 'WCI',
                'buildingStatus': 'APPROVED',
                'engineeringStatus': 'WCI',
                'treeStatus': 'IN REVIEW',
                'fireStatus': 'WCI',
            }
        )
        url = 'https://api.mailgun.net/v3/{}/messages'.format('sandboxf29bbdf6a07246b8b96099d769e570d5.mailgun.org')
        auth = ('api', 'key-11dbb88fd203333af892beaa9f408005')
        data = {
            'from': 'Charlie Misner <mailgun@{}>'.format('sandboxf29bbdf6a07246b8b96099d769e570d5.mailgun.org'),
            'to': 'charliemisner@gmail.com; charlie.misner@mercergov.org',
            'subject': 'Building Review Comments for '+ address,
            'text': 'Plaintext content',
            'html': emailTemplate
        }
        response = requests.post(url, auth=auth, data=data)
        response.raise_for_status()