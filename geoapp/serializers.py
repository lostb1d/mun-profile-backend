from rest_framework import serializers
from .models import MunDetail, StaffDetail, WardDetail, DangPop

class MunDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunDetail
        fields = '__all__'

class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffDetail
        fields = '__all__'

class WardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardDetail
        fields = '__all__'

class DangPopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DangPop
        fields = '__all__'