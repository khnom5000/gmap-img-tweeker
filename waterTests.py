from PIL import Image
import numpy as np
from math import sqrt
#from  matplotlib import pyplot as plt
#import json
#import dev_to_kmeans_article as dtkm
#import jonchar_net_article as jcna
#import npencoder as npe

green = [187,226,198]
blue = [156,192,249]

im = Image.open('3e.png').convert('RGB')

imnp = np.array(im)
#print(imnp.shape)

#x here holds a tuple - of line, column, RBG value, we can ignore the RBG bit i.e. x[2] as its always [0,1,2]
x = np.where(imnp == blue)

#Get the uniq list of "blue" pixels
water_list = list()
for i in range(len(x[0])):
    water_list.append([x[0][i],x[1][i]])
all_water = [list(x) for x in set(tuple(x) for x in water_list)]

#make it np
#X=np.asarray(all_water)
# print(X)

"""dev_to_kmeans_article https://dev.to/sajal2692/coding-k-means-clustering-using-python-and-numpy-fg1"""
# clusters, centroids=dtkm.run_Kmeans(5,X)
# Y=centroids
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(X[:,0], X[:,1], alpha=0.5)
# ax.scatter(Y[:,0], Y[:,1], alpha=0.5)
# plt.show()
# print("\n----\n",X,"\n----\n",clusters,"\n----\n")

"""jonchar_net_article https://jonchar.net/notebooks/k-means/"""
# clusters, centroids=jcna.run_Kmeans(3,X)
# Y=centroids

# group_colors = ['skyblue', 'coral', 'lightgreen']
# colors = [group_colors[j] for j in clusters]

# fig, ax = plt.subplots(figsize=(4,4))
# ax.scatter(X[:,0], X[:,1], color=colors, alpha=0.5)
# ax.scatter(centroids[:,0], centroids[:,1], color=['blue', 'darkred', 'green'], marker='o', lw=2)
# ax.set_xlabel('$x_0$')
# ax.set_ylabel('$x_1$')
# plt.show()
# print("\n----\n",X,"\n----\n",clusters,"\n----\n")

"""pure euclid distance"""
all_water_euclid = dict()
for water in all_water:
    euclid_value = int(sqrt((water[0]*water[0])+(water[1]*water[1]))*10)
    if euclid_value in all_water_euclid:
        all_water_euclid[euclid_value].append(water)
    else:
        all_water_euclid[euclid_value]=list()
        all_water_euclid[euclid_value].append(water)

# all_water_euclid_ordered.sort()
# print(all_water_euclid)
all_water_euclid_sorted=dict(sorted(all_water_euclid.items()))
# with open("water.json", "w") as outfile:
#     json.dump(all_water_euclid_sorted, outfile, cls=npe.NpEncoder)

prev_x=0
i=0
all_water_grouped=list()
all_water_grouped.append(list())
for x in all_water_euclid_sorted:
    # print(x,all_water_euclid_sorted[x])
    if prev_x == 0:
        None
    elif prev_x <= x <= prev_x+10:
        None
    else:
        i+=1
        all_water_grouped.append(list())

    prev_x=x
    for w in all_water_euclid_sorted[x]:
        all_water_grouped[i].append(w)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(X[:,0], X[:,1], alpha=0.5)

for group in all_water_grouped:
    if len(group) < 360:
        #Y=np.asarray(group)
        #ax.scatter(Y[:,0], Y[:,1], alpha=0.5)
        for w in group:
            imnp[w[0],w[1],0]=green[0]
            imnp[w[0],w[1],1]=green[1]
            imnp[w[0],w[1],2]=green[2]

# plt.show()

Image.fromarray(imnp).save('3ee.png')
