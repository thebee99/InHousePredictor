from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.submit, name='submit'),
    
    path('prediction/', views.prediction_view, name='prediction'),
    # path('result/', views.result_view, name='result'),
]

