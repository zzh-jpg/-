f=input().split()
formula=[]
cal=('+','-','*','/')
for i in f:
     if i in cal:
          a=formula.pop(0)
          b=formula.pop(0)
          formula.insert(0,i+b+a)
     else:
          formula.insert(0,i)
print(' '.join(formula[0]))