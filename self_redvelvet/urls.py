from django.urls import path
from self_redvelvet import views

app_name = 'self_redvelvet'

urlpatterns = [
    path('joy/', views.joy, name='joy'),
    path('seulgi/', views.seulgi, name='seulgi'),
]