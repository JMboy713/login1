from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login),   #users/path 이런식으로 저장
    path('login/<int:id>/', views.login_detail,name='login-detail')
]