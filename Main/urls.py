from . import views
from django.urls import path

urlpatterns = [
    path('show/<int:id>', views.get_data,name="Data"),
]