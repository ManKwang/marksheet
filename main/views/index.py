from django.shortcuts import render, redirect
from django.views.generic import View


class IndexPage(View):
    def get(self, request):
        return render(request, 'main/index.html')
