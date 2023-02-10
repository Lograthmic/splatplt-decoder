import turtle

def main():
    reset_map = {
        'lu': (0, 0),
        'ru': (319, 0),
        'ld': (0, 119),
        'rd': (319, 119),
    }
    direct_map = {
        "up":    (-1, 0),
        "down":  (1, 0),
        "left":  (0, -1),
        "right": (0, 1)
    }
    function_map = {
        "a": lambda: 255,
        "b": None,
        "x": None,
        "y": None
    }