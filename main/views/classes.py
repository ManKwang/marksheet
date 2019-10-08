from main.models import Code, Classes
from django.shortcuts import render, redirect
from django.views.generic import View
from main.forms import CreateClassForm


class CreateClass(View):
    def get(self, request, code):
        if not request.user.is_authenticated:
            return redirect('signin_page_url')

        try:
            code = Code.objects.get(assigned_to=request.user)

            if code.amount <= 0 or code.is_past_due:
                return redirect('dashboard_index_url')
        except Code.DoesNotExist:
            return redirect('dashboard_index_url')

        form = CreateClassForm()

        return render(request, 'main/create_class.html', context={'form': form, 'code': code})

    def post(self, request, code):
        if not request.user.is_authenticated:
            return redirect('signin_page_url')

        bound_form = CreateClassForm(request.POST)

        if bound_form.is_valid():
            class_ = bound_form.save(code, request.user)

            return redirect('dashboard_index_url')
        else:
            return render(request, 'main/create_class.html', context={'form': bound_form, 'code': code})


class ClassesList(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signin_page_url')

        try:
            classes_list = Classes.objects.filter(created_by=request.user)
        except:
            classes_list = None

        return render(request, 'main/classes/index.html', context={'classes_list': classes_list})


class ClassView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signin_page_url')

        if not request.GET.get('c_id'):
            return redirect('classes_index_url')

        try:
            current_class = Classes.objects.get(pk=request.GET.get('c_id'))
        except current_class.DoesNotExist:
            current_class = False

        if not current_class or current_class.created_by != request.user:
            return redirect('classes_index_url')

        test_rows = [i for i in range(5)]

        return render(request, 'main/classes/view.html', context={'current_class': current_class, 'tr': test_rows})
