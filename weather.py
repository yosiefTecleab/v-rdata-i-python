import requests
import json

CLIENT_ID = ''

def get_source_id(place):
    #place='tron'

    with open("source_id.json", "r") as file:
        id = json.load(file)  #json
        data = id["data"]

    source_id_dict = {}

    #place with the corresponding source id stored in dictionery
    for i in range(len(data)):
        if data[i]['@type'] == 'SensorSystem':
            if data[i]['country'] == 'Norge':
             source_id_dict[data[i]['name']] = data[i]['id']
            

    #some cities have more source stations ,return the first one
    stations=[]     

    for key in source_id_dict:
      if place.upper() in key:
        stations.append(source_id_dict[key])

    return stations[1]



print('Temperatur for sted, gi by navn')
place_string=input()

print('Gi dato i dd.mm.yyyy format, foreksemple 13.10.2022')
date_string = input()

# Split the string by the dot separator
day, month, year = date_string.split('.')

# Reformat the date into yyyy-mm-dd format
DATE = f"{year}-{month}-{day}"

#SOURCE_ID = SOURCE_IDS_DICT["Oslo"]
SOURCE_ID = get_source_id(place_string)

print(f'Temperatur for Oslo {DATE} ')

for HOUR in range(24):
  HOUR_STR = str(HOUR).zfill(2)  # Pad single digits with leading zero
  REFERENCE_TIME = f"{DATE}T{HOUR_STR}:00:00Z"
  URL = f"https://frost.met.no/observations/v0.jsonld?sources={SOURCE_ID}&referencetime={REFERENCE_TIME}&elements=air_temperature"
  response = requests.get(URL, auth=(CLIENT_ID, ''))
  data = response.json()

  hour = data['data'][0]['referenceTime']
  hourly_temperature = data['data'][0]['observations'][0]['value']

  #extract hour in 4 digit format
  hour_4digits = hour[hour.index('T') + 1:hour.index('T') + 6]

  #e.g  Kl 00:00 10 grader
  output = f'Kl {hour_4digits} {hourly_temperature} grader'

  print(output)




