import random as rd

L=100

names=["Bella","Tigger","Chloe","Shadow","Molly","Paws","Max","Milo","Pepper","Sasha","Oliver","Mittens","Misifu","Gremlin","Rina","Gizmo","Oreo","Patches","Bailey","Buddy","Misty","Garfield","Arseface","Baby","Peanut","Midnight","Lucky","Lucy","Luna","Kiki","Bandit","Poop","Frankie","Boots","Coco","Po","Chester","Tuna","Banana","Batman","Romeo","Jake","Tucker","Murphy","Izzy","Einstein","Iggy","Tom","Sadie","Lou","Reed","Bowie","Frank","Francis","Sadie","Pauli","Heisenberg","Richard","Dick","Leo","Tony","Blue","Red","Sox","Sue"]

colors=["black","gray","white","orange","blue","ginger","blonde","psychedelic","cream","cinnamon","smoke","chocolate","liliac"]

f=open('cats_data.txt','w+')

for i in range(L) :
  #Format = "NAME COLOR AGE WEIGHT(kg) LENGTH(cm)"
  name=rd.choice(names)
  color=rd.choice(colors)
  age=rd.randint(0,16)
  weight=rd.gauss(1.5,.5)*3.5
  length=rd.gauss(1.5,.5)*23
  cat_data="%s\t%s\t%d\t%f\t%f" % (name,color,age,weight,length)
  f.write(cat_data+"\n")


f.close()