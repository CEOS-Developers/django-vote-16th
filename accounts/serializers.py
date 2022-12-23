from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'name', 'part', 'team']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'], username=validated_data['username'],
            name=validated_data['name'], part=validated_data['part'], team=validated_data['team'])
        user.set_password(validated_data['password'])
        user.save()
        login(self.context['request'], user)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=64)
    password = serializers.CharField(max_length=500, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if user.check_password(password):
                token = RefreshToken.for_user(user)
                #refresh = str(token)
                access = str(token.access_token)

                data = {
                    'user': user.email,
                    'access_token': access,
                    'username': user.username
                }
                
                return data
            else:
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
        else:
            raise serializers.ValidationError('존재하지 않는 이메일입니다.')