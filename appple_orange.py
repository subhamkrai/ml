#!/usr/bin/python3

from  sklearn  import  tree

import  sys
inn=sys.argv

w=int(inn[1])
out=int(inn[2])
#print(type(w),type(out)) 

#  apple &  orange  ---  textture , weigth
#  smooth ==  0  and  bumpy  ==  1  

features=[[110,0], [120,0], [130,1],[140,1]]

output=["Apple","Apple","orange","orange"]


#  now loading  decisiontree classifier  

algo=tree.DecisionTreeClassifier()

#  Now training  the features and output set
 
trained=algo.fit(features,output)   #  generally looking for 1 core  CPU  --  [GPU ] 

#  testing  trained  model  OR  Q &  A 
resoutput=trained.predict([[126,1]])

#  priting  result 

print(resoutput)
