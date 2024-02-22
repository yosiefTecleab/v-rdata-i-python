import json


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
  stations = []

  for key in source_id_dict:
    for word in key.split(' '):
      if word == place.upper():
        stations.append(source_id_dict[key])
        #print(key)
  return stations
  #print(stations)


stas = get_source_id('oslo')

if len(stas) > 0:

  print(stas)
  #print(stations)
else:
  print('No data found for this location')
