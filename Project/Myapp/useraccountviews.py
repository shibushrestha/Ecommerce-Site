from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import UpdateView

# This view is for user profile
@login_required
def user_profile(request, user_username):
    user = get_object_or_404(User, username = user_username)
    context = {'user':user}
    return render(request, 'Myapp/useraccount.html', context)
    

# This view is for the password change view.
class UserPasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'Myapp/change-password.html'
    success_url = '/Myapp/login/'


class EditUserProfile(UpdateView):
    template_name = 'Myapp/edit-profile.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = User.objects.get(pk = self.id)
        return queryset
        