from django.shortcuts import render

# Create your views here.
from home.models import Education, WorkExperience


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    education_entries = Education.objects.all()
    work_entries = WorkExperience.objects.all()


    context = {
        'education_entries': education_entries,
        'work_entries': work_entries,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)