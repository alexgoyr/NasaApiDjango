from django.shortcuts import render
from django.views.generic import TemplateView
from NasaApp.services import get_asteroids
from NasaApp.forms import searchAsteroids

def home(request):
    form = searchAsteroids()
    return render(request, "home.html", {"form": form})

#class asteroidList(ListView):
#    model = [["a", "zqeat"], ["b", "azetazet"]]


class asteroidList(TemplateView):
    template_name = 'asteroid_list.html'
    def get_context_data(self):
        startDate = self.request.GET.get('start', None)
        endDate = self.request.GET.get('end', None)
        print(startDate, endDate)
        context = {
            'asteroids' : get_asteroids(),
        }
        return context