from PIL import Image
import numpy as np
# from matplotlib import interactive
# interactive(True)
from  matplotlib import pyplot as plt
from math import sqrt
#import dev_to_kmeans_article as dtkm
import jonchar_net_article as jcna

water_removal_ratio = 20000

blue = [156,192,249]

#im = Image.open('3.png').convert('RGB')
#im = Image.open('t.png').convert('RGB')
#im = Image.open('t2.png').convert('RGB')
#im = Image.open('t2_90.png').convert('RGB')
#im = Image.open('t3.png').convert('RGB')
#im = Image.open('t3_2w_c.png').convert('RGB')
im = Image.open('t3_2w_c_bw.png').convert('RGB')

imnp = np.array(im)

#print(imnp.shape)

#set up some stuff foe later
# print("height:",len(imnp[:,0]),"width:",len(imnp[0]))
# print("size:",len(imnp[:,0])*len(imnp[0]))
# print("water body pixel limit:",(len(imnp[:,0])*len(imnp[0]))/water_removal_ratio)
#limit=(len(imnp[:,0])*len(imnp[0]))/water_removal_ratio

#x here holds a tuple - of line, column, RBG value, we can ignore the RBG bit i.e. x[2] as its always [0,1,2]
x = np.where(imnp == blue)
# print(x)
#this will tell us how "big" the water is if we uniq it down i.e. there are X pixels of "water"
#print("row:",x[0],"col:",x[1])

water_list = list()
for i in range(len(x[0])):
    water_list.append([x[0][i],x[1][i]])
all_water = [list(x) for x in set(tuple(x) for x in water_list)]
# print(all_water)
# print(type(all_water))
X=np.asarray(all_water)
# print(type(X))

# print(np.linalg.norm(all_water[0])-all_water[1])
# print(np.linalg.norm(all_water[1])-all_water[0])
# print(np.linalg.norm(all_water[0])-all_water[2])
# print(np.linalg.norm(all_water[2])-all_water[0])

##HOW DO WE GROUP BODIES OF WATER ?? for now we hack :)
#water_group = all_water
##provided we can sort the above issue... we can continue to "fix" it

#if len(water_group) < limit:
#    print("water group is to small - removing:",water_group)

#print(x)
#x_2d = np.delete(x,2,0)
#print(x_2d)
#x_uniq = np.unique(x_2d,axis=1)
# print(x_uniq.shape)
# x_sort = np.sort(x_uniq,axis=1)
# print(x_sort)
#all_water_stacked = np.stack(all_water, axis=1)
# print(all_water_stacked)
#all_water_stacked_back = np.stack(all_water, axis=0)
# print(all_water_stacked_back)
   
# plt.plot(all_water)

# for water in all_water:
#     print(water)
#     print(sqrt((water[0]*water[0])+(water[1]*water[1])))

# grouped_water = []
# while len(all_water) != 0:
#     print(all_water)
#     water = all_water.pop(0)
#     print(water)
#     print(all_water)

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
clusters, centroids=jcna.run_Kmeans(3,X)
Y=centroids

group_colors = ['skyblue', 'coral', 'lightgreen']
colors = [group_colors[j] for j in clusters]

fig, ax = plt.subplots(figsize=(4,4))
ax.scatter(X[:,0], X[:,1], color=colors, alpha=0.5)
ax.scatter(centroids[:,0], centroids[:,1], color=['blue', 'darkred', 'green'], marker='o', lw=2)
ax.set_xlabel('$x_0$')
ax.set_ylabel('$x_1$')
plt.show()
print("\n----\n",X,"\n----\n",clusters,"\n----\n")