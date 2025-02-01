from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student
from django.urls import reverse_lazy
from .forms import StudentModelForm 
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'
    paginate_by = 5
    ordering = ['name']

    def get_queryset(self):
        """Custom queryset to allow filtering or searching."""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', None)
        course_filter = self.request.GET.get('course', None)

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)  # Case-insensitive search
        if course_filter:
            queryset = queryset.filter(course=course_filter)  # Exact match for course

        return queryset

    def get_context_data(self, **kwargs):
        """Add additional context for filter options."""
        context = super().get_context_data(**kwargs)
        context['courses'] = Student.objects.values_list('course', flat=True).distinct()
        return context



class StudentAddView(SuccessMessageMixin, CreateView):
    model = Student 
    template_name = 'add_student.html'
    form_class = StudentModelForm	
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    success_message = "Student added successfully!"


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student 
    template_name = 'add_student.html'
    pk_url_kwarg = 'pk'
    form_class = StudentModelForm	
    context_object_name = 'form'
    success_message = "Student updated successfully!"
    
    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.pk})


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student 
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
    success_message = "Student deleted successfully!"


class StudentDetailView(DetailView):
    model = Student 
    template_name = 'details.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'student'



