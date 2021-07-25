#%%
 #on a importé numpy de la bibliothèque pour faire des opérations sur des listes
import numpy as np
#on importe la fonction interpolate de la bibliothèque scipy pour interpoler les points
from scipy import interpolate
#on a importé matplotlib.pyplot de la bibliothèque pour dessiner la courbe qui représente la voiture
import matplotlib.pyplot as plt
#x et y représentent les abscisses et les ordonnées de la forme de la voiture sur un papier
X=[2,1.6,1.2,0.9,0.85,0.8,1,0.3, 0.8,2.1,3.3,4.6,5.4,6.4,7.25,8.4,9.6, 10.9,12.4,13.4,15.3, 16.9,19,20.5,19.2,18.1,16.8,15.1,8,2]
Y=[3.4,3.5,3.75,4,4.4,4.8,5.3,6.85,7,5.5,5,7,6,6.3,6.5,6.3,6,5.85,5-9,5.85,5.8,5.75,5.65,5.4,4.7,4.3,4.1,3.8,3.5,3.5,3.4]
#Le couple de X,Y
M =np.array([(X[i],Y[i]) for i in range(len(X))])
#L représente la longueur de la liste x.
l=len(X)
#t représente les noeuds de la fonction d'interpolation
t=np. linspace(0,1,l-2)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])
#La séquence de Longueur 3 contenant les neuds(t), les coefficients(X,Y) et le degré de la spline(4).
W=[t, [X,Y], 4]
#L représente l'intervalle [0,1] divisé en num=100 points, plus num est grand plus la courbure est plus parfaite.
L=np.linspace(0,1,100)
# I est le tableau de valeurs représentant la fonction spline évaluée aux points de X.
I= interpolate.splev(L,W)
#Plot des points (X,Y) et de la fonction représentant la spline de ces points.
plt.plot(X,Y,marker='.',markerfacecolor='red')
plt.plot(I[0],I[1], linewidth=2.0)#Plot du deuxième élèmet de liste I en fonction du premier avec une épaisseur égale à 2.
plt.axis ([min(X)-1, max(X)+1, min(Y)-1, max(Y)+1])
plt.title('Spline de la voiture')
plt.show()

# %%
