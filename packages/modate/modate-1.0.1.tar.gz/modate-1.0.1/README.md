# modate
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  
![Windows](https://svgshare.com/i/ZhY.svg) ![macOS](https://svgshare.com/i/ZjP.svg)  
[![PyPi version](https://badgen.net/pypi/v/modate/)](https://pypi.com/project/modate) [![Status](https://img.shields.io/pypi/status/modate)](https://pypi.org/manage/project/modate/release/0.0.1/)  

modate is a Python command line tool that changes a file's or group of files' "created", "modified" or "last accessed" dates.

## Installation

```bash
pip install --upgrade modate
```

## Usage
Declaring a date manually:
```bash
modate -f filepath -d YYYYmmdd_HHMMSS -c -m -a
```

Getting the date from the filename:
```bash
modate -f filepath -df srtftime_args -c -m -a
```

Options:
```
  -f, --filepath TEXT      Filepath of the file(s) to modify. 
                           Accepts wildcard arguments.
  -d, --date TEXT          Date to use.
  -df, --date_format TEXT  Specify format in which the date is stated in the
                           filename. Use strftime directives.
  -c, --created            Change the "created" datetime.
  -m, --modified           Change the "modified" datetime.
  -a, --accessed           Change the "last opened" datetime.
  --help                   Show this message and exit.
```
For details on how to use strftime directives visit https://www.programiz.com/python-programming/datetime/strftime  
  
## Examples:
Change the 'created' time of sample.jpg to 2021-Nov-22 15:42:10
```bash
modate -f sample.jpg -d 20211222_154210 -c
```

Change the 'created' time of img_2021-11-22.jpg automatically
```bash
modate -f sample.jpg -df %Y%m%d -c
```

Change the 'modified' and 'created' time of data.csv to 2021-Nov-22 15:42:10
```bash
modate -f data.csv -d 20211222_154210 -m -c
```  

Change the 'created' time of all png files in a folder to 2021-Nov-22 15:42:10
```bash
modate -f *.png -d 20211222_154210 -c
```

Change the 'modified' time of all files in a folder automatically
```bash
# Files in the folder:
# data_2021-11-22_15-42-10.csv
# data_2021-12-10_23-02-56.csv
# data_2021-12-27_12-23-38.csv

modate -f *.csv -df %Y-%m-%d_%H-%M-%S -c
```

## Upcoming features
- [x] macOS compatibility
- [x] Change each file's date based on a date specified in its filename i.e.: ```IMG_2021-12-23_19-14-19.jpg```