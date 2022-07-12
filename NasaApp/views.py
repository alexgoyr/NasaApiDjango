from django.shortcuts import render
from django.views.generic import TemplateView
from NasaApp.services import get_asteroids, get_asteroidDetails
from NasaApp.forms import searchAsteroids

def home(request):
    form = searchAsteroids()
    return render(request, "home.html", {"form": form})

class asteroidList(TemplateView):
    template_name = 'asteroid_list.html'
    def get_context_data(self):
        startDate = self.request.GET.get('start', None)
        endDate = self.request.GET.get('end', None)
        asteroids = get_asteroids(startDate, endDate)
        context = {
            'asteroids' : asteroids,
        }
        return context

class asteroidDetails(TemplateView):
    template_name = 'details.html'
    def get_context_data(self):
        id = self.request.GET.get('id', None)
        previousCloseApproach = get_asteroidDetails(id)
        context = {
            'previousCloseApproach' : previousCloseApproach,
        }
        return context