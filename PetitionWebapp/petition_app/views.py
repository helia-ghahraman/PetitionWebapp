import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  View, UpdateView)

from django.urls import reverse
from .forms import PetitionForm
from .models import Petition
from .filters import PetitionFilter


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
    paginate_by = 10
    filterset_class = PetitionFilter

    def get_context_data(self, **kwargs):
        context = super(PetitionListView, self).get_context_data(**kwargs)
        filterset = PetitionFilter(
            self.request.GET, queryset=self.get_queryset().order_by('id'))
        context['filterset'] = filterset
        return context


class SignPetitionView(LoginRequiredMixin, View):
    def post(self, request, pk):
        petition = get_object_or_404(Petition, pk=pk)
        self.object = petition
        if petition.end_datetime > datetime.now():
            petition.user_signed.add(request.user)
            petition.user_signed_count += 1
            petition.save()
            return Response({'data': petition},
                status=status.HTTP_200_OK)
        else:
            return Response({'message': 'This petition has been ended.'},
                status=status.HTTP_400_BAD_REQUEST)

    def get_context_data(self, **kwargs):
        context = super(SignPetitionView, self).get_context_data(**kwargs)
        petition = get_object_or_404(Petition, pk=kwargs.get('pk'))
        context['petition'] = petition
        return context

    def get_success_url(self):
        return reverse('petition_app:petitions-list')
