import subprocess
from argparse import ArgumentParser

class Pico2WProgrammer(ArgumentParser):
    DEFAULT_BUFFER_SIZE = 512
    DEFAULT_PORT = 'COM7'
    DEFAULT_FILENAME = 'pico2w_program_commands.txt'

    def __init__(self):
        super().__init__()
        self.add_argument('-bs', '--buffer-size', default=self.DEFAULT_BUFFER_SIZE)
        self.add_argument('-p', '--port', default=self.DEFAULT_PORT)
        self.add_argument('-f', '--filename', default=self.DEFAULT_FILENAME)
        self.args = self.parse_args()

if __name__ == '__main__':
    pico2w_programmer = Pico2WProgrammer()
    subprocess.run(['rshell',
                    '-p', f'{pico2w_programmer.args.port}',
                    '-f', f'{pico2w_programmer.args.filename}',
                    '--buffer-size', f'{pico2w_programmer.args.buffer_size}'])