from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
# Create your views here.

def hello(request) :
    bands = Band.objects.all()
    return HttpResponse(f"""<h1>My web page <h1/>
                        <p>Ma liste de preféres</p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                        </ul>
                        """)

def about(request) :
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")

def listing(request) :
    return HttpResponse("la page de lising")