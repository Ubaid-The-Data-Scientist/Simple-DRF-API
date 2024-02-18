from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/<int:pk>", views.student_info),
    path("studentapi/", views.student_list),
]
