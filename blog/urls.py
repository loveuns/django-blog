from django.urls import path
from .views import list, detail

app_name = 'post'
urlpatterns = [
    path('', list, name='list'),
    path('post/<int:pk>/', detail, name='detail'),
]
