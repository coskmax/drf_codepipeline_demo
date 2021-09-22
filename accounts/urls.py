from django.urls import path

from .views import (
	HealthCheckAPIView,
	HelloAPIView,
)

urlpatterns = [
	path('health/', HealthCheckAPIView.as_view()),
	path('hello/', HelloAPIView.as_view()),
]