from django.urls import path

from fishbook.common.views import HomeView, like_photo, comment_photo

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo')
)