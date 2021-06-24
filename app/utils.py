from django.http import Http404

import time
import hashlib
import requests
from django.conf import settings

def workflow_request(method, url, username, data=None):
    timestamp = str(time.time())[:10]
    ori_str = timestamp + settings.LOONFLOW_TOKEN
    signature = hashlib.md5(ori_str.encode(encoding='utf-8')).hexdigest()
    headers = dict(signature=signature, timestamp=timestamp, appname=settings.LOONFLOW_APP_NAME, username=username)
    url = settings.LOONFLOW_HOST + url

    if method == "get":
        r = requests.get(url, headers=headers, params=data)
    elif method == "post":
        r = requests.post(url, headers=headers, json=data)
    elif method == "patch":
        r = requests.patch(url, headers=headers, json=data)
    else:
        # TODO: another method handler
        raise Http404

    if r.raise_for_status() is None:
        return r.json()