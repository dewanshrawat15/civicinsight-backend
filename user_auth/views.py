import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serialisers import NewUserSerializer

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = NewUserSerializer

    @swagger_auto_schema(request_body=NewUserSerializer)
    def post(self, request):
        serializer = NewUserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserSessionAPI(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        print(user)
        return Response({
            "message": "Hello world"
        }, status=status.HTTP_200_OK)