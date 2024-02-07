from django.shortcuts import render # pour la reponce en html
from django.http import HttpResponse # pour la reponse en httpresponse
from django.http import JsonResponse
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
# cette fonction fait reference a ce qui doit etre afficher au sein d elle ok 
def say_hello(request): 
#la nature de reponce envoyer
    return render(request ,'hello.html')

# Django view example to retrieve temperature data from MongoDB Atlas



def get_temperature_data(request):
    # Replace the following with your MongoDB connection details
    client = MongoClient('mongodb+srv://hiba99:marwa2020@cluster0.ji3zoyq.mongodb.net/dht11?retryWrites=true&w=majority')
    db = client['dht11']
    collection = db['obs']
    
    # Retrieving the last 6 data points for the example
     # Replace 'your_streamname_id' with the ObjectId from your image
    streamname_id = ObjectId('65afebfa3a22637b465ed298')

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
