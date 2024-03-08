from django.urls import path
from .views import RetailerList, RetailerDetail

urlpatterns = [
    path('', RetailerList.as_view(), name='retailers-list'),
    path('<int:id>/', RetailerDetail.as_view(), name='retailers-detail'),
]
