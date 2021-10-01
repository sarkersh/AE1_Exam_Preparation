"""Create 2 functions: both_Ts
•	start by creating a figure with a single subplot
•	draw a smaller T shape with red continuous line and triangle markers – the coordinates are:
p1: x=2, y=2
p2: x=2, y=6
p3: x=1, y=6
p4: x=1, y=7
p5: x=4, y=7
p6: x=4, y=6
p7: x=3, y=6
p8: x=3, y=2
•	draw a larger T shape with blue dashed line and diamond markers – the coordinates are:
p1: x=1, y=1
p2: x=1, y=5
p3: x=5, y=5
p4: x=5, y=12
p5: x=10, y=12
p6: x=10, y=5
p7: x=14, y=5
p8: x=14, y=1

•	finally, show the full picture
separate_Ts
•	start by creating one figure with 2 subplots sharing x axis
•	draw the smaller T with yellow dash-dot line and square markers on the first subplot
•	draw the larger T with green line on the other subplot
•	display the full figure"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import matplotlib.pyplot as plt

def both_Ts():
    # single subplot
    plt.subplot(1,1,1)
    x = 2,2,1,1,4,4,3,3,2
    y = 2,6,6,7,7,6,6,2,2
    plt.plot(x, y, 'r^-')

    x = 1,1,5,5,10,10,14,14,1
    y = 1,5,5,12,12,5,5,1,1
    plt.plot(x, y, 'bD--')      
    plt.show()

# both_Ts()

def separate_Ts():
    # double subplots
    plt.subplot(4,1,1)
    x = 2,2,1,1,4,4,3,3,2
    y = 2,6,6,7,7,6,6,2,2
    plt.plot(x, y, 'ys-.')

    plt.subplot(4,1,3)
    x = 1,1,5,5,10,10,14,14,1
    y = 1,5,5,12,12,5,5,1,1
    plt.plot(x, y, 'g-')      
    plt.show()

separate_Ts()


























