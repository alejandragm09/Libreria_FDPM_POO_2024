from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from .forms import LibroForm

class LibroListView(ListView):
    model = Libro
    template_name = 'libros/libro_list.html'
    context_object_name = 'libros'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libros/libro_detail.html'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libros:libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libros:libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libros/libro_confirm_delete.html'
    success_url = reverse_lazy('libros:libro_list')