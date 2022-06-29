from app import app
import json
import os
from flask import render_template, redirect, url_for, request
from app.models.location import Location

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods=["POST", "GET"])
def extract():
    if request.method == "POST":
        location_name = request.form.get("location_name").replace(' ', '').lower()
        product = Location(location_name)
        product.extract_days()

        return redirect(url_for('location', location_name=location_name))

    return render_template("extract.html.jinja")

@app.route('/locations')
def locations():
    locations = os.listdir('app/locations')

    return render_template("locations.html.jinja", locations = locations)

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/location/<location_name>')
def location(location_name):
    location = Location(location_name)

    all_days = []
    
    file_names = os.listdir(f'app/locations/{location_name}/')
    file_names.sort(key=lambda x: os.path.getmtime(f'app/locations/{location_name}/{x}'))  #Sorotwanie plików po ostatniej modyfikacji
    
    for file_name in file_names:
        with open(f'app/locations/{location_name}/{file_name}') as file:
            all_days.append([file_name.split('.')[0], json.load(file)])

    return render_template("location.html.jinja", location_name = location_name, all_days = all_days)