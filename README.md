# Tetris in Python
## This code was written as a semestral work for a course at FIT CTU

## Control
* right arrow - move the cube to the right
* left arrow - move the cube to the left
* up arrow - rotate the cube by 90°
* down arrow - move the cube down

## Installation
* Creating and activating a virtual environment [optional] 
python3 -m venv env
source env/bin/activate

* Installing the necessary packages
pip3 install -r requirements.txt
python3 setup.py install

## Launching
Karels-MBP:Tetris karel$ python3 src/tetris.py --help  
usage: tetris.py [-h] [-s {slow,standard,fast}]  

optional arguments:  
  -h, --help            show this help message and exit  
  -s {slow,standard,fast}, --speed {slow,standard,fast}  
                        Game speed
