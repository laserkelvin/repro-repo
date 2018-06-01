# __Repro_ducible __Repo__sitories

## A template Github repo for reproducible research projects

---

# Introduction

This repository is designed to be cloned and used as a template to set the
foundations of an easily managable research project. The use of a repo is
two-fold: first, it removes the need to set up the file structure by hand each
and everytime, minimizing change between research projects. Second, the use of
`git` will let us track changes to the analysis code and outputs (e.g. plots).

The file structure is set to be non-field specific, and could be used for any
kind of research project. The only real requirement is that the analysis is
done with Jupyter notebooks.

# Filestructure

.
├── data

│   ├── clean

│   └── raw

├── docs

│   ├── papers

│   └── README.md

├── notebooks

│   ├── 1_Data cleaning.ipynb

│   ├── 2a_Analysis.ipynb

│   ├── 2b_More analysis.ipynb

│   ├── 3_Project summary.ipynb

│   ├── figures

│   ├── outputs

│   └── routines.py

├── README.md

└── tex

## `data`

This folder stashes all of the raw data used for the analysis. I make a copy
from our central raw data repository and put them here, so that the original
raw data does not risk being overwritten, and that the data used for the
analysis can be easily found and reproduced.

Data should be organized in some coherent fashion - timestamps, ID codes, or
conditions under which they were took. In our lab we use ID numbers (e.g.
1921516) to reference data. These are relatively easy to reference in Jupyter
notebooks.

## `docs`

This is the folder that holds all of the research material - in my case, PDFs
of papers I use to compare analysis with, or take reference values from. Simple
practice is to drag and drop the PDF into `docs/papers/`, and refer to them in
the analysis notebooks.

`README.md` is an important file - I aim to write all my notes that come up in
the process: what papers have an important figure/number to consider;
descriptions of the raw data; thoughts, etc. In lieu of a physical notebook,
this is where a majority of the documentation will fall into.

## `notebooks`

This is the folder where most of the work will be done. The practice here is to
use a new notebook for each step of the analysis: one to clean/preprocess the
data, one for each analysis procedure, and one to summarize the project. I tend
to also have separate notebooks for generating figures for presentations and
for publications.

Also in this directory are two empty folders, `figures` and `outputs`. The
figures folder is where the output of all the plots should go (if they're
saved) and outputs stashes the analysis results, in a way that subsequent
notebooks can easily load the results in and do further analysis/plotting.

It's also probably good practice to name each figure/plot not only something
descriptive, but also give reference to the notebook that produced it.

Finally, I have a file called `routines.py` as a dummy Python module. This (or
any number of module files) should be used to keep code that are shared across
notebooks. In the interest of making the notebooks as informative as possible,
I think code that is unique to the notebook should be kept in the notebook.

## `tex`

Where the write-up/manuscript preparation occurs. I use LaTeX for writing
papers, and so in a TeX document you can simply target the source path for
graphics to be within `notebooks/figures/`.

# Usage

A typical workflow would be as follows:

1. Copy raw data to `data/raw/`
2. Perform cleaning/preprocessing on raw data, output to `data/clean/`
3. Perform analysis on cleaned data, output results to `notebooks/outputs/`
4. Make figures based on analyzed data, save plots to `notebooks/figures/`
5. Project is complete, summarize in notebook
6. Write the paper!
7. ???
8. Profit.

It is probably useful to make frequent `git` commits. Natural points would be
between analysis steps, when you decide you want to analyze the data
differently, etc. It's probably better practice to track the changes of each
folder __individually__ as opposed to simply `git commit -a`.

