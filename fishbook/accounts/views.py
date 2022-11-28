from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_view, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from fishbook.accounts.forms import SignUpForm, ProfileCreateForm, ProfileEditForm
from fishbook.accounts.models import Profile

UserModel = get_user_model()


class SignInView(auth_view.LoginView):
    template_name = 'accounts/user/login-user-page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return self.get_redirect_url() or self.get_default_redirect_url()


class SignUpView(views.CreateView):
    template_name = 'accounts/user/register-user-page.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)

        return response


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('home')


class UserEditView(views.UpdateView):
    template_name = 'accounts/user/edit-user-page.html'
    model = UserModel
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user/delete-user-page.html'
    model = UserModel
    success_url = reverse_lazy('home')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/user/details-user-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        return context


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()

            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'accounts/profile/create-profile-page.html', context)


def get_profile_by_id(pk):
    return Profile.objects.filter(pk=pk).get()


def details_profile(request, pk):
    profile = get_profile_by_id(pk)

    context = {
        'profile': profile,
    }

    return render(request, 'accounts/profile/details-profile-page.html', context)


def edit_profile(request, pk):
    profile = get_profile_by_id(pk)
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save()

            return redirect('home')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'accounts/profile/edit-profile-page.html', context)