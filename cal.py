import calendar
import datetime
import re
import functools

def write(filename, value):
    with open(filename, mode='w') as f:
        f.write(value)


# conv_non_newlines_to_space
def conv(text):
    return "".join([char if char == '\n' else ' ' for char in text])


def cut_out(text, regex):
    r = re.search(regex, text)

    start = r.start()
    end = r.end()

    prev = text[:start]
    after = text[end:]

    return [conv(prev) + text[start:end] + conv(after), r]


# replace_to_space
def replace(text, r):
    start = r.start()
    end = r.end()

    size = end - start

    prev = text[:start]
    space = ' ' * size
    after = text[end:]

    return prev + space + after

# dir
t = 'tmp'

today = datetime.datetime.today()
cal = calendar.TextCalendar(6)

# _base
_base = cal.formatmonth(today.year, today.month).rstrip()

# today
d = today.day
dd = str(d).rjust(2, " ")
regex = f'{dd} |{dd}\n|{dd}$'
[today, today_r] = cut_out(_base, regex)
write(f'{t}/today.txt', today)

# sunday
[sun, sun_r] = cut_out(_base, 'Su ')
write(f'{t}/sun.txt', sun)

# saturday
[sat, sat_r] = cut_out(_base, 'Sa')
write(f'{t}/sat.txt', sat)

# base
base = functools.reduce(lambda x,y:replace(x, y), [today_r, sun_r, sat_r], _base)
write(f'{t}/base.txt', base)
