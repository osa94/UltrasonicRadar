from PC.ultrasonic_radar import Radar
import json


if __name__ == '__main__':
    with open('config/config.json', 'r') as config_file:
        data = json.load(config_file)
        port = data['default_port']
    radar = Radar(port)
    radar.run()
