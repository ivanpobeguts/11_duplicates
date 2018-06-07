# Anti-Duplicator

This script returns paths of duplicate files located in this specified directory. 
'Duplicated' - are files with the same name and size. 

# How to

Script requires Python 3.5.
Example of launch on Linux/Windows:

``` bash

$ python duplicates.py test_dir

bars.json
-- test_dir\bars.json
-- test_dir\test_dir2\bars.json


jtapiErrors.log
-- test_dir\jtapiErrors.log
-- test_dir\test_dir3\jtapiErrors.log

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
