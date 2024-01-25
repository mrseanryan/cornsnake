import urllib.request

from . import util_log

logger = util_log.getLogger(__name__)

# POST request via built in module (avoid dependencies like requests)
def post_request(api_url, headers, timeout):
    req = urllib.request.Request(url=api_url, data=None, headers=headers, origin_req_host=None, unverifiable=False, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status == 200:
            return True
        print(f"POST failed [{response.status}]")
        return False
