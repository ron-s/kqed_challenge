import requests
import json
#import time

output = []


def get_truck_info():
	"""Contact the SFO API to obtain a JSON list of objects containing all pertinent 
	food truck permit info that will be saved to one JSON file to load into the database."""


	#API endpoint to contact. Make sure to use app token if you're going to contact it regularly
	#url = "https://data.sfgov.org/resource/6a9r-agq8.json&$$app_token=ybQy5wLjPD5YeX6uCeahIgRdT"
	url = "https://data.sfgov.org/resource/6a9r-agq8.json"

	r = requests.get(url)

	data = r.json()

	#parse the json that you just retrieved 
	for val in data:

		trucks = {}
		trucks["pk"] = val["objectid"]
		trucks["fields"] = {}
		trucks["model"] = "food_trucks_app.MobileFoodTrucks"
		
		try:
			trucks["fields"]["applicant"] = val["business_name"]
		except KeyError:
			trucks["fields"]["applicant"] = ""

		try:
			trucks["fields"]["address"] = val["address"]
		except KeyError:
			trucks["fields"]["status"] = ""

		try:
			trucks["fields"]["status"] = val["permit_status"]
		except KeyError:
			trucks["fields"]["status"] = ""

		try:
			trucks["fields"]["dayshours"] = val["hours_of_operation"]
		except KeyError:
			trucks["fields"]["dayshours"] = ""

		try:
			trucks["fields"]["fooditems"] = val["cuisine"]
		except KeyError:
			trucks["fields"]["fooditems"] = ""

		try:
			trucks["fields"]["latitude"] = val["latitude"]
		except KeyError:
			trucks["fields"]["latitude"] = ""

		try:
			trucks["fields"]["longitude"] = val["longitude"]
		except KeyError:
			trucks["fields"]["longitude"] = ""

		try:
			trucks["fields"]["expirationdate"] = val["permit_exp_date"]
		except KeyError:
			trucks["fields"]["expirationdate"] = ""
	
	#add the trucks dict to the food_trucks list
	output.append(trucks)


	#create a json file that contains the results.
	with open('trucks.json', "w") as f:
		json.dump(output, f, indent=2)


if __name__ == '__main__':
	get_truck_info()