
## Mailman to Google Groups

A group of useful tools to aid in the migration of PCL's mailman mailing list to Google Groups (G Suite).

## Table of Contents
1. [`export_config`](#export_config) - a tool to export a mailman's list `config.pck` file

## `export_config`

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
