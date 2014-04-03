# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import simplejson as json
import time
from datetime import datetime

from config.py import c_id

count = 33 # this much works

# <codecell>

request_url = 'https://api.instagram.com/v1/tags/igers/media/recent?count={}&client_id={}'.format(count,c_id)
max_tag_id_url = '&max_tag_id={}'
file_name = "./instagram-tags-landscape-{0}.json"
image_count = 0
iteration = 0

# <codecell>

r = requests.get(request_url)
while image_count < 50:
    print "Iteration {0} | Photo count {1}".format(iteration, image_count)
    if r.status_code != 200:
        print(r)
    result = r.json()
    data = result['data']
    pagination = result['pagination']
    f = open(file_name.format(iteration), 'w' )
    f.write(json.dumps(result))
    f.close()
    image_count = image_count + len(data)
    time.sleep(1)
    r = requests.get(pagination['next_url'])
    iteration = iteration + 1

print "Iteration {0} | Photo count {1}".format(iteration, image_count)

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


