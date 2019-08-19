#Topic: Curl
#-----------------------------
#libraries

import requests
r = requests.get('https://github.com/timeline.json')
r.json()
