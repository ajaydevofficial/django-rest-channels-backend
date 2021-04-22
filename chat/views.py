from django.contrib.auth.models import User, Group
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes, permission_classes, parser_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

@api_view(['GET'])
def fetch_users(request):
    try:
        content = User.objects.all().values()
        return Response(content,status=status.HTTP_200_OK)
    except Exception as e:
        content = {"error": str(e)}
        return Response(content,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_groups(request):
    try:
        content = Group.objects.all().values()
        return Response(content,status=status.HTTP_200_OK)
    except Exception as e:
        content = {"error": str(e)}
        return Response(content,status=status.HTTP_400_BAD_REQUEST)