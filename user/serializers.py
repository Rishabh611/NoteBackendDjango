from rest_framework import serializers 

from .models import User
from notes.models import Notes

class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset = Notes.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'notes']