from rest_framework import serializers

from redcap_django.users.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', )
