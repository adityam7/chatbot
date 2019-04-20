from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import zomatopy
import pandas as pd
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import json

config={"user_key":"0c0148465fbe9a2b4289ed6a999afcbf"}
zomato = zomatopy.initialize_app(config)

def begin_search(loc,cuisine,price):
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	location_results = len(location_json['location_suggestions'])
	lat=location_json["location_suggestions"][0]["latitude"]
	lon=location_json["location_suggestions"][0]["longitude"]
	city_id=location_json["location_suggestions"][0]["city_id"]
	cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85, 'thai': 95}
	d = []
	df = pd.DataFrame()
	results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), limit=100)
	d1 = json.loads(results)
	d = d1['restaurants']
	df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'], 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
		'restaurant_address': x['restaurant']['location']['address'],'budget_for2people': x['restaurant']['average_cost_for_two'],
		'restaurant_photo': x['restaurant']['featured_image'], 'restaurant_url': x['restaurant']['url'] } for x in d])
	df = df.append(df1)
	def budget_group(row):
		if row['budget_for2people'] <300 :
			return 'lesser than 300'
		elif 300 <= row['budget_for2people'] <700 :
			return 'between 300 to 700'
		else:
			return 'more than 700'

	df['budget'] = df.apply(lambda row: budget_group (row),axis=1)
		#sorting by review & filter by budget
	restaurant_df = df[(df.budget == price)]
	restaurant_df = restaurant_df.sort_values(['restaurant_rating'], ascending=0)	

	return restaurant_df