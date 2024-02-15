from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MunDetailViewset, StaffDetailViewset, WardDetailViewset, DangPopViewset

router = DefaultRouter()
router.register(r'MunDetails',MunDetailViewset, basename='MunDetail')
router.register(r'StaffDetails', StaffDetailViewset, basename='StaffDetail')
router.register(r'WardDetails', WardDetailViewset, basename='WardDetail')
router.register(r'DangPop', DangPopViewset, basename='DangPop' )

urlpatterns = [
    path('api/', include(router.urls))
]