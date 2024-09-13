from django.urls import path
from . import views

urlpatterns = [
    path('form/<int:form_id>/', views.form_data, name='form_data')
]