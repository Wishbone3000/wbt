# My idea is this - when someone calls you, check the weather in their area

import requests
from pprint import pprint

#GET http://api.wunderground.com/api/394fa64c4b9c0059/features/settings/q/query.format
#api.wunderground.com/api/394fa64c4b9c0059/conditions/q/85355.json
our_api = 'http://api.wunderground.com/api/%s/conditions/q/%s.json'
zipcode = '85355'
apikey = '394fa64c4b9c0059'

#get zipcode input

user_zip = input('Enter your zipcode')
if user_zip.isdigit() and len(user_zip)== 5:
    zipcode = user_zip

our_url = our_api % (apikey,zipcode)
r = requests.get(our_url)
data = r.json()

# what does it feel like there?
print(data['current_observation'].get('feelslike_f'))

