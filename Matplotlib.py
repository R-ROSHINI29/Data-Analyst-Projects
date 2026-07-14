#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% md
# Basics of matplotlib
# *color, gradient, width, linestyle
# * plt.plot(x,y,
#             marker = "*", (or v, 8, >, <....etc)
#             markerfacecolor = "Red",
#             markeredgecolor = "black",
#             markeredgewidth = "3",
#             linestyle = "solid", (or "dash", "dot", dashdot..etc)
#             linewidth = 10,
#             color = "blue"
#             )
#%%
students_pass = np.array(["botony","tamil","english","maths","social","zoology"])
students  = np.array([40,14,20,35,45,25])
plt.plot(students_pass,students)
plt.show()
#%%
students_pass = np.array(["botony","tamil","english","maths","social","zoology"])
students  = np.array([40,14,20,35,45,25])
plt.plot(students_pass,students,
         marker='v',
         markerfacecolor='red',
         markeredgecolor='black',
         markeredgewidth=3,
         markersize=10,
         linestyle='-',
         linewidth=2,
         color='orange'
         )
plt.show()

#%% md
# Now to enter the title of this graph
#%%
students_pass = np.array(["Botony","Tamil","English","Maths","Social","Zoology"])
students  = np.array([40,14,20,35,45,25])
plt.plot(students_pass,students,
         marker='v',
         markerfacecolor='red',
         markeredgecolor='black',
         markeredgewidth=3,
         markersize=10,
         linestyle='-',
         linewidth=2,
         color='yellow'
         )
plt.title("Students Pass Analysis",
          color='blue',
          family='Times New Roman',
          fontweight='bold',
          fontsize='x-large',
          fontstyle='italic',
          ha='center',
          va='bottom')

plt.show()

#%%
subject = np.array(["Botony","Tamil","English","Maths","Social","Zoology"])
students_pass  = np.array([40,14,20,35,45,25])
subject_fail = np.array(["tam","eng","mat","soc","zoo","bot"])
students_fail = np.array ([10,50,60,90,150,89])
plt.plot(students_pass,students,
         marker='v',
         markerfacecolor='red',
         markeredgecolor='black',
         markeredgewidth=3,
         markersize=10,
         linestyle='-',
         linewidth=2,
         color='yellow'
         )
plt.plot(subject_fail, students_fail,
         marker='v',
         markerfacecolor='red',
         markeredgecolor='black',
         markeredgewidth=3,
         markersize=10,
         linestyle='-',
         linewidth=2,
         color='brown'
         )
plt.title("Students Pass Analysis",
          color='blue',
          family='Times New Roman',
          fontweight='bold',
          fontsize='x-large',
          fontstyle='italic',
          ha='center',
          va='bottom'
          )
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt

subject = np.array(["Botony","Tamil","English","Maths","Social","Zoology"])
students_pass  = np.array([40,14,20,35,45,25])



plt.bar(subject,students_pass,
        color='blue'
        )
plt.title("Students Pass Analysis",
          color='Brown',
          family='Times New Roman',
          fontweight='bold',
          fontsize='x-large',
          fontstyle='italic'
          )

plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt

subject = np.array(["Botony","Tamil","English","Maths","Social","Zoology"])
students_pass  = np.array([40,14,20,35,45,25])

students_fail = np.array ([10,50,60,90,150,89])

plt.scatter(students_pass,subject,
        color='blue'
        )

plt.scatter(subject_fail,subject,
        color='orange'
        )
plt.title("Students Pass Analysis",
          color='Brown',
          family='Times New Roman',
          fontweight='bold',
          fontsize='x-large',
          fontstyle='italic'
          )

plt.show()
#%%
x = np.array(['pizza', 'burger', 'sandwich', 'roast', 'chocichoci'])
y = np.array([20,15,50,60,15])
plt.pie(y, labels=x, autopct='%1.1f%%',
        shadow=True,
        startangle=90,
        colors=['red','green','blue','brown','orange'],
        #explode=[0.1,0.1,0.1,0.1]
        )
plt.title("Sales in per day",
          color='blue',
          family='Times New Roman',
          fontweight='bold',
          fontsize='x-large',
          fontstyle='italic'
          )
plt.show()
#%%
