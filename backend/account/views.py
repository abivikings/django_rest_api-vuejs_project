from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, views
from .utils import generate_access_token, generate_refresh_token


@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        try:
            password = request.data['password']
            hash_pass = make_password(password, salt=None, hasher='default')
            User.objects.create(first_name=request.data['first_name'],
                                last_name=request.data['last_name'],
                                email=request.data['email'],
                                username=request.data['username'],
                                password=hash_pass)
            return Response(request.data, status=status.HTTP_200_OK)
        except IntegrityError as e:
            if e.args[0]:
                return JsonResponse({"error": "username already exist!!"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class Login(views.APIView):
    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'error': "Please provide username/password"}, status="400")

        username = request.data['username']
        password = request.data['password']
        response = Response()
        try:
            user = User.objects.filter(username=username)
            check_password(password, 'encoded', setter=None, preferred='default')
            if check_password(password, user[0].password):
                if user:
                    access_token = generate_access_token(user)
                    refresh_token = generate_refresh_token(user)
                    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=False, expires=None, path='/',
                                        domain=None, secure=False)
                    response.data = {
                        'access_token': access_token,
                        'user': user[0].username,
                    }

                    return response
                else:
                    return Response(
                        {'Error': "Invalid credentials"},
                        status=400,
                        content_type="application/json"
                    )
        except:
            return JsonResponse({'error': "Invalid username/password"})
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def profile(request):
    value = request.COOKIES.get('cookie_name')
    print(value)
    return Response(status=status.HTTP_200_OK)
