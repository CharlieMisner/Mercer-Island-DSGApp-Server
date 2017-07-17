from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from emails.email_templates.email_templates import TestEmail

class EmailTest(APIView):
            
    def post(self, request, format=None):
        print('test')
        emailTemplate = loader.render_to_string(
            'testEmail.html',
            {
                'user_name': 'charlie',
                'subject':  'test',
            }
        )
        TestEmail.send(self, emailTemplate)
        return Response({"test": "success"}, status=status.HTTP_200_OK)
        
        """serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
# Create your views here.
