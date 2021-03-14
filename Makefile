.PHONY: all clean purge

all: timetable.pdf

timetable.pdf: timetable.tex
	latexmk -lualatex timetable.tex

# delete temporary files
clean:
	latexmk -c

# delete everything except sources
purge:
	latexmk -C
