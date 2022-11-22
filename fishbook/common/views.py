from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'common/home-page.html'

