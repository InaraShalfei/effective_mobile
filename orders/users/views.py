from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    """
        Registration of a new user
    """
    form_class = CreationForm
    success_url = reverse_lazy('orders:index')
    template_name = 'users/signup.html'
