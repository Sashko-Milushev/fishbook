from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from fishbook.core.decorators import profile_required, lake_owner_required
from fishbook.lakes.forms import PrivateLakeCreationForm
from fishbook.lakes.models import PrivateLake, PublicLake


class LakesListView(views.ListView):
    template_name = 'lakes/show-all-lakes.html'
    model = PublicLake
    context_object_name = 'public_lakes'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        private_lakes = PrivateLake.objects.all()

        context['private_lakes'] = private_lakes

        return context


decorators = [profile_required, lake_owner_required]


class LakeDetailsView(views.DetailView):
    model = PublicLake
    template_name = 'lakes/lake-details-page.html'


@method_decorator(decorators, name='dispatch')
class PrivateLakeCreateView(views.CreateView):
    template_name = 'lakes/create-private-lake-page.html'
    form_class = PrivateLakeCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PrivateLakeCreateView, self).form_valid(form)


class PublicLakeCreateView(views.CreateView):
    template_name = 'lakes/create-public-lake-page.html'