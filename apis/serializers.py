from rest_framework_simplejwt import serializers as jwt_serial


class TokenObtainPairSerializer(jwt_serial.TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)
        data.update(refresh.payload)
        return data
