from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import ExtendUser


class UserCreateView(CreateView):
    template_name = 'users/register.html'
    model = ExtendUser
    form_class = UserForm
    success_url = reverse_lazy('post')
