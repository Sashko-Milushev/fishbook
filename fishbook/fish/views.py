from django.views import generic as views
from fishbook.fish.models import Fish


class FishView(views.ListView):
    model = Fish
    template_name = 'fish/fish-catalogue-page.html'
    paginate_by = 3
    ordering = 'name'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class FishDetailsView(views.DetailView):
    model = Fish
    template_name = 'fish/fish-details-page.html'
