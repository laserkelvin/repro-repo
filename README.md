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
├── docs
│   ├── papers
│   └── README.md
├── fs
├── notebooks
│   ├── figures
│   ├── outputs
│   ├── routines.py
│   └── Untitled.ipynb
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

This is where the fun is!
