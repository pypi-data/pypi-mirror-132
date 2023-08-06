"""
MIT License

Copyright (c) 2021 Ali Sever

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random
from string import ascii_uppercase
from math import sqrt, degrees, asin, atan, floor


def multiple_choice(question: str, choices: list, correct, onepar=True,
                    reorder=True):
    """Takes question, choices(which contains answer), answer and returns
    a multiple choice question and the answer"""
    layout = ""
    if onepar:
        layout = 'onepar'
    choices_list = []
    if reorder:
        random.shuffle(choices)
    letter = ascii_uppercase[choices.index(correct)]
    for choice in choices:
        choices_list.append(f'\\choice {choice}\n')
    full_question = ''.join(
        [question, f'\n\n\\begin{{{layout}choices}}\n'] +
        choices_list + [f'\\end{{{layout}choices}}'])
    return [full_question, f'{letter}. {correct}']


def dollar(x):
    return '$' + str(x) + '$'


def ordinal(n):
    return '%d%s' % (n, 'tsnrhtdd'[(n // 10 % 10 != 1)
                                   * (n % 10 < 4) * n % 10::4])


def is_prime(n: int):
    if n <= 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


def nth_prime(n):
    num = 1
    for _ in range(n):
        num = num + 1
        while not is_prime(num):
            num = num + 1
    return num


def factors(n):
    my_list = []
    for i in range(1, n + 1):
        if not n % i:
            my_list.append(i)
    return my_list


def prime_factors(n):
    return [x for x in factors(n) if is_prime(x)]


def gcd(m: int, n: int, *args: int):
    if args:
        return gcd(*(gcd(m, n),) + args)
    m, n = abs(m), abs(n)
    if m < n:
        (m, n) = (n, m)
    if n == 0:
        return m
    if (m % n) == 0:
        return n
    else:
        return gcd(n, m % n)


def cast_int(a):
    return a if a % 1 else int(a)


def median(num_list: list):
    n = len(num_list)
    sorted_list = sorted(num_list)
    if n % 2:
        return sorted_list[(n - 1) // 2]
    else:
        return (sorted_list[n // 2] + sorted_list[n // 2 - 1]) / 2


def interquartile_range(num_list: list):
    n = len(num_list)
    sorted_list = sorted(num_list)
    if n % 2:
        list_1 = sorted_list[0:(n - 3) // 2]
        list_2 = sorted_list[(n + 1) // 2:]
    else:
        list_1 = sorted_list[0:n // 2 - 1]
        list_2 = sorted_list[n // 2 + 1:]
    return median(list_2) - median(list_1)


def round_sig(a, k=1):
    """Round a to k significant digits and remove trailing zeros."""
    result = float(f'{a + 1e-15:.{k}g}')
    return cast_int(result)


def frac_simplify(a, b):
    if b < 0:
        a = - a
        b = - b
    return a // gcd(a, b), b // gcd(a, b)


def latex_frac(a, b):
    return r'\frac{%s}{%s}' % (str(a), str(b))


def latex_frac_simplify(a, b):
    m, n = frac_simplify(a, b)
    if n == 1:
        return str(m)
    else:
        return latex_frac(m, n)


def fraction_addition(a, b, c, d):
    numerator = a * d + b * c
    denominator = b * d
    return frac_simplify(numerator, denominator)


def fraction_subtraction(a, b, c, d):
    numerator = a * d - b * c
    denominator = b * d
    return frac_simplify(numerator, denominator)


def sqrt_simplify(n: int):
    if n < 0:
        raise ValueError
    i = 2
    a = 1
    while i * i <= n:
        if n % (i * i) == 0:
            a *= i
            n //= i * i
        else:
            i = i + 1
    return a, n


def latex_sqrt_simplify(n):
    a, b = sqrt_simplify(n)
    if b == 0:
        return '$0$'
    elif b == 1:
        return f'${a}$'
    elif a == 1:
        return f'$\\sqrt{{{b}}}$'
    else:
        return f'${a}\\sqrt{{{b}}}$'


def triangle_area(a, b, c):
    area = - 1 / 2 * (a[0] * (b[1] - c[1]) +
                      b[0] * (c[1] - a[1]) +
                      c[0] * (a[1] - b[1]))
    return area


def valid_metric(unit):
    prefixes = ['m', 'c', 'd', '', 'da', 'h', 'k']
    base_units = ['m', 'g', 'l']
    return all([unit[-1] in base_units, unit[0:-1] in prefixes])


def convert_measurement(number, unit_in, unit_out):
    prefixes = {'m': 0.001, 'c': 0.01, 'd': 0.1, '': 1, 'da': 10,
                'h': 100, 'k': 1000}
    for unit in [unit_in, unit_out]:
        if not valid_metric(unit):
            raise NameError(f"{unit} is not a valid unit.")
    if unit_in[-1] != unit_out[-1]:
        raise TypeError("Units are not of the same type.")
    else:
        return number * prefixes[unit_in[0:-1]] / prefixes[unit_out[0:-1]]


def convert_imperial(unit_in, unit_out, number=1):
    if unit_in in ['inch', 'inches']:
        return convert_measurement(number * 2.5, 'cm', unit_out)
    elif unit_in in ['lb', 'lbs', 'pounds']:
        return convert_measurement(number / 2.2, 'kg', unit_out)
    elif unit_in in ['pint', 'pints']:
        return convert_measurement(number * 568, 'ml', unit_out)
    elif unit_in in ['mile', 'miles']:
        return convert_measurement(number * 1.6, 'km', unit_out)
    elif unit_out in ['inch', 'inches']:
        return convert_measurement(number / 2.5, unit_in, 'cm')
    elif unit_out in ['lb', 'lbs', 'pounds']:
        return convert_measurement(number * 2.2, unit_in, 'kg')
    elif unit_out in ['pint', 'pints']:
        return convert_measurement(number / 568, unit_in, 'ml')
    elif unit_out in ['mile', 'miles']:
        return convert_measurement(number / 1.6, unit_in, 'km')
    else:
        raise NameError("Given units are invalid.")


def time_unit_converter(number, unit_in, unit_out):
    def unit_reader(arg: str):
        units = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']
        for unit in units:
            if unit in arg.lower():
                return unit
        else:
            raise ValueError("Invalid unit: ", arg)

    unit_in = unit_reader(unit_in)
    unit_out = unit_reader(unit_out)

    if unit_in == 'year':
        if unit_out == 'month':
            number = number * 12
        elif unit_out == 'week':
            number = number * 52
        elif unit_out == 'day':
            number = number * 365
        else:
            raise ValueError("Conversion between inputs not valid.")
    elif unit_in == 'month':
        if unit_out == 'year':
            number = number / 12
        else:
            raise ValueError("Conversion between inputs not valid.")
    else:
        if unit_in == 'week' and unit_out == 'year':
            number = number / 52
        elif unit_in == 'day' and unit_out == 'year':
            number = number / 365
        elif unit_out in ['month', 'year']:
            raise ValueError("Conversion between inputs not valid.")
        else:
            ratios = {'second': 1, 'minute': 60, 'hour': 3600, 'day': 86400,
                      'week': 604800}
            number = number * ratios[unit_in] / ratios[unit_out]
    if number != 1:
        unit_out += "s"
    return f"{number if number % 1 else int(number)} {unit_out}"


def time_to_words(h: int, m: int):
    if h not in range(13):
        raise ValueError("Hour invalid.")
    nums = ['twelve', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen',
            'fourteen', 'quarter', 'sixteen',
            'seventeen', 'eighteen', 'nineteen',
            'twenty', 'twenty one', 'twenty two',
            'twenty three', 'twenty four',
            'twenty five', 'twenty six', 'twenty seven',
            'twenty eight', 'twenty nine', 'half']

    if m == 0:
        return f"{nums[h]} o'clock"
    elif 0 < m <= 30:
        return f"{nums[m]} past {nums[h]}"
    elif 30 < m < 60:
        return f"{nums[60 - m]} to {nums[h % 12 + 1]}"
    else:
        raise ValueError("Minute invalid.")


def minutes_to_time(minutes: int):
    if not 0 <= minutes < 1440:
        raise ValueError("Minutes must be between 0 and 1439.")
    h = str(minutes // 60)
    m = str(minutes % 60)
    return '0' * (2 - len(h)) + h + ':' + '0' * (2 - len(m)) + m


def analogue_clock(hour, minute, center=True):
    hour_angle = (90 - 30 * (hour % 12)) % 360 - 0.5 * minute
    minute_angle = (90 - 6 * minute) % 360
    clock = r'''
            \begin{tikzpicture}[line cap=rect, line width=3pt]
            \filldraw [fill=white] (0,0) circle [radius=1.3cm];
            \foreach \angle [count=\xi] in {60,30,...,-270}
              {
                \draw[line width=1pt] (\angle:1.15cm) -- (\angle:1.3cm);
                \node[font=\large] at (\angle:0.9cm) {\textsf{\xi}};
              }
            \foreach \angle in {0,90,180,270}
            \draw[line width=1.5pt] (\angle:1.1cm) -- (\angle:1.3cm);
            \draw (0,0) -- (%f:0.65cm);
            \draw (0,0) -- (%f:0.9cm);
            \end{tikzpicture}
            ''' % (hour_angle, minute_angle)
    if center:
        clock = r'\begin{center}' + '\n' + clock + '\n' + r'\end{center}'
    return clock


def num_line(denominator, extra='', length=6, labelled=False, start=0, end=1):
    if labelled:
        label = r' node[below] {$\frac{\x}{%d}$}' % denominator
    else:
        label = ''
    model = r'''
            \begin{tikzpicture}[font=\Large]
            \draw[line width = 1pt] (0,0) -- (%f,0);
            \foreach \x in {0,%f}
              {\draw [shift={(\x, 0)}, color=black, line width = 1pt] 
              (0pt,6pt) -- (0pt,-6pt);}
            \foreach \x in {1,...,%d} 
              {\draw [shift={(\x * %f/%d,0)}, color=black] 
                (0pt,5pt) -- (0pt,-5pt)%s;}
            \draw (0, -6pt) node[below]{%s};
            \draw (%f, -6pt) node[below]{%s};
            %s
            \end{tikzpicture}
            ''' % (length, length, denominator - 1, length, denominator, label,
                   start, length, end, extra)
    return model


def draw_angle(x_angle, y_angle=0, radius=4, shaded_radius=1):
    model = r'''
            \begin{tikzpicture}
            \draw
            (%f:%fcm) coordinate (a)
            -- (0:0) coordinate (b)
            -- (%f:%fcm) coordinate (c)
            pic[draw=blue!50!black, fill=blue!20, angle eccentricity=1.2, 
                angle radius=%fcm]
            {angle=c--b--a};
            \end{tikzpicture}
            ''' % (x_angle, radius, y_angle, radius, shaded_radius)
    return model


def draw_table(data: list, centered=True):
    num_columns = len(data[0])
    if centered is False:
        columns = ' | '.join('l' * num_columns)
    else:
        columns = ' | '.join('c' * num_columns)
    for row in data:
        if len(row) != num_columns:
            raise ValueError("Rows are not of fixed length.")
    table = r''' 
            \begin{center}
            \begin{tabular}{||%s||}
            \hline
            %s \\ [0.5ex]
            \hline
    ''' % (columns, ' & '.join(data[0]))
    for row in data[1:]:
        row_tex = r'''
                  %s \\
                  \hline
                  ''' % (' & '.join(row))
        table += row_tex
    table += r'''
    \end{tabular}
    \end{center}
    '''
    return table


def draw_triangle(size=1.5, draw='yellow', fill='yellow', rotate=90):
    triangle = r'''
               \tikz \node[isosceles triangle, minimum size=%sem, 
               text opacity=0, rotate=%s, draw=%s,fill=%s] (T) {};
               ''' % (size, rotate, draw, fill)
    return triangle


def draw_square(size=2, draw='red', fill='red', rotate=0):
    square = r'''
             \tikz \node[regular polygon, regular polygon sides=4, 
             text opacity=0, minimum size=%sem, 
             draw=%s,fill=%s, rotate=%s] (S) {};
             ''' % (size, draw, fill, rotate)
    return square


def draw_circle(size=1.5, fill='blue', draw='blue'):
    circle = r'''
             \tikz \node[circle, text opacity=0, minimum size=%sem,
              draw=%s,fill=%s] (c) {};
             ''' % (size, draw, fill)
    return circle


def draw_semi_circle(radius=1.5):
    shape = r'''
            \begin{tikzpicture} 
            [baseline=(current bounding box.north)] 
            \draw (-%s,0) -- (%s,0) arc(0:180:%s) --cycle; 
            \end{tikzpicture}
            ''' % (radius, radius, radius)
    return shape


def draw_regular_polygon(sides, size=2, colour=""):
    fill = '=%s, fill=%s' % (colour, colour) if colour != "" else ''
    shape = r'''
            \begin{tikzpicture} 
            \node[regular polygon, regular polygon sides=%s, minimum size=%scm, 
            draw%s] at (0, 0) {};
            \end{tikzpicture}
            ''' % (sides, size, fill)
    return shape


def ruler(length=7, additional='', unit='cm'):
    scale = (length - 0.2) / 10
    if unit in ['m', 'metres', 'meters']:
        text_scale = 0.5
        power = 10
    else:
        text_scale = 0.7
        power = 1
    draw = r'''
           \begin{tikzpicture}
           \draw (-0.2,0) rectangle (%f,1);
           %% lower divisions
           \foreach \x in {0,1,...,10}{
           \draw (\x * %f,1) -- (\x * %f,0.75)node[below,scale=%f] 
             {\pgfmathparse{%f *\x} \pgfmathprintnumber{\pgfmathresult}};
           }
           \foreach \x in {0.5,1,...,9.5}{
           \draw (\x * %f,1) -- (\x * %f,0.8);
           }
           ''' % (length, scale, scale, text_scale, power, scale, scale)

    if unit not in ['mm', 'millimetres', 'millimeters']:
        draw += r'''
                \foreach \x in {0.1,0.2,...,9.9}
                {\draw (\x * %f,1) -- (\x * %f,0.875);}''' % (scale, scale)
        tag = 'cm'
    else:
        tag = 'mm'

    draw += r'\draw (-0.2, 0.125) node[right, scale = 0.7]{%s};' \
            r'%s \end{tikzpicture}' % (tag, additional)
    return draw


def draw_random_shape(polygon, curves=2, sides=4):
    width = 3
    check = [3, 4]
    my_list = "\\ ".join([str(j) for j in check])
    if sides not in check:
        raise NameError(f"Sides must be either {my_list}")
    sides = sides

    if polygon is True:
        n = 1
    elif polygon is False:
        n = 0
    else:
        n = random.randint(0, 1)

    if sides == 3:
        parabola_line = [["--", "--", "parabola"], ["--", "--", "--"]][n]
    else:
        if curves == 3:
            parabola = ["parabola", 'parabola', "parabola"]
        elif curves == 1:
            parabola = ["--", '--', "parabola"]
        else:
            parabola = ["parabola", '--', "parabola"]
        parabola_line = [parabola, ["--", "--", "--"]][n]
        random.shuffle(parabola_line)

    x = []
    while len(x) < 3:
        triangle = [[3, 2, 1], [1, 2, 3], [1, 1, 1], [2, 2, 2], [3, 3, 3]]
        if sides == 3:
            x = random.choice(triangle)
        else:
            x_1 = random.randint(1, width)
            x_2 = random.randint(1, width)
            if x_2 == 1:
                x_3 = 1
            else:
                x_3 = random.randint(1, 3)
            my_list = [x_1, x_2, x_3]
            if my_list not in triangle:
                x = my_list
    flip = random.choices(["-", ""], k=2)
    shape = r'''
            \begin{tikzpicture} 
            \draw (0,0) -- (%s%s,0) %s (%s%s,%s1) %s (%s%s,%s2) %s (0,0); 
            \end{tikzpicture}
            ''' % (flip[0], x[0], parabola_line[0],
                   flip[0], x[1], flip[1], parabola_line[1],
                   flip[0], x[2], flip[1], parabola_line[2])
    return shape


def draw_two_lines(size=2, rotate=0, perpendicular=False, parallel=False):
    length = 3
    if perpendicular is True and parallel is True:
        raise NameError("Lines cannot be both perpendicular and parallel.")

    x_0 = random.randint(0, 3)
    if perpendicular is True:
        y_0 = -random.randint(2, 4)
        x = [x_0, x_0 + length, random.randint(x_0, x_0 + length)]
        y = [y_0, y_0, random.randint(y_0 - length, y_0)]
        x.append(x[2])
        y.append(y[1] + length)
    elif parallel is True:
        y_0 = random.randint(1, 3)
        x = [x_0, x_0 + length, random.randint(1, 3)]
        y = [0, 0, y_0, y_0]
        x.append(x[2] + length)
    else:
        x = []
        y = [0, length, 0, length]
        while len(x) < 4:
            nums = random.choices([0, 1, 2, 3], k=4)
            if nums[0] == nums[1] == nums[2] == nums[3]:
                nums[0] = (nums[0] + 1) % 4
            theta = []
            for i in range(2):
                opp = y[1 + 2 * i] - y[0 + 2 * i]
                adj = nums[1 + 2 * i] - nums[0 + 2 * i]
                h = sqrt(opp ** 2 + adj ** 2)
                if nums[0 + 2 * i] == nums[1 + 2 * i]:
                    theta.append(degrees(asin(opp / h)))
                else:
                    theta.append(degrees(atan(opp / adj)))
            delta = 180 - abs(theta[0]) - abs(theta[1])
            check_1 = [[1, 3, 3, 1], [0, 2, 2, 0]]
            check_2 = ([i for i in range(65, 115)]
                       + [j for j in range(0, 9)]
                       + [k for k in range(70, 181)]
                       + [37])
            if round(abs(delta)) not in check_2 and nums not in check_1:
                x = nums

    x = [size * i / 3 for i in x]
    y = [size * j / 3 for j in y]
    lines = r'''
    \draw[rotate=%s] (%s,%s) -- (%s,%s); 
    \draw[rotate=%s] (%s,%s) -- (%s,%s);
    ''' % (rotate, x[0], y[0], x[1], y[1], rotate, x[2], y[2], x[3], y[3])
    return r'\begin{tikzpicture} %s \end{tikzpicture}' % lines


def bar_chart(data: list, horizontal=False, fill='blue', size=(5, 5), label='',
              sym_axis=True, bar_width=15, axis_adj='', axis_step='',
              additional=''):
    coordinates = ''
    tags = []
    if horizontal is True:
        n = 0
    else:
        n = 1
    m = (n + 1) % 2
    height, width = size[0], size[1]
    for i in range(len(data)):
        tags.append(str(data[i][0]))
        coordinates += r' (%s,%s) ' % (data[i][m], data[i][n])
    tags = ','.join(tags)
    x_or_y = ["x", "y"]

    if sym_axis is True:
        sym_coord = r"symbolic %s coords={%s}, %stick=data," \
                    % (x_or_y[m], tags, x_or_y[m])
    else:
        sym_coord = ""
    if axis_adj != '':
        additional_axis = r', %s' % axis_adj
    else:
        additional_axis = ''
    if axis_step != '':
        increments = r"%stick={0, %s,..., %s * 100}," % (x_or_y[n],
                                                         axis_step,
                                                         axis_step)
    else:
        increments = ''

    chart = r'''
        \begin{tikzpicture}
        \begin{axis} [%sbar, %s bar width=%fpt, height=%fcm, width=%fcm, %s
                      %slabel=%s %s]
        \addplot[%sbar, fill=%s] coordinates { %s };
        %s
        \end{axis}
        \end{tikzpicture}
        ''' % (x_or_y[n], sym_coord, bar_width, height, width,
               increments, x_or_y[n], label, additional_axis,
               x_or_y[n], fill, coordinates, additional)
    return chart


def draw_tally(num, colour='black'):
    thickness = 0.4
    lines = [
        r'\draw[line width=%smm, %s ] (0,0) -- (0,1em);'
        % (thickness, colour),
        r'\draw[line width=%smm, %s ] (0.1,0) -- (0.1,1em);'
        % (thickness, colour),
        r'\draw[line width=%smm, %s ] (0.2,0) -- (0.2,1em);'
        % (thickness, colour),
        r'\draw[line width=%smm, %s ] (0.3,0) -- (0.3,1em);'
        % (thickness, colour),
        r'\draw[line width=%smm, %s ] (0.3,0) -- (0,1em);'
        % (thickness, colour)
    ]
    draw_integer = ' '.join(lines)
    a = floor(num / 5)
    drawing_list = []
    for i in range(a):
        drawing_list.append(r'\begin{tikzpicture} %s \end{tikzpicture}'
                            % draw_integer)
    b = num % 5
    if b > 0:
        non_int = ''.join(lines[0:b])
        drawing_list.append(r'\begin{tikzpicture} %s \end{tikzpicture}'
                            % non_int)
    drawing = r' \ '.join(drawing_list)
    return drawing


def draw_line_graph(data: list, sym_axis=True, x_label='', y_label='',
                    scale=0.7, legend='', axis_adj='', colour='blue',
                    grid=True, additional='', title=''):
    scale = scale
    x_label = x_label
    y_label = y_label

    coordinates = ''
    x_coord = []

    for i in range(len(data)):
        x_coord.append(str(data[i][0]))
        coordinates += r' (%s,%s) ' % (data[i][0], data[i][1])
    x_coord = ','.join(x_coord)

    if legend == '':
        legend_text = ''
    else:
        legend_text = r'\legend{%s}' % legend
    if sym_axis is True:
        sym_x_coord = r'symbolic x coords={%s},' % x_coord
    else:
        sym_x_coord = ''
    if axis_adj != '':
        additional_axis = r',%s' % axis_adj
    else:
        additional_axis = ''
    if grid is True:
        grid_lines = r'true'
    else:
        grid_lines = r'false'

    model = r'''
    \begin{tikzpicture}
    \begin{axis}[ scale = %s,
    xlabel = %s, 
    ylabel = %s,
    width = 10cm, height = 7cm,
    %s xtick=data, ymajorgrids=%s, title = %s,
    legend style = {at = {(0.0, .91)}, anchor = west}%s]
    \addplot[color = %s, mark = *] coordinates
    {
    %s
    };
    %s
    %s
    \end{axis}
    \end{tikzpicture}
    ''' % (scale, x_label, y_label, sym_x_coord, grid_lines, title,
           additional_axis, colour, coordinates, additional, legend_text)
    return model


def draw_thermometer(temperature, scale=0.9, text_size="small",
                     show_celsius=True, show_fahrenheit=False,
                     half_increments=False, horizontal=True,
                     length=1, width=1):
    fill_temp = temperature
    font_size = r"\%s" % text_size if text_size[0:1] != "\\" else text_size

    if show_celsius is True and show_fahrenheit is True:
        label = ["Celsius", "Fahrenheit"]
    else:
        label = ["", ""]

    if horizontal is True:
        rotate_text, rotate_label, rotate = 300, 0, 90
        x_or_y = "x"
        scale_length = r"xscale=%s" % length
        scale_width = r"yscale=-%s" % width
    else:
        rotate_text, rotate_label, rotate = 0, 0, 0
        x_or_y = "y"
        scale_length = r"yscale=-%s" % length
        scale_width = r"xscale=%s" % width

    model = r'''
    \begin{tikzpicture}[y=0.5pt, x=0.5pt, %s, %s,
                        inner sep=0pt, outer sep=0pt, scale=%s, rotate=%s]
    \def\thermopath{
      (280.0313,169.3125) .. 
      controls (263.9888,169.3125) and (250.6461,179.3446) ..
      (247.8125,192.5625) -- 
      (247.3438,563.7500) .. 
      controls (235.7346,573.2243) and (228.3438,587.6282) ..
      (228.3438,603.7813) .. 
      controls (228.3438,632.3161) and (251.4651,655.4688) ..
      (280.0000,655.4688) .. 
      controls (308.5349,655.4688) and (331.6563,632.3161) ..
      (331.6563,603.7813) .. 
      controls (331.6563,587.6282) and (324.2654,573.2243) ..
      (312.6563,563.7500) -- 
      (312.2500,192.5625) .. 
      controls (309.4164,179.3446) and (296.0737,169.3125) .. 
      (280.0313,169.3125) -- cycle
     }
    \path[miter limit=4,even odd rule,fill=gray!20]
        \thermopath;
    ''' % (scale_length, scale_width, scale, rotate)

    model += r'''
    \def\tempincelsius{%s}
    \begin{scope}
        \clip \thermopath;
        \fill[red] (210,{560- 3.7*\tempincelsius}) -- ++(140,0)
            -- (350, 690) -- (210, 690) -- cycle;
    \end{scope}
    ''' % fill_temp

    model += r'''
    \path[draw=black,miter limit=4,even odd rule,line width=2.5pt]
        \thermopath;'''
    if show_celsius is True:
        model += r'''
        \foreach \y/\x in {190/100,
                           227/90,
                           264/80,
                           301/70,
                           338/60,
                           375/50,
                           412/40,
                           449/30,
                           486/20,
                           523/10,
                           560/0%
                           }'''
        model += r'''
            {\draw (222,\y)--(198,\y) node[left, font=%s, rotate=%s](\x)
            {\x\textdegree C~};}''' % (font_size, rotate_text)
    if show_celsius is True and half_increments is True:
        model += r'''
        \foreach \y in {208.5,
                        245.5,
                        282.5,
                        319.5,
                        356.5,
                        393.5,
                        430.5,
                        467.5,
                        504.5,
                        541.5}'''
        model += r'''{\draw (217,\y)--(203,\y);}'''
    if show_fahrenheit is True:
        model += r'''
    \foreach \u/\v in {189.999/212,
                       231.111/192,
                       272.222/172,
                       313.333/152,
                       354.444/132,
                       395.555/112,
                       436.666/92,
                       477.777/72,
                       518.888/52,
                       559.999/32%
                       }'''
        model += r'''
        {\draw (338,\u)--(362,\u) node[right, font=%s, rotate=%s](\v)
        {\v\textdegree F};}''' % (font_size, rotate_text)
    if show_fahrenheit is True and half_increments is True:
        model += r'''
        \foreach \u in {231.111,
                        272.222,
                        313.333,
                        354.444,
                        395.555,
                        436.666,
                        477.777,
                        518.888,
                        559.999}'''
        model += r'''{\draw (343,\u - 41.111/2)--(357,\u - 41.111/2);}'''
    if show_celsius is True:
        model += r'''
        \draw (210,190)node[%sshift=4ex, red, font=%s, rotate=%s] {%s} 
        --(210,560) ;''' % (x_or_y, font_size, rotate_label, label[0])
    if show_fahrenheit is True:
        model += r'''
        \draw (350,190)node[%sshift=4ex, blue, font=%s, rotate=%s] {%s}
        --(350,560);''' % (x_or_y, font_size, rotate_label, label[1])
    model += r"\end{tikzpicture}"
    return model


def random_place_symbols(n, text_size='Large'):
    names = ["Coffee Shop", "Post Office", "Barbers", "Bank", "Bicycle Shop",
             "Football Stadium", "Florist", "Airport", "Hospital"]
    latex_commands = [r"\textcolor{brown!80!black}{\textbf{\Coffeecup}}",
                      r"\textcolor{blue!30!darkgray}{\Letter}",
                      r"\textcolor{red!85!black}{\LeftScissors}",
                      r"\textcolor{green!80!black}{\textbf{\textsterling}}",
                      r"\textcolor{blue!65!lightgray}{\textbf{\Bicycle}}",
                      r"\Football",
                      r"\textcolor{green!70!black}{\textbf{\FiveFlowerOpen}}",
                      r"\Plane",
                      r"\textcolor{red}{\textbf{\Plus}}"]
    k = random.sample(range(0, len(names)), k=n)
    symbol_list = [
        [names[i], r"{\%s %s}" % (text_size, latex_commands[i])] for i in k]
    return symbol_list


def venn_diagram(set_a: list, set_b: list, intersect: list, labels=None,
                 scale=1):
    if len(set_a) > 9 or len(set_b) > 9:
        raise TypeError("Maximum number of data entries in "
                        "set_a or set_b is 9.")
    if len(intersect) > 5:
        raise TypeError("Maximum number of entries in intersect is 5.")

    circle = r'''\phantom{\tikz \node[circle, text opacity=0, minimum size=1em, 
                 draw=white,fill=white] (c) {};}'''

    set_a += [circle] * (9 - len(set_a))
    random.shuffle(set_a)
    a = r' \\ '.join([' & '.join(set_a[i:i + 3]) for i in range(0, 9, 3)])

    set_b += [circle] * (9 - len(set_b))
    random.shuffle(set_b)
    b = r' \\ '.join([' & '.join(set_b[i:i + 3]) for i in range(0, 9, 3)])

    intersect += [circle] * (5 - len(intersect))
    random.shuffle(intersect)
    text_intersect = r'''
    {\arraycolsep=2pt$\begin{array}{lll} 
    & %s & \\ %s \\ & %s & \end{array}$}
    ''' % (intersect[0], ' & '.join(intersect[1:4]), intersect[4])

    if labels is None:
        labels = ["Set A", "Set B"]
    diagram = r'''
    \begin{tikzpicture}[thick,
        set/.style = {ellipse, minimum height=4cm, 
                      minimum width=4.7cm, scale=%s}]
    \node[set,fill=white,label={93:%s}] (A) at (0,0) {};
    \node[set,fill=white,label={87:%s}] (B) at (2.7,0) {};

    \draw (0,0) 
    node[ellipse, minimum height=4cm, minimum width=4.7cm,draw, scale=%s] {};
    \draw (2.7,0) 
    node[ellipse, minimum height=4cm, minimum width=4.7cm,draw, scale=%s] {};

    \node[left,black, xshift=1.2ex] at (A.center) {{\arraycolsep=2pt$\begin{array}{ccc} %s \end{array}$}};
    \node[right, black, xshift=-1.2ex] at (B.center) {{\arraycolsep=2pt$\begin{array}{ccc} %s \end{array}$}};
    \node at (1.35,0)  {%s};
    \end{tikzpicture}
    ''' % (scale, labels[0], labels[1], scale, scale, a, b, text_intersect)
    return diagram
