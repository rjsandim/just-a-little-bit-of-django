from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):

    name = "Rafael"
    languages = ['python', 'php', 'ruby', 'java']

    context = {
        'name': name,
        'languages': languages
    }

    return render(request, 'blog/home.html', context)
