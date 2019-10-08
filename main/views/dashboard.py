from main.models import Code
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='signin_page_url')
def dashboardIndex(request):
    try:
        code = Code.objects.get(assigned_to=request.user)
    except Code.DoesNotExist:
        code = None

    return render(request, 'main/dashboard.html', {'code': code})
