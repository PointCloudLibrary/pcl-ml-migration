#! /usr/bin/env python3

import argparse
import os
import pathlib
import pickle

import yaml

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument(
    "configuration",
    help="The configuration file which specifies all "
    "required information for the clone.",
)
args = parser.parse_args()

# Parse configuration
clone_config = yaml.load(open(args.configuration).read())

# Load data
original_prefix = pathlib.Path(clone_config["original"])
config = pickle.load(open(original_prefix / "config.pck", "rb"))

# Extract only required users
delivery_status = dict()
digest_members = dict()
members = dict()
language = dict()
user_options = dict()
usernames = dict()
owners = []
for user in clone_config["users"]:

    # Check if user has a special delivery status
    if user["email"] in config["delivery_status"]:
        delivery_status[user["email"]] = config["delivery_status"][user["email"]]

    # Check if user wants digest delivery
    if user["email"] in config["digest_members"]:
        digest_members[user["email"]] = config["digest_members"][user["email"]]

    # Check if user wants normal delivery
    if user["email"] in config["members"]:
        members[user["email"]] = config["members"][user["email"]]

    # Copy user language preferences
    if user["email"] in config["language"]:
        language[user["email"]] = config["language"][user["email"]]

    # Copy user options
    if user["email"] in config["user_options"]:
        user_options[user["email"]] = config["user_options"][user["email"]]

    # Copy usernames
    if user["email"] in config["usernames"]:
        usernames[user["email"]] = config["usernames"][user["email"]]

    # Check if user is owner
    if "owner" in user:
        if user["owner"]:
            owners.append(user["email"])

# Replace original fields
config["delivery_status"] = delivery_status
config["digest_members"] = digest_members
config["members"] = members
config["language"] = language
config["user_options"] = user_options
config["usernames"] = usernames
config["owner"] = owners


# Create output files
prefix = clone_config["prefix"] if "prefix" in clone_config else "."
folder = pathlib.Path(prefix) / clone_config["name"]

if not folder.exists():
    mkdir(folder)
os.symlink(original_prefix / "archive.mbox", folder / "archive.mbox")
pickle.dump(config, open(folder / "config.pck", "wb"))
