from rest_framework import serializers
from .models import CheckTime

class CheckTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckTime
        fields = ('id','name_text','in_or_out','timestamp')

