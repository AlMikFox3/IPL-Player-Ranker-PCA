#Python27
import csv
import numpy as np
import operator
np.array=[[]]
names=[]
with open('bowling_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader.next()
    for row in csvreader:
            np.array.append([float(x) for x in row[1:5]])
            names.append(row[0])
#print np.array[2:]

dataspace = np.array[1:]
print dataspace
a=np.asarray(dataspace)
sd=np.std(a,axis=0)
mean=np.mean(a,axis=0)
print mean
print sd
dataspace2=[[]]
for row in dataspace:
        k=0
        l=[]
        for i in row:
                l.append((i-mean[k])/sd[k])
                k=k+1
        dataspace2.append(l)        
##for row in dataspace2:
##        print row
dataspace2=dataspace2[1:]        
transpose = np.asarray(dataspace2).T.tolist()
##for i in transpose:
##        print i


covm = np.corrcoef(transpose)
#covm = np.cov(transpose)
##for i in covm:
##        print i

eig_vals, eig_vecs = np.linalg.eig(covm)

print eig_vals
print eig_vecs

rank={}
i=0
for row in dataspace2:
	v = (eig_vecs[0][0])*row[0] + (eig_vecs[1][0])*row[1] + (eig_vecs[2][0])*row[2] + (eig_vecs[3][0])*row[3]
	rank[v]=names[i]
	i=i+1
sorted_rank=sorted(rank.items(),key=operator.itemgetter(0))
for i in sorted_rank:
      print i
