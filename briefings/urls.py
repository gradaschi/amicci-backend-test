from django.urls import path
from .views import BriefingList, BriefingDetail

urlpatterns = [
    path('', BriefingList.as_view(), name='briefing-list'),
    path('<int:id>/', BriefingDetail.as_view(), name='briefing-detail'),
]
