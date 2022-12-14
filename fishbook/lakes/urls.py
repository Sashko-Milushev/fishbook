from django.urls import path, include

from fishbook.lakes.views import PrivateLakeCreateView, PrivateLakeEditView, PublicLakeCreateView, \
    PublicLakeDetailsView, PrivateLakeDetailsView, PublicLakesListView, PrivateLakesListView

urlpatterns = (
    path('private/', include([
        path('', PublicLakesListView.as_view(), name='list public lakes'),
        path('create/', PrivateLakeCreateView.as_view(), name='create private lake'),
        path('<int:pk>/', include([
            path('', PrivateLakeDetailsView.as_view(), name='details private lake'),
            path('edit/', PrivateLakeEditView.as_view(), name='edit private lake'),
        ]))
    ])),
    path('public/', include([
        path('', PrivateLakesListView.as_view(), name='list private lakes'),
        path('create/', PublicLakeCreateView.as_view(), name='create public lake'),
        path('<int:pk>/', PublicLakeDetailsView.as_view(), name='details public lake'),
        ])),

)
