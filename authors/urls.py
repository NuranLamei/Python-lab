from django.urls import path
from . import views
urlpatterns = [ 
                path('<str:value>',name="auth_details",view=views.authdetails),
]