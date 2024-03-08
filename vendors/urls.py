from django.urls import path
from .views import VendorList, VendorDetail

urlpatterns = [
    path('', VendorList.as_view(), name='retailers-list'),
    path('<int:id>/', VendorDetail.as_view(), name='retailers-detail'),
]
