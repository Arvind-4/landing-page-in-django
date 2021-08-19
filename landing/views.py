from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm
from .models import Register

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': RegisterForm()
        }
        return render(request, 'home_view.html', context=context)
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data.get('email')
            email_qs = Register.objects.all().filter(email=new_email)
            if not email_qs.exists():
                obj, created = Register.objects.get_or_create(email=new_email)
                if created:
                    information = 'Hola! Will Get to You as Soon as Possible!'
                    messages.success(request, information)
                    return redirect('/')
            information = 'Error! You have Already Filled!'
            messages.error(request, information)
            return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'home_view.html', context=context)