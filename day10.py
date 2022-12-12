class CPU:
    def __init__(self):
        self._cycle = 0
        self._v = 1
        self._commands = []
        self._job: str = ''
        self.crt = ''
        self.sprite_pos = ['#', '#', '#'] + ['.'] * 37
        self._job_cycles_left = 0

        self._crt_width = 40
        self._crt = ''

    def __str__(self):
        return f'CPU on cycle {self._cycle} with reg v = {self._v}. Signal Strength {self.get_signal_strength()}'

    def __repr__(self):
        return f'CPU : {self._cycle} : {self._v}'

    def get_cycle(self):
        return self._cycle

    def have_work(self):
        return self._job or self._commands

    def set_commands(self, commands: [str]):
        self._commands = [c.strip() for c in commands[::-1]]

    def update_sprite_pos(self, debug=False):
        self.sprite_pos = ['.'] * 40
        self.sprite_pos[self._v - 1] = '#'
        self.sprite_pos[self._v] = '#'
        self.sprite_pos[self._v + 1] = '#'
        if debug:
            print(f'{self._cycle} {self.sprite_pos}')

    def update(self):
        # Update sprite pos
        self.update_sprite_pos(debug=False)

        if self.sprite_pos[(self._cycle-1) % self._crt_width] == '#':
            self._crt += '#'
        else:
            self._crt += ' '

        self._job_cycles_left -= 1
        if self._job_cycles_left == 0:
            if self._job.startswith('noop'):
                pass
            elif self._job.startswith('addx'):
                self._v += int(self._job.split(' ')[1])
            # print(f'{self._job} completed')
            self._job = None

    def run_cycle(self):
        self._cycle += 1
        if not self._job:
            if not self._commands:
                return

            future_work = self._commands.pop()
            self._job = future_work
            if future_work.startswith('noop'):
                self._job_cycles_left = 1
            elif future_work.startswith('addx'):
                self._job_cycles_left = 2

        # Info Print
        if False and self._cycle in [20, 60, 100, 140, 180, 220]:
            print(self)

        self.update()

        # Crt Print
        if self._cycle % self._crt_width == 0:
            print(f'{self._crt} (length:{len(self._crt)})')
            self._crt = ''

    def get_signal_strength(self):
        return self._v * self._cycle


def main():
    data = CPU()
    with open('input/input10.txt') as f:
    #with open('input/input_sample.txt') as f:
        lines = f.readlines()

    data.set_commands(lines)

    while True:
        data.run_cycle()
        if not data.have_work():
            break


if __name__ == "__main__":
    main()
