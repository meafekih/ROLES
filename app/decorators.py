# yourapp/decorators.py

from functools import wraps
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.userprofile.role == 'admin':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden('Permission denied')
    return _wrapped_view

def seller_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.userprofile.role == 'seller':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden('Permission denied')
    return _wrapped_view
