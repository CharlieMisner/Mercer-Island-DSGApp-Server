from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from emails.email_service.email_templates import Email
import requests

class EmailTest(APIView):
            
    def post(self, request, format=None):
        newEmail = Email(request.data)
        newEmail.send()
        return Response({"test": "success"}, status=status.HTTP_200_OK)
        