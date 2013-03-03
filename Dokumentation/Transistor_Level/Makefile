all: transistor.pdf

transistor.pdf: transistor.tex ../LIPS.tex
	pdflatex transistor.tex && \
	pdflatex transistor.tex && \
	pdflatex transistor.tex

clean:
	rm -f transistor.toc transistor.log transistor.aux transistor.pdf
