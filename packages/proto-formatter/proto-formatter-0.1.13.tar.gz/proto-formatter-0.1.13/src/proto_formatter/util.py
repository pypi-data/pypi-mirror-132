import curses


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def remove_suffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text


def is_word(line, target_index):
    return line[target_index + 1].lower() not in ' \n' or line[target_index - 1].lower() not in ' \n'


def find_word_start_index(line, target_index):
    index = target_index - 1
    while index >= 0:
        if line[index].lower() in ' \n':
            return index
        index = index - 1
    return target_index


def find_word_end_index(line, target_index):
    index = target_index + 1
    while True:
        if line[index].lower() in ' \n':
            return index
        index = index + 1
    return target_index


def to_lines(line, length):
    lines = []
    while True:
        if len(line) <= length:
            lines.append(line)
            break

        if not is_word(line, length - 1):
            lines.append(line[:length - 1])
            sub_line = line[:length - 1]
            line = line[length - 1:].strip()
        else:
            index = find_word_start_index(line, length - 1)
            sub_line = line[:index]
            line = line[index:].strip()

        lines.append(sub_line)

    return lines


def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def view_curses_colors():
    def print_color(stdscr):
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)
        try:
            for i in range(0, 255):
                stdscr.addstr(str(i) + " ", curses.color_pair(i))
        except curses.ERR:
            # End of screen reached
            pass
        stdscr.getch()

    curses.wrapper(print_color)
