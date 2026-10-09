colors = [
    ("Black", 30),       ("DarkBlue", 34),    ("DarkGreen", 32),   ("DarkCyan", 36),
    ("DarkRed", 31),     ("DarkMagenta", 35), ("DarkYellow", 33),  ("Gray", 37),
    ("DarkGray", 90),    ("Blue", 94),        ("Green", 92),       ("Cyan", 96),
    ("Red", 91),         ("Magenta", 95),     ("Yellow", 93),      ("White", 97)
]

for name, fg in colors:
    bg = fg + 10
    col1 = f"{name:<15}"
    col2 = f"\033[{fg}m{name:<20}\033[0m"
    col3 = f"\033[{bg}m{name:<20}\033[0m"
    print(f"{col1}{col2}{col3}")
