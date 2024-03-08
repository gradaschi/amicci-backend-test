from rest_framework import serializers
from .models import Briefing


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'
