from re import S
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
import json

# Create your views here.



class sendEmail(APIView):
    authentication_classes = []


    def get(self, request, *args, **kwargs):
        return render(request, 'email_sender/email_sending_page.html')

    @method_decorator(csrf_exempt)
    def post(self, request, format=None, *args, **kwargs):
        content = {}

        data = json.loads(request.body)
        if type(data) is not type(dict()):
            content["message"] = 'Body should be a JSON object'
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
        if 'recipient' not in data or 'email_body' not in data:
            content["message"] = 'body needs to be in the following json format { "recipient" : str (max 80 char), "email_body" : str }'
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
        sendable_email_list = ['numchai@swiftdynamics.co.th','sapjarern@swiftdynamics.co.th','varit@swiftdynamics.co.th','teemthai@outlook.com',]
        if data["recipient"] not in sendable_email_list:
            content["message"] = 'recipient not in sendable_email_list, please check the recipient email'
            return Response(content, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        self.send_email("quiz_for_swift_dynamics",data['email_body'],data['recipient'])
        content["message"] = f'Email has been sent to {data["recipient"]}'
        return Response(content, status=status.HTTP_200_OK)
    
    @staticmethod
    def send_email(subject, message, recipient_list):
        email_from = settings.EMAIL_HOST_USER
        if type(recipient_list) is type(str()):
            recipient_list = [recipient_list]
        send_mail( subject, message, email_from, recipient_list)
