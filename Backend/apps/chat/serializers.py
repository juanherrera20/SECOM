from rest_framework import serializers
from .models import Room, Message
from apps.usuarios.models import CustomUser

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        Model = CustomUser
        fields = ['id', 'username', 'img_profile']


class RoomSerializer(serializers.ModelSerializer):
    users = UserMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'state', 'create_date', 'chat_type', 'product', 'users']


class MessageSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'content', 'send_date', 'user', 'room', 'message_type', 'url']
        read_only_fields = ['send_date']

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['user'] = request.user
        return super().create(validated_data)
