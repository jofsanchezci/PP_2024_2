def S(n):
  return n+1

def A(n):
  return n-1

def SumaS(x,y):
  if y==0:
    return x
  else:
    count=0
    while count < y:
      aux=S(x)
      count=count+1
      x=aux
  return x

#print(SumaS(2,2))

def mulS(x,y):
  if y==0:
    return 0
  else:
    count=0
    resul=x
    while count < y-1:
      aux=SumaS(resul,x)
      count=count+1
      resul=aux  
  return resul  
    

#print(mulS(9,9))

def restaS(x,y):
  if y > x:
    return False
  elif y == 0:
    return x
  else:
    count = 0
    while count < y:
      aux=A(x)
      count=count+1
      x=aux
  return x

print(restaS(15,3))    

def divS(x,y):
  if y>x:
    return False
  elif y==0:
    return False
  else:
    count=0
    resul=x
    while x+1>y:
      aux=restaS(resul,y)
      count=count+1
      resul=aux
      x=aux

  return count  

print(divS(81,9))





