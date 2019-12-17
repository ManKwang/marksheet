from main.models import Code, Classes, Students
from django.shortcuts import render, redirect
from django.views.generic import View
from main.forms import AddStudentForm


class AddStudent(View):
    def get(self, request, c_id):
        if not request.user.is_authenticated:
            return redirect('signin_page_url')

        try:
            code = Code.objects.get(assigned_to=request.user)

            if code.is_past_due:
                return redirect('classes_index_url')
        except Code.DoesNotExist:
            return redirect('classes_index_url')

        try:
            class_ = Classes.objects.get(pk=c_id)

            if class_.created_by != request.user:
                return redirect('classes_index_url')

        except class_.DoesNotExist:
            return redirect('classes_index_url')

        form = AddStudentForm()

        return render(request, 'main/students/add.html', context={'c_id': c_id, 'form': form})

    def post(self, request, c_id):
        if not request.user.is_authenticated:
            return redirect('signin_page_url')

        try:
            code = Code.objects.get(assigned_to=request.user)

            if code.is_past_due:
                return redirect('classes_index_url')
        except Code.DoesNotExist:
            return redirect('classes_index_url')

        try:
            class_ = Classes.objects.get(pk=c_id)

            if class_.created_by != request.user:
                return redirect('classes_index_url')

        except class_.DoesNotExist:
            return redirect('classes_index_url')

        form = AddStudentForm(request.POST)

        print('--------------------')
        print(request.POST)
        print('--------------------')

        if form.is_valid():
            student = Students()
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.third_name = form.cleaned_data['third_name']
            student.assigned_class = class_
            student.passport_lot = form.cleaned_data['passport_lot']
            student.passport_number = form.cleaned_data['passport_number']
            student.gender = form.cleaned_data['gender']

            student.save()

            return redirect('add_student_url', c_id=c_id)

        return render(request, 'main/students/add.html', context={'c_id': c_id, 'form': form})
