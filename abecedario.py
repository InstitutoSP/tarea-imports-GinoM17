list1 = [1,5,9,8,2,65,45,78,95,32,111,55,8,-5]
stop= True
list1_ord=[]
list_temp=list1.copy()
while stop:
  val_max=list_temp[0]
  for i in range(len(list_temp)):
     x=list_temp[i]

     if (x>val_max):
       val_max=x

  list1_ord.append(val_max)
  list_temp.remove(val_max)
  if len(list_temp)==0:
     stop= False
print("lista ordenada",list1_ord)
print("lista original",list1)



list2 = [51,18,89,65,4,2,3,5,96,85,74,14,25,36,32,65,98,87,45,12]
stop= True
list2_ord=[]
list_temp=list2.copy()
while stop:
  val_min=list_temp[0]
  for i in range(len(list_temp)):
     x=list_temp[i]

     if (x<val_min):
       val_min=x

  list2_ord.append(val_min)
  list_temp.remove(val_min)
  if len(list_temp)==0:
     stop= False
print("lista ordenada",list2_ord)
print("lista original",list2)

list3 = ["Bruno","Joaquin","Martin","Gonzalo","Franco","Matias","Quimy","Marti"]
stop= True
list3_ord=[]
list_temp=list3.copy()

while stop:
  letra_may=list_temp[0]
  for i in range(len(list_temp)):
     x=list_temp[i]

     if (x<letra_may):
       letra_may=x

  list3_ord.append(letra_may)
  list_temp.remove(letra_may)

  if len(list_temp)==0:
     stop= False

print("lista ordenada",list3_ord)
print("lista original",list3)