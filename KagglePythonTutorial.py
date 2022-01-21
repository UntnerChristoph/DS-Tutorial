import pandas as pd
import numpy as np

#
# https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
# https://pynative.com/python-class-method-vs-static-method-vs-instance-method/


class KagglePythonTutorial:
	def __init__(self, first_name):
		self.first_name = first_name

	def PrintOut(cls):
		print(cls.first_name)