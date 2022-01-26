from django.views.generic import FormView
from django.urls import reverse_lazy
from post.forms import UserForm


class MyFormView(FormView):
    success_url = reverse_lazy("home")
    template_name = "home.html"
    form_class = UserForm
