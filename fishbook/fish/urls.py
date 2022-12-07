from django.urls import path

from fishbook.fish.views import FishView, FishDetailsView

urlpatterns = (
    path('', FishView.as_view(), name='fish catalogue'),
    path('<int:pk>/', FishDetailsView.as_view(), name='fish details'),
)