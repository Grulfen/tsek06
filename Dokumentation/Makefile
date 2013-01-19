all: test.pdf

test.pdf: test.tex
	pdflatex test.tex && \
	pdflatex test.tex && \
	pdflatex test.tex

clean:
	rm -f test.toc test.log test.aux test.pdf
