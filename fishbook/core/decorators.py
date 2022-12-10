import functools

from django.shortcuts import redirect


def profile_required(view_func):
    functools.wraps(view_func)

    def wrapper(request, *args, **kwargs):
        profile = request.user.profile
        if not profile.is_completed:
            return redirect('create profile')

        return view_func(*args, **kwargs)

    return wrapper
