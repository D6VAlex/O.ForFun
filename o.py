import os
import sys
import time
import math
import random
import shutil


def wtf():
    return shutil.get_terminal_size((110, 38))


def what_do_u_wanna(c):
    return f"\033[38;2;{c[0]};{c[1]};{c[2]}m"


R = "\033[0m"
HIDE = "\033[?25l"
SHOW = "\033[?25h"
CLEAR = "\033[2J"
HOME = "\033[H"


def fuck_u():
    sys.stdout.write(CLEAR + HOME)
    sys.stdout.flush()


def where_is_my_name():

    title = "By z01309z"
    names = []

    w, h = wtf()

    x = max(1, (w - len(title)) // 2)
    y = max(1, h // 2)

    sys.stdout.write(CLEAR)

    for i in range(1, len(title) + 1):

        sys.stdout.write(HOME)
        sys.stdout.write(f"\033[{y};{x}H")

        sys.stdout.write(
            what_do_u_wanna((245, 245, 245))
            + title[:i]
            + R
        )

        sys.stdout.flush()
        time.sleep(0.13)

    time.sleep(0.8)

    for _ in range(28):

        w, h = wtf()

        x = random.randint(1, max(1, w - 8))
        y = random.randint(1, max(1, h - 2))

        names.append((
            x,
            y,
            random.choice([
                (245, 245, 245),
                (255, 130, 45),
                (75, 205, 220)
            ])
        ))

        sys.stdout.write(CLEAR + HOME)

        for px, py, c in names:

            sys.stdout.write(
                f"\033[{py};{px}H"
                + what_do_u_wanna(c)
                + "z01309z"
                + R
            )

        sys.stdout.flush()
        time.sleep(0.13)

    time.sleep(0.8)


def bro_is_loading():

    fuck_u()

    w, h = wtf()

    width = min(36, max(1, w - 10))

    x = max(1, (w - width) // 2)
    y = max(1, h // 2)

    for progress in range(width + 1):

        sys.stdout.write(CLEAR + HOME)

        for i in range(progress):

            sys.stdout.write(
                f"\033[{y};{x+i}H"
                + what_do_u_wanna((255, 130, 45))
                + "█"
                + R
            )

        sys.stdout.flush()
        time.sleep(0.045)

    time.sleep(0.5)
    fuck_u()


def create_canvas(w, h):

    grey = (95, 95, 105)

    return [
        [(" ", grey) for _ in range(w)]
        for _ in range(h)
    ]


def put(canvas, x, y, char, c):

    h = len(canvas)
    w = len(canvas[0])

    if 0 <= x < w and 0 <= y < h:
        canvas[y][x] = (char, c)


def draw_line(canvas, x1, y1, x2, y2, c):

    steps = max(
        abs(x2 - x1),
        abs(y2 - y1),
        1
    )

    for i in range(steps + 1):

        t = i / steps

        x = int(x1 + (x2 - x1) * t)
        y = int(y1 + (y2 - y1) * t)

        put(
            canvas,
            x,
            y,
            random.choice(".*+:"),
            c
        )


def circle(canvas, cx, cy, radius, c, phase=0):

    for angle in range(0, 360, 3):

        a = math.radians(angle + phase)

        x = int(cx + math.cos(a) * radius)
        y = int(
            cy + math.sin(a) * radius * 0.48
        )

        put(
            canvas,
            x,
            y,
            random.choice("oO.*+"),
            c
        )


def diamond(canvas, x, y, size, c):

    points = [
        (x, y - size),
        (x + size, y),
        (x, y + size),
        (x - size, y),
        (x, y - size)
    ]

    for i in range(4):

        draw_line(
            canvas,
            *points[i],
            *points[i + 1],
            c
        )


def make_some_chaos(w, h):

    colors = [
        (245, 245, 245),
        (255, 130, 45),
        (75, 205, 220),
        (170, 110, 255),
        (95, 95, 105)
    ]

    particles = []

    for _ in range(150):

        particles.append({

            "x": random.uniform(0, w - 1),
            "y": random.uniform(0, h - 1),
            "speed": random.uniform(0.1, 0.7),
            "symbol": random.choice([".", "*", "·", "+"]),
            "color": random.choice(colors)

        })

    return particles


def move_the_dots(canvas, particles):

    h = len(canvas)
    w = len(canvas[0])

    for p in particles:

        p["y"] -= p["speed"]
        p["x"] += math.sin(p["y"] * 0.1) * 0.25

        if p["y"] < 0:

            p["y"] = h - 1
            p["x"] = random.uniform(0, w - 1)

        put(
            canvas,
            int(p["x"]),
            int(p["y"]),
            p["symbol"],
            p["color"]
        )


def make_some_shapes(canvas, t):

    h = len(canvas)
    w = len(canvas[0])

    cx = w // 2
    cy = h // 2

    colors = [
        (245, 245, 245),
        (255, 130, 45),
        (75, 205, 220),
        (170, 110, 255),
        (95, 95, 105)
    ]

    for i in range(8):

        circle(
            canvas,
            cx,
            cy,
            3 + i * 2.5,
            colors[i % len(colors)],
            int(t * 30 + i * 15)
        )

    for i in range(650):

        angle = i * 0.09 + t * 0.5
        radius = i * 0.027

        x = int(cx + math.cos(angle) * radius)

        y = int(
            cy + math.sin(angle) * radius * 0.48
        )

        put(
            canvas,
            x,
            y,
            random.choice(".*+:"),
            colors[i % len(colors)]
        )

    for x in range(w):

        y = int(
            cy
            + math.sin(x * 0.09 + t * 2) * 7
            + math.cos(x * 0.035 - t * 1.5) * 4
        )

        put(canvas, x, y, "~", (75, 205, 220))

    for _ in range(10):

        x = random.randint(2, max(2, w - 3))
        y = random.randint(2, max(2, h - 3))

        size = random.randint(2, 7)
        c = random.choice(colors)

        shape = random.choice([
            "diamond",
            "triangle",
            "cross",
            "circle"
        ])

        if shape == "diamond":

            diamond(canvas, x, y, size, c)

        elif shape == "triangle":

            draw_line(
                canvas, x, y,
                x + size, y + size, c
            )

            draw_line(
                canvas,
                x + size, y + size,
                x - size, y + size,
                c
            )

            draw_line(
                canvas,
                x - size, y + size,
                x, y, c
            )

        elif shape == "cross":

            draw_line(
                canvas,
                x - size, y,
                x + size, y, c
            )

            draw_line(
                canvas,
                x, y - size,
                x, y + size, c
            )

        else:

            circle(
                canvas,
                x, y, size, c,
                int(t * 20)
            )


def keep_my_name(canvas, names, frame):

    h = len(canvas)
    w = len(canvas[0])

    if frame % 4 == 0 and len(names) < 45:

        if w > 10 and h > 2:

            x = random.randint(1, w - 9)
            y = random.randint(1, h - 1)

            names.append((
                x,
                y,
                random.choice([
                    (255, 130, 45),
                    (245, 245, 245),
                    (75, 205, 220)
                ])
            ))

    for x, y, c in names:

        for i, char in enumerate("z01309z"):

            put(
                canvas,
                x + i,
                y,
                char,
                c
            )


def render(canvas):

    output = [HOME]

    for row in canvas:

        last_color = None
        line_text = ""

        for char, c in row:

            if c != last_color:

                line_text += what_do_u_wanna(c)
                last_color = c

            line_text += char

        output.append(line_text + R + "\n")

    sys.stdout.write("".join(output))
    sys.stdout.flush()


def end_by_z01309z():

    fuck_u()

    w, h = wtf()

    title = "End Byz01309z"
    hint = "Press Ctrl + C to cancel"

    x = max(1, (w - len(title)) // 2)
    y = max(1, h // 2)

    sys.stdout.write(
        f"\033[{y};{x}H"
        + what_do_u_wanna((255, 130, 45))
        + title
        + R
    )

    sys.stdout.flush()

    time.sleep(2)

    hx = max(1, (w - len(hint)) // 2)

    sys.stdout.write(
        f"\033[{y + 2};{hx}H"
        + what_do_u_wanna((95, 95, 105))
        + hint
        + R
    )

    sys.stdout.flush()

    while True:
        time.sleep(1)


def what_a_mess():

    sys.stdout.write(HIDE)

    try:

        where_is_my_name()
        bro_is_loading()

        frame = 0
        particles = None
        last_size = None
        names = []

        art_duration = 7.0
        start = time.monotonic()

        while time.monotonic() - start < art_duration:

            w, h = wtf()

            w = max(40, w - 1)
            h = max(12, h - 2)

            if last_size != (w, h):

                particles = make_some_chaos(w, h)
                names = []
                last_size = (w, h)

            canvas = create_canvas(w, h)

            t = time.monotonic() - start

            move_the_dots(canvas, particles)
            make_some_shapes(canvas, t)
            keep_my_name(canvas, names, frame)

            render(canvas)

            frame += 1

            time.sleep(0.065)

        end_by_z01309z()

    except KeyboardInterrupt:
        pass

    finally:

        sys.stdout.write(R + SHOW)
        sys.stdout.flush()


if __name__ == "__main__":

    what_a_mess()
