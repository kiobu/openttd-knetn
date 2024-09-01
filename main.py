import requests

states = ["MA", "NH", "CT", "RI", "VT", "ME"]
base_url = "http://api.geonames.org/searchJSON?username=kiobu&country=US&featureClass=P&continentCode=NA&maxRows=1000&adminCode1={STATE}"

preprocessed_towns = []

print(f":: extracting towns and cities from: {states}")

for state in states:
    print(f":: requesting: {state} ...")
    response_json = requests.get(base_url.format(STATE=state)).json()
    for town in response_json['geonames']:
        preprocessed_towns.append(town['toponymName'])

print(":: sanitizing town names...")
postprocessed_towns = list(set([town for town in preprocessed_towns if
                                "-" not in town and
                                "/" not in town and
                                " " not in town and
                                "West" not in town and
                                "North" not in town and
                                "East" not in town and
                                "South" not in town
                                ]))

print(":: writing result to file...")
with open("towns.txt", "w") as file:
    for town in postprocessed_towns:
        file.write(town + "\n")

print(":: done!")