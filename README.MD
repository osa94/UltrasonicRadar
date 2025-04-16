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
1. Mount HC-SR04 on mounting bracket
2. Connect the devices as shown in the electrical diagram
3. Download and install python 3.10 (https://www.python.org/downloads/)
4. Execute command: ``` pip install -r requirements.txt ```
5. Download .uf2 file (pico 2w) from https://micropython.org/download/
6. Press boot button on pico 2w and copy file .uf2
7. Reconnect pico2w
8. Change default_port name to your port name in config/config.json
9. Program pico: ``` python .\program_pico2w\program_pico2w.py ```
10. Reconnect pico2w
11. Execute command: ``` python .\main.py ```

## TODO:
1. Add bluetooth communication between pico 2w and PC
2. Add containerization