from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from django.http import HttpResponseBadRequest
import jwt
from datetime import datetime, timedelta

import json
# Create your views here.
@api_view(['GET'])
def say_hello(request):
    """
    returns a json response
    methods: GET
    args:request
    """
    return Response({'message': "Hello world"})
@api_view(['POST'])
def register(request):
    data = json.loads(request.body)
    email = data["email"]
    print(data)
    checkuser = User.objects.filter(email = email).first()
    if checkuser:
        return HttpResponseBadRequest("User already exist")
    else:
        newUser = User()
        newUser.email = data["email"]
        newUser.password = data["password"]
        newUser.save()
        return Response({'message': "Successfully added new user"})

@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data["email"]
    password = data["password"]
    userQueried = User.objects.filter(email = email).first()
    if userQueried and userQueried.password == password:
        # Set the token expiration time
        token_exp = datetime.utcnow() + timedelta(hours=1)

    # Create the JWT payload
        payload = {
            'email': userQueried.email,
            'exp': token_exp
    }

    # Generate the JWT token
        token = jwt.encode(payload, 'holamundo', algorithm='HS256')
        return Response({"token":token})
        #crear token
    if userQueried and userQueried.password != password:
        return HttpResponseBadRequest("wrong password")
    if not userQueried:
        return HttpResponseBadRequest("User doesnt exist")

@api_view(['GET'])
def get_email(request):
    data = json.loads(request.body)
    token = data['token']
    decoded_token = jwt.decode(token, 'holamundo', algorithms=['HS256'])
    return Response(decoded_token)