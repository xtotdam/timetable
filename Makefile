.PHONY: all clean purge

all: timetable.pdf

timetable.pdf: timetable.tex
	latexmk -lualatex $<

timetable-example.pdf: timetable-example.tex
	latexmk -lualatex $<

# delete temporary files
clean:
	latexmk -c

# delete everything except sources
purge:
	latexmk -C
