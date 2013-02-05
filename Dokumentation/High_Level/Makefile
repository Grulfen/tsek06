all: highlevel.pdf

highlevel.pdf: highlevel.tex ../LIPS.tex
	pdflatex highlevel.tex && \
	pdflatex highlevel.tex && \
	pdflatex highlevel.tex

clean:
	rm -f highlevel.toc highlevel.log highlevel.aux highlevel.pdf
