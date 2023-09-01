from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileUserView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = "registration/profile.html"

class UpdateProfileUserView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("profile")
    template_name = "registration/user_change_form.html"

    def get_success_url(self):
        uid = self.kwargs['uuid']
        return reverse_lazy('users:profile', kwargs={'uuid': uid})
