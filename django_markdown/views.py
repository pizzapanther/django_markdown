""" Supports preview. """
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import settings

@csrf_exempt
def preview(request):
    """ Render preview page.

    :returns: A rendered preview

    """
    if settings.MARKDOWN_PROTECT_PREVIEW:
        user = getattr(request, 'user', None)
        if user and not user.is_staff:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())

    return render(
        request, settings.MARKDOWN_PREVIEW_TEMPLATE, dict(
            content=request.REQUEST.get('data', 'No content posted'),
            css=settings.STATIC_URL + settings.MARKDOWN_STYLE,
        ))
