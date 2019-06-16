# Overview
fig_html generates minimal html files from directories where figures were saved.

# Requirement

```
python >= 3.6
```

```
numpy
pandas
matplotlib
jinja2 >= 2.10
```
The matplotlib is only for making sample figures.

# Installation

```
pip install fig-html
```

# Usage
Suppose we saved figures in a directory hierarchicaly.

`SampleFiguresMaker` makes sample figures and directory.

```python
from fig_html.utils import SampleFiguresMaker

root_dir = "./outputs"
SampleFiguresMaker().make(root_dir)
```

```
└── outputs
    ├── correlation
    │   ├── correlation
    │   │   ├── fig1.png
    │   │   ├── fig2.png
    │   │   └── fig3.png
    │   ├── fig1.png
    │   ├── fig2.png
    │   └── fig3.png
    └── histogram
        ├── histogram1.png
        ├── histogram2.png
        └── histogram3.png
```

`HTMLMaker` adds html file in each directory like below.

```python
from fig_html import HTMLMaker

root_dir = "./outputs"
HTMLMaker().make(root_dir)
```

```
└── outputs
    ├── _static
    │   └── basestyle.css
    ├── correlation
    │   ├── correlation
    │   │   ├── correlation.html
    │   │   ├── fig1.png
    │   │   ├── fig2.png
    │   │   └── fig3.png
    │   ├── correlation.html
    │   ├── fig1.png
    │   ├── fig2.png
    │   └── fig3.png
    ├── histogram
    │   ├── histogram.html
    │   ├── histogram1.png
    │   ├── histogram2.png
    │   └── histogram3.png
    └── outputs.html
```

Now we can check figures easily like this.

![htmldemo](https://raw.github.com/wiki/kazetof/fig_html/img/fig_html_sample.gif)


