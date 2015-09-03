---
layout: post
title: Python on the lab bench (Munich)
date: 2015-08-30 15:49:18
modified: 2015-09-03 11:06:06
categories: journal
---

In the lecture I will try to take an integrative approach to using python in computational science. You shouldn't treat my lecture as the sets of hard standards, but rather my personal view on how to use python and other tools in everyday lab work. Due to my background the lecture will be necessarily biased toward experimental labs, but I hope that many of its ideas can be also used by theoreticians.

It is the first time that we are proposing this lecture at the Python school. Therefore, I would like to ask you for some extra feedback during and after the lecture. Please do not hesitate to interrupt me to ask questions, make comments or disagree. We are all here to learn from each other - so please forget the standard teacher-pupil relationship.

# Prelude

Before we get to the meat of the lecture, I would like to set the stage by discussing a few general remarks about science and scientific computing. Science, in my opinion, is an art of problem solving. Scientists first identify the problem and then use all possible means to find an answer. More and more often *one* of the means is scientific computing. It also means that the goals of scientific computing and software engineering are different: the final product of the former is knowledge (often, but not only, summarised in papers), whereas software engineering attempts to produce robust software meeting all the requirements. In science we don't even know  the requirements until we see the final results (at which time we usually switch to another project). Thus said, scientists may (and should) learn from software engineers (as software engineers may learn from scientists), but we have to select only methods which apply to our field.

A particularly important concepts in scientific computing is *rapid prototyping*. The idea is probably familiar to everyone and its also one of the main strengths of Python: When we come up with an idea, we want to test it as soon as possible without paying too much attention to the elegance of our implementation or adherence to coding conventions (having much experience with the conventions, we can even apply them without much extra effort). When the prototype is done we ditch it and move to another one (if the hypothesis was wrong) or we turn it into a "production" code following the practices we discussed so far at the school.

Another important aspect of the scientific computing is the "getting things done approach". This often involves using tools implemented in many different labs, in different languages (Fortran, Python, C, Matlab etc.), or different systems (Dos, Windows, Unix, MacOS). There is no reason to refuse using a well-designed piece of software just because it was not implemented in the One and Only(TM) programming language.

Unfortunately, I can't give you any general "best practices", which would apply to all the problems, because each problems is different and needs spatial attention. Not always the best solution will involve computer program, sometimes (and more often than we realise) some blackboard calculations or literature search will do much better job. Above all be adaptive and use your common sense.

Before moving on, I would like to offer you some general tips:

* *Focus on problems rather than tools*. I find myself spending 70% of my time on programming and the rest on writing, discussing or reading. I think that people who enjoy programming, like all of you, tend to overemphasise the methodological part of the research over the conceptual. In my opinion, focusing on the problem rather than methods will not only "get you the job", but also will make you also a more productive scientist.

* *Fail early fail often* This phrase reflects advice that I was given by a colleague on how to become a successful scientist: "Produce a lot of ideas and find out quickly that you were wrong". We do learn from our mistakes and even missed attempts will get us closer to our goals. However, if we spend too much time on a misguided idea (or attach to it too strongly), we may never get to the goals.

* *Test your assumptions* This is similar to testing, which is covered by another lecture, don't just assume that you program does what you think, but test it on both real-world and simulated cases. 

* *Learn the tools used in your field* Science is also about collaboration. One platform for collaboration is using the same tools as your colleagues do. Do not try to re-invent the wheel if the existing tools "do their job".

I will to illustrate the concepts with examples from my field that is "computational neuroscience". Neuroscience is a scientific discipline whose goal is to understand how the brain processes information to produce perceptions and actions. As you know the elementary "building block" of the brain is a cell called a neuron. Our brains consist of 10 billions of such neurons which communicate with each other through electrical signals called action potentials. If you insert an electrode close to a neuron you will see typically some erratic small amplitude fluctuations interspersed by high amplitude pulse-like signals. These are the action potentials. Since they are all-or-none events for our purposes it is enough to store just the times at which these action potentials occur (represented by red marks in the plot), thus compressing the signal many-fold. A sequence of such events is called a spike train.

