import pandas as pd
import numpy as np

#
# https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
# https://pynative.com/python-class-method-vs-static-method-vs-instance-method/

# TODO:
#  self oder cls?
#  naming convention
#  Wie Doku für API damit es als Infotext kommt?


class EnergieGemeinschaft:
	def __init__(self, ):
		self.EnergieDatenGemeinde = pd.DataFrame()
		self.HausA = 0
		self.HausB = 0


	def ladenDerEnergieStandardWerte(self):
		self.EnergieDatenGemeinde = pd.read_excel(sheet_name="EnergieStandardWerte.xlsx")

	def InputDatenHinzufügen(self, HausA, HausB):
		self.HausA = HausA
		self.HausB = HausB

	def berechnenDesGesamtenEnergieverbrauches(self):
		# Hier soll eine Spalte die GesamtEnbergieanzahl beinhalten und pro kategorie,


	def normierenDerDaten(self):
		# TODO:

