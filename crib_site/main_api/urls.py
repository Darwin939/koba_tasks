from django.urls import path
from .views import CribList , CribDetail

urlpatterns = [
    path('', CribList.as_view()),
    path('<int:pk>', CribDetail.as_view())
]