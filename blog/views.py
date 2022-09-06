from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import requests


# Create your views here.

#07ec3b32
#0369d3ccf3729ac58c7c0e9fe235f5aa	





def index(request):
    query="creme brulee"
    response= requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query+"&app_id=07ec3b32&app_key=0369d3ccf3729ac58c7c0e9fe235f5aa%09")
    jsonResponse= response.json()
    recipes= jsonResponse['hits']
    # print(json.dumps(jsonResponse, indent=4, sort_keys=True))
    return render(request, 'blog/index.html', {'recipes': recipes})

def specific(request):
    
    return HttpResponse("This is the specific url")


def search(request):
    if request.method== "POST":
       userText= request.POST.get('userText')
       response= requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+userText+"&app_id=07ec3b32&app_key=0369d3ccf3729ac58c7c0e9fe235f5aa%09")
       jsonResponse= response.json()
       recipes= jsonResponse['hits']
   
       return render(request, 'blog/index.html', {'recipes': recipes})
    else:
        return render(request, "blog/index.html")


# def single_meal(meal_id):
#     response = requests.get("http://www.themealdb.com/api/json/v1/1/lookup.php?i="+str(meal_id))
#     meals = response.json()
#     return render_template("single_meal.html", meals=meals)




def about(request):
    response= requests.get("https://api.edamam.com/api/recipes/v2?type=public&app_id=07ec3b32&app_key=0369d3ccf3729ac58c7c0e9fe235f5aa%09")
    jsonResponse= response.json()
    recipes= jsonResponse['hits']

    return render(request, 'blog/about.html', {'recipe_count': len(recipes)})



def contact(request):
    return render(request, 'blog/contact.html')


