from django.urls import path, include

from fishbook.lakes.views import PrivateLakeCreateView, LakesListView, LakeDetailsView

urlpatterns = (
    path('', LakesListView.as_view(), name='list lakes'),
    path('create/', PrivateLakeCreateView.as_view(), name='create lake'),
    path('<int:pk>/', include([
        path('', LakeDetailsView.as_view(), name='details lake')
    ]))
)