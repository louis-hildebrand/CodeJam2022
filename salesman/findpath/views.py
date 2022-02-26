from django.http import HttpResponse
import json
from rest_framework.decorators import api_view

from findpath.findpath import calculate_route

@api_view(['POST'])
def find_path(request):
    """
    [
        {
            "input_trip_id": 101,
            "start_latitude": 27.961307,
            "start_longitude": -82.4493,
            "start_time": "2022-02-04 08:00:00",
            "max_destination_time": "2022-02-06 15:00:00"
        },
        {
            "input_trip_id": 102,
            "start_latitude": 27.961307,
            "start_longitude": -82.4493,
            "start_time": "2022-03-04 08:00:00",
            "max_destination_time": "2022-02-04 15:00:00"
        },
        ...
    ]
    """
    paths = []
    for trip_request in request.data:
        id = trip_request['input_trip_id']
        start_lat = trip_request['start_latitude']
        start_long = trip_request['start_longitude']
        start_time = trip_request['start_time']
        max_dest_time = trip_request['max_destination_time']
        path = calculate_route(start_lat, start_long, start_time, max_dest_time)
        result = {
            'input_trip_id': id,
            'load_ids': path
        }
        paths.append(result)
    return HttpResponse(json.dumps(paths))

@api_view(['POST'])
def test(request):
    """
    {
        "name": "Bob"
    }
    """
    name = request.data['name']
    return HttpResponse(f"Hello, {name}.")
