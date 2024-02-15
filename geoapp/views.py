from django.shortcuts import render
from rest_framework import viewsets
from .models import MunDetail, StaffDetail, WardDetail, DangPop
from .serializers import MunDetailSerializer, StaffDetailSerializer, WardDetailSerializer, DangPopSerializer

# Create your views here.
class MunDetailViewset(viewsets.ModelViewSet):
    queryset = MunDetail.objects.all()
    serializer_class = MunDetailSerializer

class StaffDetailViewset(viewsets.ModelViewSet):
    queryset = StaffDetail.objects.all().order_by('level')
    serializer_class = StaffDetailSerializer
    
class WardDetailViewset(viewsets.ModelViewSet):
    queryset = WardDetail.objects.all().order_by('wardNo')
    serializer_class = WardDetailSerializer

class DangPopViewset(viewsets.ModelViewSet):
    queryset = DangPop.objects.all()
    serializer_class = DangPopSerializer