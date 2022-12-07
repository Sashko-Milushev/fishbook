from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from fishbook.photos.forms import PhotoCreateForm


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
