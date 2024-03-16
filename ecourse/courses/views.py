from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Category
# Create your views here.

class CategoryView(View):

    def get(self, request):
        cats = Category.objects.all()
        return render(request, 'list.html', {
            'categories': cats
        })

    def post(self, request):
        pass
def index(request):
    return HttpResponse('Hello CS')

def list(request, course_id):
    return HttpResponse(f'Course {course_id}')