from django.contrib.auth import logout
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import *

# Create your views here.

class SignUpView(views.APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(
            context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data})
        return Response({'message': '회원가입 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'message': '유저 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


class LoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.validated_data}, status=HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    def get(self, request, format=None):
        logout(request)
        return Response({'message': "로그아웃 성공"}, status=HTTP_200_OK)