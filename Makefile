.PHONY: docs
.PHONY: data

all: data docs

clean:
	rm -fr data/retina
	rm -fr results/*
	rm -f docs/intro.slides.html
	rm -fr docs/reveal.js
	rm -fr figures/*
	
distclean : clean
	rm -f data/Data.zip
	rm -f scripts/*
	rm -f workflows/*
	rm -fr libs/pyNeuro/__pycache__

pageclean: docs
	rm -fr data
	rm -fr workflows
	rm -fr scripts
	rm -fr libs
	rm -fr results
	rm -fr figures
	mv docs/intro.slides.html index.html
	mv docs/reveal.js .
	mv docs/custom.css .
	rm -fr reveal.js/.git
	mv docs/images .
	rm -fr docs
	rm Makefile

docs: docs/intro.slides.html docs/lecture_notes.html

data : data/retina

docs/intro.slides.html: docs/intro.ipynb
	ipython nbconvert docs/intro.ipynb --to slides --output=docs/intro
	patch -p1 docs/intro.slides.html < docs/reveal_initialize.patch
	rm docs/intro.slides.html.orig
	git submodule update

docs/lecture_notes.html : docs/lecture_notes.md
	pandoc $< -o $@ -s -c pandoc.css --toc

data/retina:
	unzip data/Data.zip -d data
	mv data/Data data/retina
