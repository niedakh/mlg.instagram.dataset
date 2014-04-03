# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import simplejson as json
import time
from datetime import datetime

from config import c_id

count = 33 # this much works

# desired tag
tag = "igers"

# request scheme for recent media per igers tag
request_url = 'https://api.instagram.com/v1/tags/{}/media/recent?count={}&client_id={}'.format(tag, count, c_id)
file_name = "./results/instagram-tags-landscape-{0}.json"
image_count = 0
iteration = 0
max_image_count = 50
image_ids = []
# <codecell>

r = requests.get(request_url)
while image_count < 50:
    print "Iteration {0} | Photo count {1}".format(iteration, image_count)
    if r.status_code != 200:
        print(r)
    result = r.json()
    data = result['data']
    for image in data:
        image_ids.append(image['id'])
    pagination = result['pagination']a
    f = open(file_name.format(iteration), 'w' )
    f.write(json.dumps(result))
    f.close()
    image_count = len(set(image_ids))
    time.sleep(1)
    r = requests.get(pagination['next_url'])
    iteration = iteration + 1

print "Iteration {0} | Photo count {1}".format(iteration, image_count)
