#! /usr/bin/env python2

"""Run it on the server to cleanup the mailman configuration files so that
they are portable
"""

import argparse
import json
import pickle

PATH = {"in": "/var/lib/mailman/lists/%s/config.pck", "out": "config-%s.pck"}

# Parse list name
parser = argparse.ArgumentParser()
parser.add_argument("list", help="The name of the list.")
args = parser.parse_args()

# Load data
data = pickle.load(open(PATH["in"] % args.list, "rb"))

# Cleanup the 'bounce_info'
# Replace instance on Mailman Bounce class for a simple dictionary
for key in data["bounce_info"]:
    data["bounce_info"][key] = vars(data["bounce_info"][key])

# Don't export passwords
del data["password"]
del data["passwords"]

# Dump data out
pickle.dump(data, open(PATH["out"] % args.list, "wb"))
