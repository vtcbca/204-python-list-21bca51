# ​WAS To create list using UDF with duplicate number and print only unique value from it using UDF.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
l=['2','3','4','5','6','2','3']
print(unique_list(l)) 