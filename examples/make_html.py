root_dir = "./outputs"

from fig_html.utils import SampleFiguresMaker
SampleFiguresMaker().make(root_dir)

from fig_html import HTMLMaker
HTMLMaker().make(root_dir)