from django.urls import path
from .views import leads_page

app_name = "Leads"

urlpatterns = [
    path('', leads_page)
]