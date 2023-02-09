from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
# Create your views here.
@api_view(['GET'])
def say_hello(request):
    """
    returns a json response
    methods: GET
    args:request
    """
    return Response({'message': "Hello world"})
