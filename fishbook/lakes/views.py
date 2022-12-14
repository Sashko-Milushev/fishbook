from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from fishbook.core.decorators import profile_required, lake_owner_required
from fishbook.lakes.forms import PrivateLakeCreationForm, PublicLakeCreateForm, PrivateLakeEditForm
from fishbook.lakes.models import PrivateLake, PublicLake


class PublicLakesListView(views.ListView):
    template_name = 'lakes/show-public-lakes.html'
    model = PublicLake
    context_object_name = 'public_lakes'
    paginate_by = 3

class PrivateLakesListView(views.ListView):
    template_name = 'lakes/show-private-lakes.html'
    model = PrivateLake
    context_object_name = 'private_lakes'
    paginate_by = 3

    # def get_lakes_page(self):
    #     return self.request.GET.get('page', 1)
    #
    # def get_paginated_lakes(self):
    #     page = self.get_lakes_page()
    #     private_lakes = PrivateLake.objects.order_by('name').all()
    #     paginator = Paginator(private_lakes, self.paginate_by)
    #     return paginator.get_page(page)
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #
    #     context['private_lakes'] = self.get_paginated_lakes()
    #
    #     return context


class PrivateLakeDetailsView(views.DetailView):
    model = PrivateLake
    template_name = 'lakes/private-lake-details-page.html'


decorators = [profile_required, lake_owner_required]


@method_decorator(decorators, name='dispatch')
class PrivateLakeCreateView(views.CreateView):
    template_name = 'lakes/create-private-lake-page.html'
    form_class = PrivateLakeCreationForm
    success_url = reverse_lazy('list lakes')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PrivateLakeCreateView, self).form_valid(form)


class PrivateLakeEditView(views.UpdateView):
    template_name = 'lakes/edit-private-lake-page.html'
    form_class = PrivateLakeEditForm
    success_url = reverse_lazy('list lakes')


class PublicLakeDetailsView(views.DetailView):
    model = PublicLake
    template_name = 'lakes/public-lake-details-page.html'


class PublicLakeCreateView(views.CreateView):
    template_name = 'lakes/create-public-lake-page.html'
    form_class = PublicLakeCreateForm
    success_url = reverse_lazy('list lakes')
