from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
        new_user = User()
        new_user.name = data["name"]
        new_user.email = data["email"]
        new_user.password = data["password"]
        birthdate = datetime.strptime(data["birthdate"], '%Y-%m-%d').date()
        new_user.birthdate= birthdate
        new_user.save()
        return Response({'message': "Successfully added new user"})

@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data["email"]
    password = data["password"]
    user_queried = User.objects.filter(email = email).first()
    if not user_queried:
        return Response({"error":"email"}, status=400)
    if user_queried and user_queried.password == password:
        # Set the token expiration time
        token_exp = datetime.utcnow() + timedelta(hours=1)

        #crea el payload de JWT
        payload = {
            'id': user_queried.id,
            'exp': token_exp
        }
        #Genera el token JWT
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return Response({"loged": True, "token":token})
    if user_queried and user_queried.password != password:
        return Response({"error":"password"}, status=400)

@api_view(['POST'])
def validate_email(request):
    data = json.loads(request.body)
    user_queried = User.objects.filter(email=data["email"]).first()
    if user_queried:
        return Response({"email_in_use": True})
    else:
        return Response({"email_in_use": False})

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_user_information(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
    userQueried = User.objects.get(id=decoded_token["id"])
    dic = {"name":userQueried.name, "birthdate":userQueried.birthdate}
    return Response(dic)