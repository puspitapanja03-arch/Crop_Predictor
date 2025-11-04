from django.shortcuts import render
import pickle
from django.conf import settings
import os

model_path = os.path.join(settings.BASE_DIR, "dtc_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

def home(request):
    model_pred = None
    if request.method == "POST":
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        phlavel = float(request.POST['phlavel'])
        water = float(request.POST['water'])
        season = float(request.POST['season'])

        data = [[temperature,humidity,phlavel,water,season]]
        model_pred = model.predict(data)
    
    context = {
        "result" : model_pred
    }

    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")