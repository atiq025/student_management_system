from django.urls import path
from student.views import StudentListView, StudentAddView, StudentUpdateView, StudentDeleteView, StudentDetailView

urlpatterns = [
    path('home/', StudentListView.as_view(), name='home'),
    path('student-add/', StudentAddView.as_view(), name='student-add'),
    path('student-update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student-delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

]