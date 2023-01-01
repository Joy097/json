import json
a=[]
data = open("file\\pos_0.png.json","r")
result = data.read()
obj=json.loads(result)
a.append(obj)
data = open("file\\pos_10010.png.json","r")
result = data.read()
obj=json.loads(result)
a.append(obj)
data = open("file\\pos_10492.png.json","r")
result = data.read()
obj=json.loads(result)
a.append(obj)

for i in range(len(a)):
   listt = list(a[i].keys())
   list2 = a[i][listt[3]]
   l = len(list2)

   for j in range(l):
  
     list3 = list2[j]
     li = len(list3)
     res = list(list3.keys())
     for k in range(len(res)):
       if(res[k]=="classTitle"):
         if(list3["classTitle"] == "Vehicle"):
           list3["classTitle"] = "car"
         if(list3["classTitle"] == "License Plate"):
           list3["classTitle"] = "number"


with open("01.json",'w') as f: #the combined file name is 01.json
  for i in range(len(a)):
    json.dump(a[i],f,indent=4)
