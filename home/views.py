from django.shortcuts import render

# Create your views here.
from home.models import Education, WorkExperience


def home(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html')


def homeCS(request):
    # Generate counts of some of the main objects
    education_entries = Education.objects.all()
    work_entries = WorkExperience.objects.all()

    context = {
        'work_index': 0,
        'education_entries': education_entries,
        'work_entries': work_entries,
    }

    return render(request, 'cs-home.html', context=context)


def homeMusic(request):
    return render(request, 'music-home.html', )
