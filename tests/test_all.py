import unittest
import doctest
from fightml.utils import sample_fig_maker
from fightml.utils import path
from fightml import fightml_maker

modules = [sample_fig_maker, path, fightml_maker]
suite = unittest.TestSuite()

for module in modules:
    suite.addTest(doctest.DocTestSuite(module))
runner = unittest.TextTestRunner()
runner.run(suite)