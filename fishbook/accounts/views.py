from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_view, login, get_user_model, update_session_auth_hash
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponseRedirect

from fishbook.accounts.forms import SignUpForm, ProfileCreateForm, ProfileEditForm, UserEditForm, PasswordChangeForm
from fishbook.accounts.models import Profile, AppUser

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

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('home')


class UserEditView(views.UpdateView):
    template_name = 'accounts/user/edit-user-page.html'
    model = UserModel
    form_class = UserEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['user_pk'] = self.request.user.pk

        return context

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


def change_password(request, pk):
    user = get_user_by_id(pk)
    if request.method == "GET":
        form = PasswordChangeForm(user=request.user)
    else:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('change password done')
    context = {
        'form': form,
        'user': user,

    }

    return render(request, 'accounts/user/password-change-page.html', context)


class PasswordChangeSuccessful(views.TemplateView):
    template_name = 'accounts/user/password-change-done-page.html'


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


@login_required
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


def get_user_by_id(pk):
    return AppUser.objects.filter(pk=pk).get()


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