An important question in our field is the one of "neural coding" that is how the neurons represent the information about information in the spike trains. One possibility is that each neuron responds only to a particular element of the world -- in the shown example some neurons respond to the features of forehead others to nose. But if there are two noses and two foreheads how would we know which belong to the same face. This is what is called a "binding problem". One hypothesis postulates that neurons encoding features of the same object are active simultaneously (this is shown for the pair of "red" and "blue" neurons). To test it we might calculate the correlations between the spike times of the neurons after presenting several images.

We are going to do a simple analysis to look into the correlations between neurons located in the retina, which is a layer of photoreceptor located at the back of your eyeball.

## Project phases

We can split a life time of a typical project into several phases. 

* Data exploration -- our first contact with the data and formulating hypotheses,

* Analysis workflow -- a well-defined analysis process, which addresses one or several of our hypothesis

* Batch processing -- running the analysis on all available datasets and gathering statistics.

* Automation -- configuring the analysis to run automatically producing final output (figures, tables, reports) from raw data.

# Data exploration

The first step we usually do when we attack a new problem is to look at the data. We may open it in our favourite data analysis environment (Python) plot a segment of the data, calculate some statistics and perform some sanity checks (the range of values in the right order, the length of recording as given in metadata, the spectrum of the signal looks right etc.). All these preliminary analyses are know as "exploratory data analysis" or EDA.

EDA emphasises the graphical and interactive approach rather than formal statistical analysis. It draws on our pattern-recognition capabilities to get first insights into the data and help to formulate new hypotheses.  

The approach is best summarised by its creator and most famous proponent John Tukey:

> Exploratory data analysis can never be the whole story, but nothing else can serve as the foundation stone -- as the first step.

EDA has many objectives, but the most common are:

* checking data sanity
* discovering unexpected phenomena
* forming new hypotheses
* setting standards for further experiments, such as number of acquired data points to obtain sufficient "statistical power"
* selection of tools and procedures, which are most reliable and most efficient for the data set

In Python we have everything that is needed for EDA: apart from the standard trinity (Python, numpy, matplotlib), recently pandas is gaining popularity (pandas is a Python-based implementation of the DataFrame known from R). For EDA one usually works with the interactive prompt (such as IPython), because it offers immediate feedback. Often I also turn to IPython notebook (nowadays Jupyter) for its literate programming approach (self-documenting code), combination of code and graphs in the same "workspace" and the possibility to re-evaluate the past commands. The disadvantage of Jupyter is that it works only in the browser (so you cannot use your favourite editor) and it is not easy to diff it.

I would also recommend you learning a bit of shell. Shell, such as bash, zsh, ksh etc. is just another programming language. It offers standard programming structures such as variables, functions, loops and conditionals, but it is specialised with operations on file systems (creating, copying, moving files, executing external programs). It also allows to pass extra parameters to the programs by means of *command-line arguments*. One of its strengths is that shell is language agnostic, i.e. it can execute programs written in all scripting and compiled languages. Finally, many of the most powerful editors (such as vim or emacs) work (mainly) in shell.

## Data analysis workflow

After we settled on the hypothesis and analysis methods, we might than design our analysis process. A particularly powerful approach uses so-called analysis workflows. According to my definition an analysis workflow is "a system of interchangeable components connected by a common interface". The component is loosely defined as any program of any complexity that produces output for a given input. The programs can be put together (output of one become inputs of another) thanks to sharing the same interface, which could be anything: a file in a particular format, a function with a specific signature or a common data structure (dictionary, class) etc. This is an instance of one of design patterns called "loose coupling". This design allows to mix-and-match from a poll of available components and assemble them into more complex data analysis workflows. 

Another important feature of many workflows is "data provenance", which tracks the origins of all data generated within the workflow including the scripts used for the generation, their version and version of called libraries, date and time of execution, and possibly all log entries. Provenance is in general a very complex problem and requires a lot of attention and contentiousness, but for larger projects it may ascertain an extra level of reproducibility. I won't cover this topic to a greater detail, but I invite you to check out the resources available [online](https://rrcns.readthedocs.org/en/latest/index.html).

