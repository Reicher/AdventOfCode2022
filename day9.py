import math
import time


def calc_distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def get_best_move(x1, y1, x2, y2):
    all_moves = [[x1-1, y1+1], [x1, y1+1], [x1+1, y1+1],
                 [x1-1, y1], [x1+1, y1],
                 [x1-1, y1-1], [x1, y1-1], [x1+1, y1-1]]
    ok_moves = []
    for m in all_moves:
        if calc_distance(m[0], m[1], x2, y2) < 1.5:
            ok_moves.append(m)

    closest = 10
    best = []
    for m in ok_moves:
        dist = calc_distance(m[0], m[1], x1, y1)
        if dist < closest:
            closest = dist
            best = m
    return best


def print_rope(x, y, w, h, rope):
    for px in range(x, x+w):
        line = ''
        for py in range(y, y + h):
            if [px, py] in rope:
                line += '*'
            else:
                line += '.'
        print(line)

def main():
    knots = 10
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    tail_history = [[0, 0]]
    with open('input/input9.txt') as f:
    #with open('input/input_sample.txt') as f:
        for line in f:
            line = line.strip()
            direction, times = line.split(' ')
            for _ in range(int(times)):
                if direction == 'U':  # Up
                    rope[0][1] += 1
                elif direction == 'D':  # Down
                    rope[0][1] -= 1
                elif direction == 'L':  # Left
                    rope[0][0] -= 1
                elif direction == 'R':  # Right
                    rope[0][0] += 1

                for k in range(1, knots):
                    knot_before = rope[k-1]
                    h_t_dist = calc_distance(knot_before[0], knot_before[1], rope[k][0], rope[k][1])
                    if h_t_dist > 1.5:
                        best_move = get_best_move(knot_before[0], knot_before[1], rope[k][0], rope[k][1])
                        rope[k][0] = best_move[0]
                        rope[k][1] = best_move[1]

                if rope[-1] not in tail_history:
                    tail_history.append(rope[-1][:])

    print(len(tail_history))

if __name__ == "__main__":
    main()
