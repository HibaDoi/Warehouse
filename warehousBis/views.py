from django.shortcuts import render # pour la reponce en html
from django.http import HttpResponse # pour la reponse en httpresponse
from django.http import JsonResponse
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import geopandas as gpd
from geojson_rewind import rewind
# cette fonction fait reference a ce qui doit etre afficher au sein d elle ok 
def say_hello(request): 
#la nature de reponce envoyer
    return render(request ,'hello.html')
def get_temperature_data(request):
    # Replace the following with your MongoDB connection details
    client = MongoClient('mongodb+srv://hiba99:marwa2020@cluster0.ji3zoyq.mongodb.net/dht11?retryWrites=true&w=majority')
    db = client['dht11']
    collection = db['obs']
    
    # Retrieving the last 6 data points for the example
     # Replace 'your_streamname_id' with the ObjectId from your image
    streamname_id = ObjectId('65afebfa3a22637b465ed298')
    R1=ObjectId('65afed703a22637b465ed29c')
    R2=ObjectId('65afed983a22637b465ed29d')
    R3=ObjectId('65afedb33a22637b465ed29e')
    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    temperature_data_R1 = collection.find({'Streamname': streamname_id,'RoomID':R1}).sort('_id', 1)
    temperature_data_R2 = collection.find({'Streamname': streamname_id,'RoomID':R2}).sort('_id', 1)
    temperature_data_R3 = collection.find({'Streamname': streamname_id,'RoomID':R3}).sort('_id', 1)

    # Transforming the data into the format expected by Chart.js
    hh1 = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in temperature_data_R1]
    hh2 = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in temperature_data_R2]
    hh3 = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in temperature_data_R3]
    transformed_list1 = [[item[0] for item in hh1], [item[1] for item in hh1]]
    transformed_list2 = [[item[0] for item in hh2], [item[1] for item in hh2]]
    transformed_list3 = [[item[0] for item in hh3], [item[1] for item in hh3]]

    # temperatures = [data['Result'] for data in temperature_data]
   
    data = {
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'labels': transformed_list1[0],
        'datasets': [{
            'label': 'Temperature',
            'data': transformed_list1[1],
            # You can add more styling options here
        }],
       'labels2': transformed_list2[0],
        'datasets2': [{
            'label2': 'Temperature',
            'data_2': transformed_list2[1],
            # You can add more styling options here
        } ]     ,  
       'labels_3': transformed_list3[0],
        'datasets3': [{
            'label3': 'Temperature',
            'data3': transformed_list3[1],
            # You can add more styling options here
        } ]     ,         
        
    }
    
    return JsonResponse(data)
def get_humidity_data(request):
    # Replace the following with your MongoDB connection details
    client = MongoClient('mongodb+srv://hiba99:marwa2020@cluster0.ji3zoyq.mongodb.net/dht11?retryWrites=true&w=majority')
    db = client['dht11']
    collection = db['obs']
    
    # Retrieving the last 6 data points for the example
     # Replace 'your_streamname_id' with the ObjectId from your image
    streamname_id = ObjectId('65afec0c3a22637b465ed299')

    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    Humidity_data = collection.find({'Streamname': streamname_id}).sort('_id', 1)

    # Transforming the data into the format expected by Chart.js
    hh = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in Humidity_data]

    transformed_list = [[item[0] for item in hh], [item[1] for item in hh]]


    # temperatures = [data['Result'] for data in temperature_data]
   
    data = {
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'labels': transformed_list[0],
        'datasets': [{
            'label': 'Humidity',
            'data': transformed_list[1],
            # You can add more styling options here
        }]
    }
    
    return JsonResponse(data)
