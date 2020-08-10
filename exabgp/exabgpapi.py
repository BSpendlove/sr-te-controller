#!/usr/bin/env python
import json
import os
import requests
import env_file
from sys import stdin, stdout

def message_parser(line):
    temp_message = json.loads(line)

    return temp_message

api_details = env_file.get(path="/exabgp/env/api")
api_url = api_details["flask_api"]

counter = 0
while True:
    try:
        line = stdin.readline().strip()
        
        # When the parent dies we are seeing continual newlines, so we only access so many before stopping
        if line == "":
            counter += 1
            if counter > 100:
                break
            continue
        counter = 0
        
        # Parse message, and if it's the correct type, store in the database
        message = message_parser(line)
        if message:
            if message["type"] == "state":
                if message["neighbor"]["state"] == "up":
                    # /exabgp/neighbor/state/up
                    pass
                if message["neighbor"]["state"] == "down":
                    # /exabgp/neighbor/state/down
                    pass
                if message["neighbor"]["state"] == "connected":
                    # /exabgp/neighbor/state/connected
                    pass
                requests.post("{}/exabgp/state".format(api_url), json=message)
            if message["type"] == "update":
                # Determine the message type... eg bgpls-node, bgpls-link, bgpls-prefix-v4 or bgpls-prefix-v6
                # /exabgp/update/bgpls/node
                # /exabgp/update/bgpls/link
                # /exabgp/update/bgpls/prefixv4
                # /exabgp/update/bgpls/prefixv6
                requests.post("{}/exabgp/update".format(api_url), json=message)

    except KeyboardInterrupt:
        pass
    except IOError:
        # most likely a signal during readline
        pass
