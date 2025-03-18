import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
import random
import threading


class Radar:
    MAX_DISTANCE = 200  # cm
    MIN_DISTANCE = 0  # cm
    STEP_DISTANCE = 1  # cm
    MIN_ANGLE = 0
    MAX_ANGLE_RAD = np.pi
    MAX_ANGLE_DEG = 180
    THETA_GRID_NR = 7
    TICKS_NR = 5

    def __init__(self):
        mpl.rcParams['toolbar'] = 'None'
        plt.ion()

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
        self.__points, = self.__ax.plot([], linewidth=0, markersize=10, marker='o', color='red')

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
        obj_rad = np.pi / 2
        dist = 75
        mul = 0
        while plt.fignum_exists(self.__fig.number):
            if np.pi / 180 * mul == obj_rad:
                self.theta_object.insert(0, obj_rad)
                self.distance_object.insert(0, dist)
            self.__scan_line.set_data(self.__scan + np.pi / 180 * mul, self.__radius)
            self.__points.set_data(self.theta_object, self.distance_object)

            self.__fig.canvas.draw()
            self.__fig.canvas.flush_events()
            if mul >= 180:
                self.__inverted_scan_direction = True
                self.theta_object.clear()
                self.distance_object.clear()
            if mul <= 0:
                self.theta_object.clear()
                self.distance_object.clear()
                self.__inverted_scan_direction = False
            if self.__inverted_scan_direction:
                mul -= 2
            else:
                mul += 2

