import calendar
import datetime
import re
import functools

tmp = '/pic/tmp'

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


today = datetime.datetime.today()
print(today)

cal = calendar.TextCalendar(6)

# _base
base = cal.formatmonth(today.year, today.month).rstrip()
write(f'{tmp}/base.txt', base)

# today
d = today.day
dd = str(d).rjust(2, " ")
regex = f'{dd} |{dd}\n|{dd}$'
[today, today_r] = cut_out(base, regex)
write(f'{tmp}/today.txt', today)

# sunday
[sun, sun_r] = cut_out(base, 'Su ')
write(f'{tmp}/sun.txt', sun)

# saturday
[sat, sat_r] = cut_out(base, 'Sa')
write(f'{tmp}/sat.txt', sat)
