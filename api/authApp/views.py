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
        newUser = User()
        newUser.name = data["name"]
        newUser.email = data["email"]
        newUser.password = data["password"]
        birthdate = datetime.strptime(data["birthdate"], '%Y-%m-%d').date()
        newUser.birthdate= birthdate
        newUser.save()
        return Response({'message': "Successfully added new user"})

@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data["email"]
    password = data["password"]
    userQueried = User.objects.filter(email = email).first()
    if not userQueried:
        return Response({"error":"email"}, status=400)
    if userQueried and userQueried.password == password:
        # Set the token expiration time
        token_exp = datetime.utcnow() + timedelta(hours=1)

        #crea el payload de JWT
        payload = {
            'id': userQueried.id,
            'exp': token_exp
        }
        #Genera el token JWT
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return Response({"loged": True, "token":token})
    if userQueried and userQueried.password != password:
        return Response({"error":"password"}, status=400)
    
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_user_information(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
    userQueried = User.objects.get(id=decoded_token["id"])
    dic = {"name":userQueried.name, "birthdate":userQueried.birthdate}
    return Response(dic)