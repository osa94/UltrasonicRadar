## General
Radar using an ultrasonic sensor, operating in the range of 0-180 degrees and a maximum distance of 200 cm. Project is divided into two parts, the first one concerns pico 2w control, the second one concerns radar visualization on PC. 

## Warning 
Application was used on Windows 10

## Required components
- RPI Pico2W
- ultrasonic sensor (HC-SR04) 
- servo (SG90)   
- mounting bracket for HC-SR04
- logic level converter
- wires for prototyping board
- prototype board
- cable USB - microUSB

## Setup
1. Connect the device as shown in the electrical diagram
2. Download and install python 3.10 (https://www.python.org/downloads/)
3. Execute command: ``` pip install -r requirements.txt ```
4. Download .uf2 file (pico 2w) from https://micropython.org/download/
5. Press boot button on pico 2w and copy file .uf2
6. Reconnect pico2w
7. change default_port name to your port name in config/config.json
8. Program pico: ``` python .\program_pico2w\program_pico2w.py ```
9. Reconnect pico2w
10. Execute command: ``` python .\main.py ```