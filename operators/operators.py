# -*- coding: utf-8 -*- 

def add(a, b):
  """ It add two numbers
  
      param a: Frist value
      type a: int, float
      param b: Second value
      type b: int, float
      
      return: int, float 
  """
  if type(a) == str or type(b) == str: raise TypeError("IT should not be an string")
  return a + b