"""
URL configuration for WebCamping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#TODO ajouter proprement les views
from django.contrib import admin
from django.urls import path, include
from camping.views.camping_view import CampingViewSet
from camping.views.client_view import ClientViewSet
from camping.views.adresse_view import AdresseViewSet

from rest_framework.routers import DefaultRouter
from camping.views.gen_dashboard_emissions_group_view import EmmissionGroup
from camping.views.pie_chart import Pie_chart
from camping.views.distance_by_mean_of_transport_view import Distance_by_mean_of_transport
from camping.views.emission_by_mean_of_transport_view import Emissions_by_mean_of_transport
from camping.views.insert_new_value import Insert_value
from camping.views.login_view import LoginView

router = DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'camping', CampingViewSet)
router.register(r'adresse', AdresseViewSet)
urlpatterns = [
    path('secretadmin/',admin.site.urls),
    path('admin/', include("admin_honeypot.urls")),
    path('api/auth/token/', LoginView.as_view(), name='api_auth_token'),
    path('gen_em_group/', EmmissionGroup.as_view(), name="Emmission_group_per_year"),
    path('pie_chart/', Pie_chart.as_view(), name="Pie_chart"),
    path('distances_by_mean_of_transport/', Distance_by_mean_of_transport.as_view(), name="Distance_by_mean_of_transport"), 
    path('emissions_by_mean_of_transport/', Emissions_by_mean_of_transport.as_view(), name="Emission_by_mean_of_transport"),
    path('insert_value/', Insert_value.as_view(), name = "Insert_value"),
    path('login/', LoginView.as_view(), name='Login'),
    path('', include(router.urls))
]