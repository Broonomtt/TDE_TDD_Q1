def soma(n1, n2):
  if num(n1) and num(n2):
    return float(n1) + float(n2)
  else:
    return None
    
def sub(n3, n4):
  if num(n3) and num(n4):
    return float(n3) - float(n4)
  else:
    return None    
    
def num(s):
  try:
    float(s)
      return True
  except ValueError:
      return False
