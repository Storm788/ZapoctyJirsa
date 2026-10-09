colors = [
    ("Black",       30, 40),
    ("DarkBlue",    34, 44),
    ("DarkGreen",   32, 42),
    ("DarkCyan",    36, 46),
    ("DarkRed",     31, 41),
    ("DarkMagenta", 35, 45),
    ("DarkYellow",  33, 43),
    ("Gray",        37, 47),
    ("DarkGray",    90, 100),
    ("Blue",        94, 104),
    ("Green",       92, 102),
    ("Cyan",        96, 106),
    ("Red",         91, 101),
    ("Magenta",     95, 105),
    ("Yellow",      93, 103),
    ("White",       97, 107),
]

reset = "\033[0m"

for name, fg, bg in colors:
    column1 = f"{name:<15}"
    column2 = f"\033[{fg}m{name:<20}{reset}"
    column3 = f"\033[{bg}m{name:<20}{reset}"

    print(f"{column1}{column2}{column3}")