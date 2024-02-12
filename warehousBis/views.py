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
import networkx as nx 
from shapely.geometry import Point, LineString
from math import sqrt
import json
from django.http import JsonResponse
gdfyy= gpd.read_file('https://pydeck2.s3.eu-north-1.amazonaws.com/CENTROIDS.geojson')
# cette fonction fait reference a ce qui doit etre afficher au sein d elle ok 
def say_hello(request): 
#la nature de reponce envoyer
    return render(request ,'me.html')
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
    temperature_data_R1 = collection.find({'Streamname': streamname_id,'RoomID':R1}).sort('_id', 1).limit(40)
    temperature_data_R2 = collection.find({'Streamname': streamname_id,'RoomID':R2}).sort('_id', 1).limit(40)
    temperature_data_R3 = collection.find({'Streamname': streamname_id,'RoomID':R3}).sort('_id', 1).limit(40)

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
            'data2': transformed_list2[1],
            # You can add more styling options here
        } ],  
       'labels3': transformed_list3[0],
        'datasets3': [{
            'label3': 'Temperature',
            'data3': transformed_list3[1],
            # You can add more styling options here
        } ],         
        
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
    R1=ObjectId('65afed703a22637b465ed29c')
    R2=ObjectId('65afed983a22637b465ed29d')
    R3=ObjectId('65afedb33a22637b465ed29e')
    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    Humidity_data_R1 = collection.find({'Streamname': streamname_id,'RoomID':R1}).sort('_id', 1).limit(40)
    Humidity_data_R2 = collection.find({'Streamname': streamname_id,'RoomID':R2}).sort('_id', 1).limit(40)
    Humidity_data_R3 = collection.find({'Streamname': streamname_id,'RoomID':R3}).sort('_id', 1).limit(40)
    # Transforming the data into the format expected by Chart.js
    hh = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in Humidity_data_R1]
    hh2 = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in Humidity_data_R2]
    hh3 = [([datetime.fromisoformat(data['PhenomenonTime']).strftime("%H:%M") ,data['Result'][0]])for data in Humidity_data_R3]
    transformed_list = [[item[0] for item in hh], [item[1] for item in hh]]
    transformed_list2 = [[item[0] for item in hh2], [item[1] for item in hh2]]
    transformed_list3 = [[item[0] for item in hh3], [item[1] for item in hh3]]

    # temperatures = [data['Result'] for data in temperature_data]
   
    data = {
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'labels': transformed_list[0],
        'datasets': [{
            'label': 'Humidity',
            'data': transformed_list[1],
            # You can add more styling options here
        }],
    
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'labels2': transformed_list2[0],
        'datasets2': [{
            'label2': 'Humidity',
            'data2': transformed_list2[1],
            # You can add more styling options here
        }],
    
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'labels3': transformed_list3[0],
        'datasets3': [{
            'label3': 'Humidity',
            'data3': transformed_list3[1],
            # You can add more styling options here
        }],
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
    
    # gdf['rooms'] = np.repeat(['A', 'B', 'C'], [8, 8, 7])
    gdf['status'] = gdfyy['status']
    print("had statut li bghina",gdf['status'].tolist())
    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    marchandise= collection1.find().sort('_id', -1).limit(1)
    
    marchandise = [da['id_thing'] for da in marchandise]
    room_merch= collection2.find({'_id':ObjectId(marchandise[0])}).sort('_id', -1).limit(1)
    room_merch = [data['Properties'] for data in room_merch]
    Room_stt=room_merch[0]['room']
    print('from mhm shelve nnnnnnnnnnnnnnnnnnnnnnn',Room_stt)
    def color_polygons(row):
        if row['status'] == 1 and row['rooms'] == Room_stt :
            return '#0000FF'
        elif row['status'] == 1 and row['rooms'] != Room_stt:
            return '#32CD32'
        elif row['status'] == 0 :
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

    return JsonResponse(output, safe=False)
def get_infra(request):

    gdf2= gpd.read_file('https://pydeck2.s3.eu-north-1.amazonaws.com/contour_uniquement.geojson')
    geojson_data = gdf2.to_json()
    output = rewind(geojson_data)
    return JsonResponse(output, safe=False)
def routing(request):
    
    client = MongoClient('mongodb+srv://hiba99:marwa2020@cluster0.ji3zoyq.mongodb.net/dht11?retryWrites=true&w=majority')
    db = client['dht11']
    collection = db['thing_locations']
    coll_loc=db['locations']
    coll_thing=db['things']
    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    last_thing = collection.find().sort('_id', -1).limit(1)
    # Transforming the data into the format expected by Chart.js
    obj_location_id = [(data['id_location'] ,data['id_thing'])for data in last_thing]

    obj_location_id=obj_location_id[0]

    obj_location_id,obj_thing_id =obj_location_id[0],obj_location_id[1]


    last_thing_loca = coll_loc.find({'Description': str(obj_location_id)})

    # Transforming the data into the format expected by Chart.js
    obj_location = [data['Location'] for data in last_thing_loca]
    obj_location =obj_location[0]['coordinates']
    #########################################
    # Retrieve the last 4 documents where 'streamname' matches 'streamname_id'
    obj_thing = coll_thing.find({'_id': ObjectId(obj_thing_id)})

    # Transforming the data into the format expected by Chart.js
    obj_thingy = [data['Properties']['room'] for data in obj_thing]
    obj_thingy=obj_thingy[0]
    obj_thingy=obj_thingy.split(' ')[1]
    print('location',obj_location)
    print('from location jjjjjjjjjjjjjjjjjjj',obj_thingy)

    def load_geojson_segments(file_path):
        """Load segments from a GeoJSON file."""
        gdf = gpd.read_file(file_path)
        if not gdf.empty:
            return gdf
        else:
            raise ValueError("GeoJSON file is empty or not valid.")

    def extract_start_end_points(gdf):
        """Extract start and end points from each LineString segment."""
        points_list = []
        for idx, row in gdf.iterrows():
            if isinstance(row.geometry, LineString):
                start_point = Point(row.geometry.coords[0])
                end_point = Point(row.geometry.coords[-1])
                points_list.append((start_point, end_point))
            else:
                print(f"Row {idx} is not a LineString.")
        return points_list

    def calc_distance(point1, point2):
        """Calculate distance between two points."""
        return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    # Load the segments from the GeoJSON file
    segments_gdf = load_geojson_segments('https://pydeck2.s3.eu-north-1.amazonaws.com/ROUTINGF.geojson')

    # Extract start and end points
    points_list = extract_start_end_points(segments_gdf)

    # Create a directed graph
    G = nx.DiGraph()

    # Add edges to the graph along with their weights (distances)
    for start, end in points_list:
        distance = calc_distance((start.y, start.x), (end.y, end.x))
        G.add_edge((start.y, start.x), (end.y, end.x), weight=distance)
        G.add_edge((end.y, end.x), (start.y, start.x), weight=distance)  # If the paths are bidirectional

    shortest_paths = []  # Store all shortest paths to different end points
    min_distance = float('inf')  # Initialize with a very large value
    closest_shortest_path = None  # Initialize closest_shortest_path outside the loop
    
    
    
    # Read the GeoJSON file
    
    data1 = gdfyy.to_json()
   
    data = json.loads(data1)
    # Filter points with status = 1 and rooms = given room
    filtered_features = [feature for feature in data["features"] if feature["properties"]["status" ]== 1 and feature["properties"]["rooms"] == obj_thingy]

    # Extract shelves information from filtered features
    shelves = []
    for feature in filtered_features:
        shelves.append({
            'label': feature['properties']['id'],
            'coordinates': {
                'x': feature['geometry']['coordinates'][1],
                'y': feature['geometry']['coordinates'][0],
            }
        })

    coordinates_list = [(feature["coordinates"]["x"], feature["coordinates"]["y"]) for feature in shelves]  # Populate coordinates_list here
    
      # Initialize an empty list to store shelf IDs
    ID=999
    for end_point in coordinates_list:
        start_point = obj_location
        # Find the nearest points in the graph to the provided start and end points
        start_node = min(G.nodes(), key=lambda x: calc_distance(x, start_point))
        end_node = min(G.nodes(), key=lambda x: calc_distance(x, end_point))

        # Check if start and end nodes are within the range of the road network
        if start_node not in G or end_node not in G:
            print("Start or end point is not within the road network.")
        else:
            # Find the shortest path using Dijkstra's algorithm
            try:
                shortest_path = nx.dijkstra_path(G, source=start_node, target=end_node, weight='weight')
                shortest_paths.append(shortest_path)
                distance_to_end_point = sum(calc_distance(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1))
                if distance_to_end_point < min_distance:
                    min_distance = distance_to_end_point
                    closest_shortest_path = shortest_path

                    # Extract the shelf ID associated with the end point
                    shelf_id = [feature["properties"]["id"] for feature in filtered_features if 
                                (feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]) == end_point]
                    
                    ID = shelf_id[0]
                      # Append the shelf ID to the ID list
                    print("yes i exist")
            except nx.NetworkXNoPath:
                print("No",end_point ,obj_location)
            
            

            
    # Return both closest_shortest_path and ID as a JSON response
    print("le status des shelf ",(gdfyy['status']).tolist().count(0))
    if ID !=999:

        gdfyy.at[ID-1, 'status'] = 0
        print("id ocupeeeeeeeeeeeee",ID )
    else: 
        print("matbadaaaaaal walo a zaft ")    
    print("333333333333333333333333333333333333333333333333333333333333333333 ") 
    #print(gdfyy["status"])
    
    return JsonResponse(closest_shortest_path,safe=False)



def empty_shelf(request):
    x=gdfyy['status'].tolist()[:12].count(1)
    y=gdfyy['status'].tolist()[12:23].count(1)
    z=gdfyy['status'].tolist()[23:].count(1)
    data= {
        # 'labels': ["9AM", "10AM", "11AM", "12PM"],
       'r1': x,
        'r2': y,
       'r3': z,    
    }
    return JsonResponse(data)
