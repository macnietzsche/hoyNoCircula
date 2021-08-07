# Quito Distrito Metropolitano - Pico y Placa
Because of the increasing number of cars, Quito Distrito Metropolitano has develop a strategy called "Pico y Placa" that aims to decrease vehicle traffic on busy hours. Vehicles are prohibited to be on the roads depending on their plates, day of the week and time; according to the following table:

| Day of the week             | Plates allowed to be on the road | Plates not allowed to be on the road | Restriction schedule     |
| ----------------------------| -------------------------------- |--------------------------------------|--------------------------|
|Monday, Wednesday, Friday     | 1,3,5,7,9                        |0,2,4,6,8                             |07:00-09:30/16:00-19:30   |
|Tuesday, Thursday, Saturday   | 0,2,4,6,8                        |1,3,5,7,9                             |07:00-09:30/16:00-19:30   |
|Sunday, Holidays             | All                              |None                                  |07:00-09:30/16:00-19:30   |

## Introducing Can my car be on the road? - Predictor
As many car drivers have been fined due to their lack of knowledge about Pico y Placa, we have developed a predictor that tells if a vehicle can be on the roads based on its plate, date and time.

### Requirements
The project requires [Python 3.7](https://www.python.org/downloads/release/python-370/) and
the [PIP](https://pip.pypa.io/en/stable/) package manager.

### Add input data
In order to get a prediction, the user must provide the vehicle(s)' plate, date and time in ```plates_input.json```; following the JSON structure below:
```json
[
  { "plate": "AAA-0820", "datetime": "2020-12-01 15:23" },
  { "plate": "ABB-0826", "datetime": "2021-08-01 15:23" },
]
```
Please notice that plate's format must be AAA-1234 or AAA-123 and datetime's format must be YYYY-MM-DD HH:MM 
### Run the application and get predicitions
```console
$ python src/app.py
```
The JSON input above will produce the following predictions on the console:
```console
$ Vehicle with plates AAA-0820 can be on the road on 2020-12-01 15:23
$ Vehicle with plates AAA-0826 can be on the road on 2021-08-01 15:23
```

## For administrators
The configuration file ```config/restrictions.ini``` has been generated to help administrators manage restrictions' behavior in case they need to. Below is an example of a restriction configuration for Monday:
```ini
[MONDAY]
restricted=yes
restricted_time = 07:00-09:30/16:00-19:30
restricted_plate_ending_digit = 2,4,6,8,0
```
where:
- the day is mapped by its full name in uppercase,
- ```restricted=yes``` denotes restriction is enabled on that day whereas ```restricted=no``` would denote restriction is disabled; if this last is the case, ```restricted_time``` and ```restricted_plate_ending_digit``` will be ignored.
- ```restricted_time``` are the segments of time when restriction applies. Notice that time segments are separated by ```/```. Each segment must have a start and end time where ```start time > end time```
- ```restricted_plate_ending_digit``` are those plate's ending digits that applies for restriction. Notice that each digit is separated by a ```,```

## For developers
### Run the tests
```console
$ python -m pytest
```
14 tests have been written in order to test subdomains (units), services, and end-to-end points. Settings handler subdomain has testing and production environments, so when running tests, the configuration file is ```test/config/restrictions_testing.ini```



