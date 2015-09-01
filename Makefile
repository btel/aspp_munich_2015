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

docs: docs/intro.slides.html

data : data/retina

docs/intro.slides.html: docs/intro.ipynb
	ipython nbconvert docs/intro.ipynb --to slides --output=docs/intro
	patch -p1 docs/intro.slides.html < docs/reveal_initialize.patch
	rm docs/intro.slides.html.orig
	git submodule update

data/retina:
	unzip data/Data.zip -d data
	mv data/Data data/retina
