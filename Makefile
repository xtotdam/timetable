LATEX       = pdflatex
BASH        = bash -c
ECHO        = echo
RM          = rm -rfv
# TMP_SUFFS   = pdf aux bbl blg log dvi ps eps out toc lof lot dep 
ALL_SUFFS   = pdf aux log out
TMP_SUFFS   = aux log out

.PHONY: all clean purge color wb

all: timetable.pdf timetable-wb.pdf

data.tex: data.py
	python3 data.py

timetable.pdf: data.tex timetable.tex defines.tex colors.tex
	${LATEX} timetable
	( grep Rerun timetable.log && ${LATEX} timetable ) || echo "Done."
	( grep Rerun timetable.log && ${LATEX} timetable ) || echo "Done."

timetable-wb.pdf: data.tex timetable-wb.tex defines.tex colors_laser.tex
	${LATEX} timetable-wb
	( grep Rerun timetable-wb.log && ${LATEX} timetable-wb ) || echo "Done."
	( grep Rerun timetable-wb.log && ${LATEX} timetable-wb ) || echo "Done."

color: timetable.pdf
	
wb: timetable-wb.pdf

# delete temporary files
clean:
	${RM} $(foreach suff, ${TMP_SUFFS}, timetable.${suff})
	${RM} $(foreach suff, ${TMP_SUFFS}, timetable-wb.${suff})

# delete everything except sources
purge: clean
	${RM} $(foreach suff, ${ALL_SUFFS}, timetable.${suff})
	${RM} $(foreach suff, ${ALL_SUFFS}, timetable-wb.${suff})