all: projektplan.pdf

projektplan.pdf: projektplan.tex ../LIPS.tex
	pdflatex projektplan.tex && \
	pdflatex projektplan.tex && \
	pdflatex projektplan.tex

clean:
	rm -f projektplan.toc projektplan.log projektplan.aux projektplan.pdf
