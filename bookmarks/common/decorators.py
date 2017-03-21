from django.http import HttpResponseBadRequest

def ajax_required(f):
    """
    Custom decorator for Ajax views,
    It defines a wrap function that returns
    an HTttpResponseBadRequest object(HTTP 400 code) if
    the request in not AJAX. Otherwise, it returns the
    decorator function.
    """
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap
