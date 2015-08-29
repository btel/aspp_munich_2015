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
	git push
	git clean -x
	rm -f data/Data.zip
	rm -f scripts/*
	rm -f workflows/*
	rm -fr .git
	rm -fr libs/pyNeuro/__pycache__
	git init
	git add * .gitmodules .gitignore
	git commit -m 'initial commit'

docs: docs/intro.slides.html

data : data/retina

docs/intro.slides.html: docs/intro.ipynb
	ipython nbconvert docs/intro.ipynb --to slides --output=docs/intro
	git submodule update

data/retina:
	unzip data/Data.zip -d data
	mv data/Data data/retina
