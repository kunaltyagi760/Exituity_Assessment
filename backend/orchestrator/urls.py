from django.contrib import admin
from django.urls import path
from .views import RunValuationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/run-valuation/', RunValuationView.as_view(), name='run-valuation'),
]