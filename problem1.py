import json

data = open("file\\pos_0.png.json","r")
result = data.read()
obj=json.loads(result)

final={}
s={}
k = {}

listt = list(obj.keys())
list2 = obj[listt[3]]
#print(list2[1])
l = len(list2)
b={}
for j in range(l):
  a={}
  list3 = list2[j]
  li = len(list3)
  res = list(list3.keys())
  tags = list3[res[7]]
  for i in range(len(tags)):
    g = list(tags[i].keys())
    v = tags[i]
    a[str(v[g[2]])]=str(v[g[3]])
  b[str(list3[res[8]])] = a
  list4=list3[res[9]]
  vx = list(list4.keys())
  
  if(list3[res[8]]=="Vehicle"):
    s["presence"]=1
    s["bbox"]=list4[vx[0]]
  elif(list3[res[8]]=="license_plate") :
     s["presence"]=0
     s["bbox"]=" "
  k[str(list3[res[8]])]=s
    
final["dataset_name"] = "pos_0.png.json"
final["image_link"] = " "
final["annotation_type"] = "image"
final["annotation_objects"] = k
final["annotation_attributes"] = b

print(final)

  

with open("formatted_pos_0.png.json",'w') as f:  # the combined file is 01.json
  json.dump(final,f,indent=4)

    