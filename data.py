#!/usr/bin/python3
'''Memo:
\\ppp{What}{Where}{Who}
\\ppps{What}
\\pppf{What}{Where}{Who}{Неч/Ч}
\\ppppp{What1}{Where1}{Who1}{What2}{Where2}{Who2}
\\blue \\green \\orange \\magenta \\yellow \\violet
'''

monday = [
"\\blue \\ppp{Численные методы в физике наноструктур}{4-30}{Колесников С.В.}",
"\\green \\ppp{История и методология физики}{ЦФА}{Трубачев О.О.}",
"\\blue \\ppp{Квантовая физика твердого тела}{4-30}{Клавсюк А.Л.}",
"\\blue \\ppp{Нано\\-структуры в биомед. иссл-х}{4-30}{Салецкий А.М.}",
"\\green \\ppp{Правоведение}{ЦФА}{Петраш И.П.}"
]
tuesday = ["\\pppmil", "\\pppmil", "\\pppmil", "\\pppmil", ""]
wednesday = ["", "", "", "\\yellow \\pppmfk", "\\yellow \\pppmfk"]
thursday = [
"\\blue \\ppp{Само\\-организация в сложных э/д системах}{Поляков П.А.}{4-30}",
# "\\blue \\ppp{Микромагнетизм}{Лукашева Е.В.}{4-28}",
"\\blue \\ppp{Введение в спинтронику}{4-30}{Цысарь К.М.}",
"\\orange \\ppp{Английский язык}{Линг. каб.}{Коваленко И.Ю.}",
"\\blue \\ppp{Оптика нано- и микроструктур}{4-30}{Колмычек И.А.}",
"\\blue \\ppp{ЭМР: \\break теория и практические применения}{Кокшаров Ю.А.}{4-30}"
# "\\blue \\ppp{Прикладная спектро\-скопия в экол. и биомед. исследованиях}{Пацаева С.В.}{4-28}"
]
friday = ["", "", "", "", ""]
saturday = ["", "", "", "", ""]

#############################################
numbers = [
"\ddd{1}{{\color{white}0}9:00}{10:35}",
"\ddd{2}{10:50}{12:25}",
"\ddd{3}{13:30}{15:05}",
"\ddd{4}{15:20}{16:55}",
"\ddd{5}{17:05}{18:40}"
]

out = open('data.tex', 'w')
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

out.close()
