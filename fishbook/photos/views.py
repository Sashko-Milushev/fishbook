from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from fishbook.photos.forms import PhotoCreateForm
from fishbook.photos.models import Photo


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'photos/add-photo-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    context = {
        'photo': photo,
        'is_owner': photo.user == request.user,
    }

    return render(request, 'photos/details-photo-page.html', context)

def edit_photo(request, pk):
    pass