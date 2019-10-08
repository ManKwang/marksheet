from main.forms import SignUpForm, SignInForm
from django.views.generic import View
from django.shortcuts import render, redirect
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class SignUp(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard_index_url')

        year = datetime.datetime.now().year
        form = SignUpForm()

        return render(request, 'main/sign-up.html', context={'form': form, 'current_year': year})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard_index_url')

        year = datetime.datetime.now().year
        bound_form = SignUpForm(request.POST)

        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect('dashboard_index_url')
        else:
            return render(request, 'main/sign-up.html', context={'form': bound_form, 'current_year': year})


class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard_index_url')

        year = datetime.datetime.now().year
        form = SignInForm()

        return render(request, 'main/sign-in.html', context={'form': form, 'current_year': year})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard_index_url')

        year = datetime.datetime.now().year
        bound_form = SignInForm(request.POST)

        if bound_form.is_valid():
            email = bound_form.cleaned_data['email']
            password = bound_form.cleaned_data['password']

            user = authenticate(username=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard_index_url')
                else:
                    bound_form.add_error('email', 'Акаунт вимкнено! Авторизація неможлива.')
                    return render(request, 'main/sign-in.html', context={'form': bound_form, 'current_year': year})
            else:
                bound_form.add_error('email', 'Неправильно введені дані.')
                return render(request, 'main/sign-in.html', context={'form': bound_form, 'current_year': year})

        else:
            return render(request, 'main/sign-in.html', context={'form': bound_form, 'current_year': year})


@login_required(login_url='signin_page_url')
def signOut(request):
    logout(request)
    return redirect('index_page_url')
