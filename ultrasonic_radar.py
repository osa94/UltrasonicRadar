import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import serial
import time
import random
import threading
from itertools import cycle

dummy_angles = cycle(list(range(0, 181, 1)) + list(range(179, 0, -1)))
distance1 = 150
distance2 = 68
distance3 = 0
objects_coordinates = {}
def make_fake_coordinates():
    for angle in list(range(0, 181, 1)):
        if 160 > angle > 120:
            distance = distance1
            objects_coordinates[angle] = distance
        elif 90 > angle > 78:
            distance = distance2
        else:
            distance = distance3

        objects_coordinates[angle] = distance




class Radar:
    MAX_DISTANCE = 200  # cm
    MIN_DISTANCE = 0  # cm
    STEP_DISTANCE = 1  # cm
    MIN_ANGLE = 0
    MAX_ANGLE_RAD = np.pi
    MAX_ANGLE_DEG = 180
    THETA_GRID_NR = 7
    TICKS_NR = 9

    # def __init__(self, com_port):
    def __init__(self):
        mpl.rcParams['toolbar'] = 'None'
        plt.ion()

        # self.serial = serial.Serial(com_port)
        self.__fig, self.__ax = plt.subplots(subplot_kw={'projection': 'polar', 'facecolor': 'darkgreen'})
        self.__manager = self.__fig.canvas.manager

        self.__set_fig_params()
        self.__set_ax_params()
        self.__set_manager_params()

        self.__radius = np.arange(self.MIN_DISTANCE, self.MAX_DISTANCE, self.STEP_DISTANCE)
        self.__scan = self.MIN_ANGLE * self.__radius

        self.theta_object = []
        self.distance_object = []

        self.__scan_line, = self.__ax.plot([], color='lightblue', linewidth=2)
        self.__points, = self.__ax.plot([], linewidth=0, markersize=5, marker='x', color='red')

        self.__inverted_scan_direction = False

    def __set_fig_params(self):
        self.__fig.set_facecolor('black')

    def __set_manager_params(self):
        self.__manager.window.showMaximized()
        self.__manager.set_window_title('Radar')

    def __set_ax_params(self):
        self.__ax.set_ylim(self.MIN_DISTANCE, self.MAX_DISTANCE)
        self.__ax.set_xlim(self.MIN_ANGLE, self.MAX_ANGLE_RAD)
        self.__ax.tick_params(labelcolor='white')
        self.__ax.set_rticks(np.linspace(self.MIN_DISTANCE, self.MAX_DISTANCE, self.TICKS_NR))
        self.__ax.set_thetagrids(np.linspace(self.MIN_ANGLE, self.MAX_ANGLE_DEG, self.THETA_GRID_NR))

    def run(self):
        make_fake_coordinates()
        for angle in dummy_angles:
            if plt.fignum_exists(self.__fig.number):
                if objects_coordinates.get(angle) > self.MIN_DISTANCE:
                    self.theta_object.insert(0, np.pi / 180 * angle)
                    self.distance_object.insert(0, objects_coordinates.get(angle))

                self.__scan_line.set_data(self.__scan + np.pi / 180 * angle, self.__radius)
                self.__points.set_data(self.theta_object, self.distance_object)

                # self.__fig.canvas.draw()
                self.__fig.canvas.flush_events()
                if angle >= 180:
                    self.theta_object.clear()
                    self.distance_object.clear()
                if angle <= 0:
                    self.theta_object.clear()
                    self.distance_object.clear()
            else:
                exit(0)

# radar = Radar()
# radar.run()
