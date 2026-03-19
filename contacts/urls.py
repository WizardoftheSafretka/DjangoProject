from django.urls import path, include
from contacts.apps import ContactsConfig
from contacts.views import ContactsView

app_name = ContactsConfig.name

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name="contacts"),
]