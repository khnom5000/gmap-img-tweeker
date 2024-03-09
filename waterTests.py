from PIL import Image
import numpy as np
from  matplotlib import pyplot as plt
from math import sqrt
#import dev_to_kmeans_article as dtkm
import jonchar_net_article as jcna

water_removal_ratio = 20000

blue = [156,192,249]
im = Image.open('t3_2w_c_bw.png').convert('RGB')
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
X=np.asarray(all_water)

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