from django.contrib.auth.views import password_reset
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def admin_password_reset(request, *args, **kwargs):
    return password_reset(request, *args, **kwargs)
