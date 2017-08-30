from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from emails.email_service.email_templates import TestEmail
import requests

class EmailTest(APIView):
            
    def post(self, request, format=None):
        print('test')
        TestEmail.send(self)
        return Response({"test": "success"}, status=status.HTTP_200_OK)
        