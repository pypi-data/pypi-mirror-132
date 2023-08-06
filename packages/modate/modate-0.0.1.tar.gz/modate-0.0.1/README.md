# modate
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![Windows](https://svgshare.com/i/ZhY.svg) ![macOS](https://svgshare.com/i/ZjP.svg)
[![Status](https://img.shields.io/pypi/status/modate)]()


modate is a Python command line tool that changes a file's or group of files "created", "modified" or "last accessed" dates.

The tool currently only works on Windows machines.

## Installation

Clone or download this repository and run ```pip``` in its root directory:
```bash
cd path/to/modate
```
```bash
pip install .
```

#### Using pip
> :warning: Under developement
> Not yet available
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
