from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views import generic as views

from fishbook.common.forms import PhotoCommentForm
from fishbook.common.models import PhotoLike
from fishbook.common.utils import get_photo_url
from fishbook.core.decorators import profile_required
from fishbook.core.utils import apply_likes_count, apply_user_liked_photo
from fishbook.photos.models import Photo


class HomeView(views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        photos = Photo.objects.all()
        user = self.request.user
        photos = [apply_likes_count(photo) for photo in photos]
        photos = [apply_user_liked_photo(photo, user) for photo in photos]
        context['photos'] = photos
        context['comment_form'] = PhotoCommentForm()

        return context


@login_required
@profile_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects.filter(photo_id=photo_id, user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(photo_id=photo_id, user_id=request.user.pk)

    return redirect(get_photo_url(request, photo_id))


@login_required
@profile_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()

    return redirect('home')
