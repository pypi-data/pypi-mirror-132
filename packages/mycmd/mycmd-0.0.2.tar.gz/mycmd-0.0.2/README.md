# MyCmd

MyCmd is a CLI for using MyCommands web app.
MyCmd allows you to easily create and search commands and folders from your commands repository.

## Installing MyCmd

MyCmd is available on [PyPI](https://pypi.org/project/mycmd):

```console
$ python -m pip install mycmd
```

## User Guide

- To open your commands repository in browser
```console
$ mycmd open
```
- To push command to repository in:
  - default folder
    ```console
    $ mycmd push "<command>"
    ```
  - specific folder
    ```console
    $ mycmd push "<command>" -f <folder_name>
    ```
- To get all folders
```console
    $ mycmd getf <folder_name>
```
- To get all commands
```console
    $ mycmd getc
```
-To get all commands from specific folder
```console
    $ mycmd getcf <folder_name>
```
- To search all commands by query
```console
    $ mycmd getcs "<query>"
```
