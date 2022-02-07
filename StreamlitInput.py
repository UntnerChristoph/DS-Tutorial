import streamlit as st
import numpy as np

# class
def test():
	dataframe = np.random.randn(10, 20)
	print("dataframe")
	st.dataframe(dataframe)


def testPrint():
	print("Hello")