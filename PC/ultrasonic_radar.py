import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import serial


class Radar:
    MAX_DISTANCE = 200  # cm
    MIN_DISTANCE = 0  # cm
    STEP_DISTANCE = 1  # cm
    MIN_ANGLE = 0
    MAX_ANGLE_RAD = np.pi
    MAX_ANGLE_DEG = 180
    THETA_GRID_NR = 7
    TICKS_NR = 9

    def __init__(self, com_name: str) -> None:
        """

        :param com_name: Serial port name
        """
        mpl.rcParams['toolbar'] = 'None'
        mpl.use('Tkagg')
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
        self.__points, = self.__ax.plot([], linewidth=0, markersize=5, marker='x', color='red')

        self.__inverted_scan_direction = False

        self.__serial_connection = serial.Serial(com_name)

    def __set_fig_params(self) -> None:
        """
        Method responsible for setting the figure parameters.
        :return: None
        """
        self.__fig.set_facecolor('black')

    def __set_manager_params(self) -> None:
        """
        Method responsible for setting the manager parameters.
        :return: None
        """
        self.__manager.window.state('zoomed')
        self.__manager.set_window_title('Radar')

    def __set_ax_params(self) -> None:
        """
        Method responsible for setting the axes parameters.
        :return: None
        """
        self.__ax.set_ylim(self.MIN_DISTANCE, self.MAX_DISTANCE)
        self.__ax.set_xlim(self.MIN_ANGLE, self.MAX_ANGLE_RAD)
        self.__ax.tick_params(labelcolor='white')
        self.__ax.set_rticks(np.linspace(self.MIN_DISTANCE, self.MAX_DISTANCE, self.TICKS_NR))
        self.__ax.set_thetagrids(np.linspace(self.MIN_ANGLE, self.MAX_ANGLE_DEG, self.THETA_GRID_NR))

    def run(self) -> None:
        """
        Method responsible for running the Radar.
        :return: None
        """
        while True:
            self.__serial_connection.flushInput()
            self.__serial_connection.flushOutput()
            mes = self.__serial_connection.read_until(expected=b'\r')
            mes = mes.decode('utf-8')
            angle, dist = mes.split(',')
            dist = float(dist)
            angle = int(angle)

            if plt.fignum_exists(self.__fig.number):
                if self.MIN_DISTANCE < dist <= self.MAX_DISTANCE:
                    self.theta_object.insert(0, np.pi / self.MAX_ANGLE_DEG * angle)
                    self.distance_object.insert(0, dist)

                self.__scan_line.set_data(self.__scan + np.pi / self.MAX_ANGLE_DEG * angle, self.__radius)
                self.__points.set_data(self.theta_object, self.distance_object)

                # self.__fig.canvas.draw()
                self.__fig.canvas.flush_events()
                if angle >= self.MAX_ANGLE_DEG:
                    self.theta_object.clear()
                    self.distance_object.clear()
                if angle <= self.MIN_ANGLE:
                    self.theta_object.clear()
                    self.distance_object.clear()
            else:
                self.__serial_connection.close()
                exit(0)