def get_fire_data(request):

    # Replace the following with your MongoDB connection details
    client = MongoClient('mongodb+srv://hiba99:marwa2020@cluster0.ji3zoyq.mongodb.net/dht11?retryWrites=true&w=majority')
    db = client['dht11']
    collection = db['obs']
    
    # Retrieving the last 6 data points for the example
     # Replace 'your_streamname_id' with the ObjectId from your image
    streamname_id = ObjectId('65afec3b3a22637b465ed29b')

    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    temperature_data = collection.find({'Streamname': streamname_id}).sort('_id', 1)

    # Transforming the data into the format expected by Chart.js
    hh = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result']])for data in temperature_data]
  
    transformed_list = [[item[0] for item in hh], [item[1] for item in hh]]


    # temperatures = [data['Result'] for data in temperature_data]
   
    data = {
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'labels': transformed_list[0],
        'datasets': [{
            'label': 'Temperature',
            'data': transformed_list[1],
            # You can add more styling options here
        }]
    }
    
    return JsonResponse(data)
def get_shelf_data(request):
    # Replace the following with your MongoDB connection details
    client = MongoClient('mongodb+srv://hiba99:marwa2020@cluster0.ji3zoyq.mongodb.net/dht11?retryWrites=true&w=majority')
    db = client['dht11']
    collection = db['obs']
    collection1 = db['thing_locations']  # Remplacez 'ma_collection' par le nom de votre collection
    collection2= db['things']

    # Charger les données GeoJSON depuis un fichier
    gdf= gpd.read_file('https://pydeck2.s3.eu-north-1.amazonaws.com/Shelf_uniquement.geojson')

    
    # geojson_data = json.load(f)
    streamname_id = ObjectId('65afec1c3a22637b465ed29a')
    R1=ObjectId('65afed703a22637b465ed29c')
    R2=ObjectId('65afed983a22637b465ed29d')
    R3=ObjectId('65afedb33a22637b465ed29e')
    motion_data_R1 = collection.find({'Streamname': streamname_id,'RoomID':R1}).sort('_id', -1).limit(1)
    motion_data_R2 = collection.find({'Streamname': streamname_id,'RoomID':R2}).sort('_id', -1).limit(1)
    motion_data_R3 = collection.find({'Streamname': streamname_id,'RoomID':R3}).sort('_id', -1).limit(1)
    motion_dd1 = [data['Result'] for data in motion_data_R1]
    motion_dd2 = [data['Result'] for data in motion_data_R2]
    motion_dd3 = [data['Result'] for data in motion_data_R3]
    motion_dd1 = motion_dd1[0][0]
    motion_dd2 = motion_dd2[0][0]
    motion_dd3 = motion_dd3[0][0]
    status=motion_dd1+motion_dd2+motion_dd3
    print(status)
    # gdf['rooms'] = np.repeat(['A', 'B', 'C'], [8, 8, 7])
    gdf['status'] = status
    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    marchandise= collection1.find().sort('_id', -1).limit(1)
    print(marchandise)
    marchandise = [da['id_thing'] for da in marchandise]
    room_merch= collection2.find({'_id':ObjectId(marchandise[0])}).sort('_id', -1).limit(1)
    room_merch = [data['Properties'] for data in room_merch]
    Room_stt=room_merch[0]['room']
    def color_polygons(row):
        if row['status'] == 1 and row['rooms'] == Room_stt :
            return '#0000FF'
        elif row['status'] == 1 and row['rooms'] != None:
            return '#32CD32'
        elif row['status'] == 0 and row['rooms'] != None:
            return '#FF0000'
        elif row['status'] == None:
            return '#000000'
        

    gdf['color'] = gdf.apply(color_polygons, axis=1)
    # ____________________________
    # Read your data into a GeoDataFrame (replace 'your_file.gdf' with your actual file name)
    #Convert the GeoDataFrame to GeoJSON
    geojson_data = gdf.to_json()
    output = rewind(geojson_data)
    # Return the GeoJSON response
    print(type(output))
    print(output)
    return JsonResponse(output, safe=False)
def get_infra(request):
    gdf2= gpd.read_file('https://pydeck2.s3.eu-north-1.amazonaws.com/contour_uniquement.geojson')
    geojson_data = gdf2.to_json()
    output = rewind(geojson_data)
    return JsonResponse(output, safe=False)