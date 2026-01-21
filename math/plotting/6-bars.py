#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

labels = ['Farrah', 'Fred', 'Felicia']
apple = fruit[0]
banana = fruit[1]               
orange = fruit[2]
peach = fruit[3]
bar_width = 0.5
x = np.arange(len(labels))  
plt.bar(x, apple, color='red', width=bar_width, label='Apples')
plt.bar(x, banana, bottom=apple, color='yellow', width=bar_width, label='Bananas')
plt.bar(x, orange, bottom=apple+banana, color='#ff8000', width=bar_width, label='Oranges')
plt.bar(x, peach, bottom=apple+banana+orange, color='#ffe5b4', width=bar_width, label='Peaches')
plt.ylabel("Quantity of Fruit")
plt.yticks(np.arange(0, 81, 10))
plt.xticks(x, labels)           
plt.title("Number of Fruit per Person")
plt.legend()
plt.show()