# Timetable #

Эта маленькая штуковина генерирует расписание на неделю в формате `pdf`, используя `pdflatex`.

### Использование ###

```bash
make color 		# цветная версия
make wb			# черно-белая версия (хорошо для лазерного принтера)
make			# создает обе
make clean		# очищает временные файлы (кроме финальных)
make purge		# удаляет все, кроме исходников
```

### Типы клеток ###

Описаны в `defines.tex`. Обратный слеш `\` кодируется в строках как `\\`.

* `\ppp{What}{Where}{Who}` - обычная пара
* `\ppps{What}` - заглушка
* `\pppf{What}{Where}{Who}{eo}` - мигающая пара. Вместо `eo` необходимо подставить `Неч` либо `Ч` в зависимости от четности недели. `ётная неделя` подставится самостоятельно. 
* `\ppppp{What1}{Where1}{Who1}{What2}{Where2}{Who2}` - полноценно мигающие пары, когда пара занята и на четной, и на нечетной неделе. `1` отвечает за нечетные недели, `2` - за четные.

##### Сокращения #####

* `\pppnir   	--->   НИ/Р`
* `\pppmil   	--->   В/П`
* `\pppsprak   	--->   Практикум`
* `\pppmfk   	--->   МФК`

### Цвета ###

Описаны в `colors.tex`, `colors_laser.tex`. Добавляются до `\ppp?{?}?`, например`\blue \ppp?{?}?`.

* `\blue`
* `\green`
* `\orange`
* `\magenta`
* `\yellow`
* `\violet`

Цыет текста меняется с помощью обычного `{ \color{?}{ \ppp?{?}? }`.

В `colors_laser.tex` переопределяются на белый.

### Пример ###

`make example`

![Example](https://cloud.githubusercontent.com/assets/5108025/12861910/e16ae94e-cc77-11e5-818c-b085ffb1aaf6.png)
