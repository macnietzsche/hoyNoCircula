import json
from predictor.predictor import Predictor

if __name__ == '__main__':
    print("Pico y Placa - Predictor")
    with open('plates_input.json') as file:
        data = json.load(file)
    
    for entry in data:
        plate=entry['plate']
        date_n_time=entry['datetime']
        prediction=Predictor(date_n_time,plate)
        if prediction.can_my_vehicle_be_on_the_road():
            print(f'Vehicle with plates {plate} can be on the road on {date_n_time}')
        else:
            print(f'Vehicle with plates {plate} cannot be on the road on {date_n_time}')    