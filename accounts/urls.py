from django.urls import path
from . import views

# name of my app
app_name = 'accounts'

urlpatterns = [
    # name=" " the name will called in (Html) files
    path('signup', views.signup, name='signup'),
]