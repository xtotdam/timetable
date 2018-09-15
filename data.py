#!/usr/bin/python3

'''Memo:
\\ppp{What}{Where}{Who}
\\pppl{What}{Where}{Who}            % long name

\\ppps{What}

\\pppf{What}{Where}{Who}{Неч/Ч}
\\pppfl{What}{Where}{Who}{Неч/Ч}    % long name

\\ppppp{What1}{Where1}{Who1}{What2}{Where2}{Who2}

\\blue \\green \\orange \\magenta \\yellow \\violet
'''

monday = ["", "", "", "", ""]

tuesday = ["", "", "", "", ""]

wednesday = [
"\\magenta \\pppf{ВТЭК}{4-23}{Курилова М.В.}{Неч}", 
"\\magenta \\pppf{ВТЭК}{4-23}{Курилова М.В.}{Неч}", 
"",
"\\blue \\ppp{Магнетизм}{1-15а}{Грановский А.Б.}",
"", 
]

thursday = ["", "", "", "", ""]

friday = [
"", 
"\\blue \\ppp{DFT \\\\ (на перерыве)}{4-19а}{Колесников С.В.}", 
"\\magenta \\ppp{ВТЭК}{4-23}{Иванова О.С.}",
"\\magenta \\ppp{ВТЭК}{4-23}{Иванова О.С.}",
"\\blue \\ppp{DFT (на перерыве)}{4-19а}{Колесников С.В.}"
]

saturday = ["", "", "", "", ""]

#############################################
numbers = [
"\ddd{1}{{\color{white}0}9:00}{10:35}",
"\ddd{2}{10:50}{12:25}",
"\ddd{3}{13:30}{15:05}",
"\ddd{4}{15:20}{16:55}",
"\ddd{5}{17:05}{18:40}"
]

with open('data.tex', 'w', encoding='utf8') as out:
    out.write("%% This file is generated automatically. Do not edit it.\n\n")

    for i in range(5):
        a = monday[i] if monday[i] else "\\ppps{~}"
        b = tuesday[i] if tuesday[i] else "\\ppps{~}"
        c = wednesday[i] if wednesday[i] else "\\ppps{~}"
        d = thursday[i] if thursday[i] else "\\ppps{~}"
        e = friday[i] if friday[i] else "\\ppps{~}"
        f = saturday[i] if saturday[i] else "\\ppps{~}"
        if i == 1:
            end = ' \n\n\\\\ \\hline\\hline\n\n'
        elif i == 4:
            end = ''
        else:
            end = ' \n\n\\\\ \\hline\n\n'

        out.write(numbers[i] + ' &\n' +
                a + ' &\n' + b + ' &\n' + c + ' &\n' + d + ' &\n' + e + ' &\n' + f + end)