## Unix philosophy

The concept of data analysis workflows aligns very well with the Unix philosophy. According to Wikipedia:

> Unix philosophy emphasizes building short, simple, clear, modular, and extensible code that can be easily maintained and repurposed by developers other than its creators

One of the principles of Unix philosophy is that each tool should do only one thing and do it well (in design-pattern parlance this is called "Single responsibility" principle). This is also what I recommend for the components of the workflow. In Unix the common protocol is the text file, which can be read and produced by most of the Unix shell commands. In data analysis world text files may not be always the best efficient way of storing data, especially when large datafiles are handled. However, this principle applies well to files storing parameters of the analysis workflow. The Unix tools (and also the components) should be possibly small, so that they can be easily combined into larger processes. Finally, the Unix systems allows to construct ad-hoc text processing tools (aka prototypes) on the spot without the need of looking at the implementation of the individual tools. Similarly, a well-designed workflow will allow one to construct data analyses within few minutes with few lines of code.

## Workflow step

A typical workflow will consists of these steps:

* data access -- might be locating and reading files on the local file system, querying the database or downloading from the Web

* data analysis -- the core of the workflow

* data visualisation -- which produces the final outputs


## Workflow managers

Analysis workflows are so abundant in science that you can find a plenty of "workflow managers". Workflow manager will usually allow you to construct a workflow and execute it. Some managers also keep track of the data provenance.

The disadvantage of using workflow managers is that you usually have to learn (and stick to) the API for programming new components.

We can differentiate between the general-purpose managers, which can be used for any field, but don't come pre-equipped with built-in components, and specialised managers, which offer a set of components for analysis of specific data types (bioinformatics, machine learning or image processing). The managers are implemented in many languages (including Python) and may have a command-line interface, scripting language, GUI or Web interface. 

Some of the interesting Python-based managers are:

