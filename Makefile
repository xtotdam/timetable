LATEX       = pdflatex
BASH        = bash -c
ECHO        = echo
RM          = rm -rfv
# TMP_SUFFS   = pdf aux bbl blg log dvi ps eps out toc lof lot dep
ALL_SUFFS   = pdf aux log out
TMP_SUFFS   = aux log out


ifeq ($(OS),Windows_NT)
	PYTHON3 = C:\Miniconda3\python.exe
else
	PYTHON3 = python3
endif

.PHONY: all clean purge color wb example

all: color wb

data.tex: data.py
	${PYTHON3} data.py

timetable.pdf: data.tex timetable.tex defines.tex colors.tex
	${LATEX} -quiet timetable
	( grep Rerun timetable.log && ${LATEX} timetable ) || echo "Done."
	( grep Rerun timetable.log && ${LATEX} timetable ) || echo "Done."

timetable-wb.pdf: data.tex timetable-wb.tex defines.tex colors_laser.tex
	${LATEX} -quiet timetable-wb
	( grep Rerun timetable-wb.log && ${LATEX} timetable-wb ) || echo "Done."
	( grep Rerun timetable-wb.log && ${LATEX} timetable-wb ) || echo "Done."

timetable-example.pdf: timetable-example.tex defines.tex colors.tex
	${LATEX} timetable-example
	( grep Rerun timetable-example.log && ${LATEX} timetable-example ) || echo "Done."
	( grep Rerun timetable-example.log && ${LATEX} timetable-example ) || echo "Done."

color: timetable.pdf

wb: timetable-wb.pdf

example: timetable-example.pdf

# delete temporary files
clean:
	${RM} $(foreach suff, ${TMP_SUFFS}, timetable.${suff})
	${RM} $(foreach suff, ${TMP_SUFFS}, timetable-wb.${suff})
	${RM} $(foreach suff, ${TMP_SUFFS}, timetable-example.${suff})

# delete everything except sources
purge: clean
	${RM} data.tex
	${RM} $(foreach suff, ${ALL_SUFFS}, timetable.${suff})
	${RM} $(foreach suff, ${ALL_SUFFS}, timetable-wb.${suff})
	${RM} $(foreach suff, ${ALL_SUFFS}, timetable-example.${suff})
