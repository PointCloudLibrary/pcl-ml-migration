
## Mailman to Google Groups

A group of useful tools to aid in the migration of PCL's Mailman 2 mailing list to Google Groups (G Suite).

## Table of Contents
1. [Organizing your Data](#organizing-your-data)
2. [export_config](#export_config) - a tool to export a portable mailman's list `config.pck`
3. [create_dev_list](#create_dev_list) - creates a reduced member list from an already existing one

## Organizing your Data

There are two main files which contain all relevant data about a mailing list:
- `config.pck`, the lists configuration file. It contains information the list's settings, users and user preferences.
- `<list_name>.mbox` the email archive file. It contains all emails sent to the mailing list.

Designating mailman's installation prefix as `<prefix>`, both files can be found at `<prefix>/lists/<list_name>/config.pck` and `<prefix>/archives/private/<list_name>.mbox/<list_name>.mbox`, respectively.

Most of the tools in this repository will expect you to have pulled copied/exported these files out of the server, and place them somewhere in your computer organized as:
```
$ tree pcl-users/
pcl-users/
├── archive.mbox
└── config.pck
```

The directory provides implicitly the list's name and both the mails' archive and list configuration file have been renamed to `archive.mbox` and `config.pck`, respectively.

**Important:** In order to export a portable `config.pck` you are likely to have to export it using [`export_config`](#export_config).

[Go back up.](#table-of-contents)

## export_config

This tools allows you to export a mailman's list `config.pck` file. It strips the original configuration file of all password related information and converts all custom classes to simple dictionaries, to ensure the file can be parsed on any standard Python installation.

It assumes a typical mailman installation at `/var/lib/mailman`. It might happen that the `Mailman` python module is not visible for the installation. If that's the case, just export the path
```shell
$ export PYTHONPATH="/var/lib/mailman:$PYTHONPATH"
```

Here's an usage description of the tool.
```
$ ./export_config.py --help
usage: export_config.py [-h] list

positional arguments:
  list        The name of the list.

optional arguments:
  -h, --help  show this help message and exit
```
Just supply the name of the list you wish to export the config, e.g.
```
$ ./export_config.py pcl-developers
```

will export a `config-pcl-developers.pck` in the current working directory.

[Go back up.](#table-of-contents)

## create_dev_list

This tool allows you to create a reduced member list from an existing one. It will look for the specified users in the old list and will populate the new list with the users it manages to find. The mailbox archive will be simply symlinked. The tool assumes you have your data organized as described in the [Organizing your Data](#organizing-your-data) section. To use it, you need to supply a YAML configuration file like the one bellow.
```yaml
name: pcl-admins
prefix: /tmp/data

original: /tmp/pcl-developers

users:
  - email: owner@pointclouds.org
    owner: true
  - email: user-1@pointclouds.org
  - email: user-2@pointclouds.org

```
A brief explanation of the keys is provided:
- `name`: the name for the new list.
- `prefix` (optional): the folder prefix to create the files.
- `original`: the path to the original list files
- `users`: the list of users to be migrated
	- `email`: the user's email
	- `owner`(optional): a key which specified if the user should be upgraded to owner of the new list.


[Go back up.](#table-of-contents)
