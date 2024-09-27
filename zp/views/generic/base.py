from django.views.generic.base import TemplateView as Tv
from django.contrib.auth.mixins import LoginRequiredMixin


class TemplateView(LoginRequiredMixin, Tv):
    pass
