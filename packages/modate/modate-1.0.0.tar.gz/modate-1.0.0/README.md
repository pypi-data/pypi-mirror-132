# modate
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  
![Windows](https://svgshare.com/i/ZhY.svg) ![macOS](https://svgshare.com/i/ZjP.svg)  
[![PyPi version](https://badgen.net/pypi/v/modate/)](https://pypi.com/project/modate) [![Status](https://img.shields.io/pypi/status/modate)](https://pypi.org/manage/project/modate/release/0.0.1/)  


> :warning: Under early developement, beware of file corruption, make a back-up copy beforehand

modate is a Python command line tool that changes a file's or group of files' "created", "modified" or "last accessed" dates.

## Installation

Clone or download this repository and run ```pip``` in its root directory:
```bash
cd path/to/modate
```
```bash
pip install .
```

### Install Using pip
```bash
pip install modate
```

## Usage
```bash
modate -f filename -d YYYYmmdd_HHMMSS -c -m -a
```
```
Options:
-f, --filepath  TEXT  Filepath of the file(s) to modify. Accepts wildcard arguments (i.e.: '*.jpg').
-d, --date      TEXT  Date to be modified
-c, --created         Change the "created" datetime
-m, --modified        Change the "modified" datetime
-a, --accessed        Change the "last opened" datetime
--help                Show this message and exit.
```

Examples:
```bash
# Change the creation time of sample.jpg
modate -f sample.jpg -d 20211222_154210 -c
```

```bash
# Change the modification and creation time of data.csv
modate -f data.csv -d 20211222_154210 -m -c
```

```bash
# Change the creation time of all png files in a folder
modate -f *.png -d 20211222_154210 -c
```

## Upcoming features
- [x] macOS compatibility
- [] Change each file's date based on a date specified in its filename i.e.: ```IMG_2021-12-23_19-14-19.jpg```