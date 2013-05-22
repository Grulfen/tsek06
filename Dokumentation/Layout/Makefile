all: layout.pdf

layout.pdf: layout.tex ../LIPS.tex
	pdflatex layout.tex && \
	pdflatex layout.tex && \
	pdflatex layout.tex

clean:
	rm -f layout.toc layout.log layout.aux layout.pdf
