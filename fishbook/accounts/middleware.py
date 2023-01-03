from django.shortcuts import redirect
from django.urls import reverse_lazy


def check_profile_completion(get_response):
    def middleware(request, *args, **kwargs):

        response = get_response(request, *args, **kwargs)

        if request.user.is_anonymous:
            return response
        profile = request.user.profile

        if profile.profile_type is not None and profile.profile_picture.name != '' \
                and profile.username is not None and profile.fishing_style != []:
            profile.is_completed = True
            profile.save()

        return response

    return middleware
