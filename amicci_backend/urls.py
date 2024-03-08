from django.urls import path, include

urlpatterns = [
    path('api/', include([
        path('briefings/', include('briefings.urls')),
        path('retailers/', include('retailers.urls')),
        path('categories/', include('categories.urls')),
        path('vendors/', include('vendors.urls')),
    ])),
]
