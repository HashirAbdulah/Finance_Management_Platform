from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.dashboard_overview, name='dashboard_overview'),
    path('dashboard_view/', views.dashboard_view, name='dashboard_view'),
]