* [luigi](https://github.com/spotify/luigi)- developed at Spotify and used mainly for web-data analysis locally or on a cluster (such as Hadoop). It includes a sophisticated scheduler (main about it later). The components are defined as Python classes.

* [joblib](http://pythonhosted.org/joblib/) - it comes from the neurimaging field, but it can be easily repurposed for analysis of other types of data. The components are Python functions -- it allows for storing the intermediate results (memomize pattern).

* [sumatra](http://pythonhosted.org/Sumatra/) - it is not a typical workflow manager, but it focuses on data provenance. Analysis is defined in external programs (bash, Python etc.). It includes a command-line interface for running analysis, and Web-interface for accessing the database of executed analysis (together with its parameters, version of all libraries and results).

## Simple Python-based workflow

Instead of using one of the above workflow managers, I will demonstrate you how to build your own. In Python a simple workflow can be constructed from individual Python modules:

```python
import parse_data
import calculate_correlations
import plot_histogram


def main(data_path):
    data = parse_data.main(data_path)

    correlations = calculate_correlations.main(data)

    plot_histogram.main(correlations,
                        saveto='correlation_histogram.svg')
                        
if __name__ == '__main__':
    
    data_path = '/location/of/datafile'
    main(data_path)
```

In the example `parse_data`, `calculate_correlations` and `plot_histogram` are three modules, which define at least the `main` function, which runs their part of the analysis. The `data` returned by the `main` function of `parse_data` is then passed to `calculate_correlations`, whose output, the `correlations` array is than plotted in `plot_histogram`. The resulting image is stored in a file on the local file system. Note that the analysis implemented by the workflow is itself defined in the `main` function, such that the workflows may be reused and nested. The data file used by the workflow is given in the `__main__` block of the Python script (only executed when the script is executed, not imported). A better way of passing parameters to Python program will be demonstrated during the exercises.

This approach works indeed very well when all the components (workflow steps) are implemented in Python. If this is not the case a Python adapter would have to be implemented. Another disadvantage of this example is that the intermediated results are not kept, but it can also be implemented (you can also check out [joblib](http://pythonhosted.org/joblib/)).

## Data management

Before we move on, I will add some comments on the data management. First of all, remember to keep the backups of the raw data. Small (< 100 MB) binary data can be kept in the git repository, for larger datasets you can use git annex or similar. Alternatively (or additionally) remember to keep the back-ups (several copies) on robust media (stationary disks are more robust than portable, SSDs are more robust than spinning disks) and in diverse geographical locations (work, home, cloud). The raw data should be accompanied with relevant meta-data (format of the files, acquisition protocol etc.)

You should never change the raw data. Instead, make a copy for the processed files and keep them in a separate folder. Separate your code and your data; the same holds for code and parameter files.

## Directory structure

Speaking of directory structure, here is an example of organisation of your project directory:

```
..
├── data
│   ├── Data.zip
│   └── README.txt
```

Data folder contains the raw data together with meta-data (README.txt)

```
├── docs
│   ├── images
│   ├── intro.ipynb
│   └── outline.txt
```

`docs` contains project documentation.

```
├── figures
```

`figures` is a folder where all the generated figures will be stored.

```
├── libs
│   └── pyNeuro
```

`libs` contains all the libraries, which are developed simultaneously with the project. The libraries usually consists of functions that are not specific for the project and can be re-used for other projects.

```
├── results
```

The folder where the data files generated by the workflow are created.

```
├── scripts
│   ├── batch_analyse.py
│   ├── calculate_correlations.py
│   ├── merge_script.py
│   └── plot_correlations.py
```

The `scripts` component contains the  workflow components.

```
├── workflows
│   ├── dodo.py
│   └── run_workflow.sh
```

Actual workflow definitions.

```
└── Makefile
```

`Makefile` for automatically generating documentation and running analyses. More on that later.

# Batch processing

In most data analysis tasks after we decided on the details of data analysis on a single file, we want to run the same process on all data sets coming from multiple recording sessions and gather more "statistics". This is called "batch processing". Since individual task (running the analysis on a single dataset) do not depend on each other, batch processing is easily parallelizable (it is "embarrassingly parallel").

Python paradigm for bath processing is running the workflow in a for loop on each file separately. In addition, `glob` module can be used for interaction over all the files in the data directory.

# Automation

After we have set most of our analysis and batch processing, we may try to automate the process of running the analysis and producing the final documents (reports, papers, etc.). Since some of the analyses might take much time, we might also want to run them only when needed, that is when new data is added or some parameters of the analysis change.

This problem is known to software engineers as automatic build process and includes compiling source code into binary code, running automated test or creating documentation from sources. In science, the respective tasks for automatic build include running analyses, producing figures, compiling source documents. 

Most build tools implement dependency tracking, which allows to shorten building times by running only the steps, whose inputs changed. The inputs, outputs and the process which transforms inputs into outputs is defined by rules and recipes. Based on the list of the rules and the status of all the inputs (usually modification times) it is up to the build tool to determine which recipes to execute and in what order.

This is illustrated by the simple example consisting of two rules defined in an abstract syntax:

```
Rule 1:
    input.txt --| python script1.py |--> intermediate.txt

Rule 2:
    intermediate.txt,params.json --| python script2.py |--> results.txt
```

The output of Rule 1 is one of the inputs in Rule 2. When `input.txt` changes the both scripts have to be re-executed. If `intermediate.txt` changes the dependencies of Rule 1 are satisfied and only `script2.py` is re-executed.

The most widespread build tool is `make`. Other tools such as `cmake` and `ant` are modelled after `make`, but improve on some of its weaknesses. All these programs can be used to automate any process, but there are especially well suited for compiling programs (they all include pre-defined rules for compiling libraries from C sources etc.). Similar build tools (`SCons` and `waf`) are implemented in Python and use Python syntax for defining the rules and writing extensions.

`doit` and `rake` are two build tools that do not come with pre-defined rules, but the rules can be easily defined using a programming language (Python in the former case and ruby in the other).

Finally, there exist build tools that specialise in running the data analysis. Some examples include `drake` (`make`-like program that facilitates some of the common tasks used in data analysis) and `luigi` (a workflow manager implemented in Python with dependency tracking mechanisms).
