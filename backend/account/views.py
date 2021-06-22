from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        try:
            User.objects.create(first_name=request.data['first_name'],
                                last_name=request.data['last_name'],
                                email=request.data['email'],
                                username=request.data['username'],
                                password=request.data['password'])
            return Response(request.data, status=status.HTTP_200_OK)
        except IntegrityError as e:
            if e.args[0]:
                return JsonResponse({"error": "username already exist!!"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
