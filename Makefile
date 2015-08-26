.PHONY: docs
.PHONY: data

all: data docs
clean:
	rm -fr data/retina
	rm -fr results/*
	rm docs/intro.slides.html

docs:
	ipython nbconvert docs/intro.ipynb --to slides --output=docs/intro

data:
	mkdir -p data/retina
	unzip data/Data.zip -d data/retina
