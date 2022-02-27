# The Brazen Gears: LoadMode

Simple API that determines the optimal route for a trucker given certain constraints.

## Set up
1. Move into the `/salesman` directory.
2. Set up a Python virtual environment using `python -m venv .venv`.
3. Install the project dependencies using `python -m pip install -r requirements.txt`.

You should now be all set to calculate optimal routes and help truckers minimize deadhead! The API can be run locally using `python manage.py runserver`. By default, the API will be available at `localhost:8000`.

## The API
One endpoint is provided: `POST /findpath`.

Requests should be made in the following format:
```
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
   }
]
```

The response will be a list of routes in the following format:
```
[
    {
        "input_trip_id": 101,
        "load_ids": [ 434307296, 401121 ]
    },
    {
        "input_trip_id": 102,
        "load_ids": [ 434307296 ]
    }
]
```

## The marketplace
The available loads are retrieved from the file `salesman\data\123Loadboard_CodeJam_2022_dataset.csv`. After updating the marketplace, open an interactive Python session using `python manage.py shell`. To organize the new data, run the following code:
```
from data import update_marketplace
update_marketplace.main()
```
