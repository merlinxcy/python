import pickle
file=open("temp.pkl","w")
list=[1,2,3,4,5,6]
pickle.dump(list,file)
file.close()
file=open("temp.pkl","r")
read=[]
mylist=pickle.load(file)
print mylist
