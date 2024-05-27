#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
  def is_exclamation(self):
    return self.value.endswith('!')

  def is_sentence(self):
    return self.value.endswith('.')
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
        self._value = value
    else:
        print("The value must be a string.")
  
  def is_sentence(self):
        return self.value.endswith('.')
      
  def is_exclamation(self):
     return self.value.endswith('!')
   
  def is_question(self):
     return self.value.endswith('?')
   
  def count_sentence(self):
      
      sentences = [sentence for sentence in sentences if self.value()]
      return len(sentences)
  
  