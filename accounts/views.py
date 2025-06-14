from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomLoginForm, CustomRegisterForm
from home.models import About


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = CustomLoginForm

    def form_valid(self, form):
        messages.success(self.request, "با موفقیت وارد شدید!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context


def register_view(request):
    about = About.objects.first()

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ثبت نام با موفقیت انجام شد!")
            return redirect('home:home')
    else:
        form = CustomRegisterForm()

    return render(request, 'account/register.html', {
        'form': form,
        'about': about
    })


def logout_view(request):
    logout(request)
    return redirect('home:home')
