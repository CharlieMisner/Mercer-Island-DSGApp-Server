from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
import django

class TestEmail():

    def send(self, html_message):
        print('test email')
        #html_message = '<p>This is a</p> <p><b>test</b></p><p>of html</p>'
        send_mail('Test', 'test', 'charlie.misner@mercergov.org', ['charliemisner@gmail.com'], html_message=html_message)