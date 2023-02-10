import numpy as np
from PIL import Image


def main():
    reset_map = {
        'lu': (0, 0),
        'ru': (319, 0),
        'ld': (0, 119),
        'rd': (319, 119),
    }
    direct_map = {
        "up":    (0, -1),
        "down":  (0, 1),
        "left":  (-1, 0),
        "right": (1, 0)
    }
    function_map = {
        "a": lambda: 0,
        "b": None,
        "x": None,
        "y": None
    }
    point = np.array((0, 0))
    img_array = np.ones((320, 120), dtype=np.uint8) * 255

    with open('full_dark.plan') as f:
        commands = [line.strip() for line in f.readlines()]

    row_num = 0
    for command in commands:
        row_num += 1
        if command in reset_map:
            point = np.array(reset_map[command])
        elif command in direct_map:
            point += direct_map[command]
        elif command in function_map:
            if (point > (319, 119)).any():
                print('error: row number {}'.format(row_num))
                #point = np.array((min(point[0], 319), min(point[1], 119)))
                #point = np.array((max(point[0], 0), max(point[1], 0)))
            else:
                img_array[tuple(point)] = function_map[command]()
        else:
            pass

    Image.fromarray(img_array.T).save('full_dark.png')


if __name__ == '__main__':
    main()
    # delta = 0.5
    # th = 4
    # img_array = np.ones((320, 120), dtype=np.uint8) * 255
    # for r in range(1, 50):
    #     for row in range(320):
    #         for col in range(120):
    #             ds = (row-160) ** 2 + (col-60) ** 2
    #             if ds >= (r*th-delta) **2 and ds <= (r*th+delta) **2:
    #             # if ds == (r*th) **2:
    #                 img_array[row][col] = 0

    # for row in range(320):
    #     for col in range(120):
    #         if col % 2 == 0:
    #             img_array[row][col] = 0

    # Image.fromarray(img_array.T).save('raw_circle.png')