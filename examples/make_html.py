root_dir = "./outputs"

from fightml.utils import SampleFiguresMaker
SampleFiguresMaker().make(root_dir)

from fightml import HTMLMaker
HTMLMaker().make(root_dir)