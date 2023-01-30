from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from django.urls import reverse
from .forms import PetitionForm
from .models import Petition


class PetitionCreateView(LoginRequiredMixin, CreateView):
    form_class = PetitionForm
    model = Petition

    def get_success_url(self):
        return reverse('petition_app:petitions-list')


class PetitionUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = PetitionForm
    model = Petition
    
    def has_permission(self):
        petition = Petition.objects.get(pk=self.kwargs.get('pk'))
        return self.request.user == petition.user_created

    def get_success_url(self):
        return reverse('petition_app:petitions-detail', kwargs={'pk': self.kwargs.get('pk')})


class PetitionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Petition
    
    def has_permission(self):
        petition = Petition.objects.get(pk=self.kwargs.get('pk'))
        return self.request.user == petition.user_created

    def get_success_url(self):
        return reverse('petition_app:petitions-list')


class PetitionDetailView(LoginRequiredMixin, DetailView):
    model = Petition


class PetitionListView(LoginRequiredMixin, ListView):
    model = Petition


class SignPetitionView(LoginRequiredMixin, TemplateView):
    template_name = 'petition_app\petition_sign.html'

    def post(self, request, pk):
        petition = get_object_or_404(Petition, pk=pk)
        self.object = petition
        petition.user_signed.add(request.user)

    def get_context_data(self, **kwargs):
        context = super(SignPetitionView, self).get_context_data(**kwargs)
        petition = get_object_or_404(Petition, pk=kwargs.get('pk'))
        context['petition'] = petition
        return context

    def get_success_url(self):
        return reverse('petition_app:petitions-list')
