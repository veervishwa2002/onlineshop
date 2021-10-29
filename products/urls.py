from django.urls import path
from . import views

#
# /products/1/detail
# /product/new

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]