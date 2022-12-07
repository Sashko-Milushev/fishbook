from django.views import generic as views

from fishbook.photos.models import Photo


class HomeView(views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['photos'] = Photo.objects.all()

        return context

