import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Step1: Create the Figure and Axis
fig,ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.grid(True)

# Step 2: Initialize the 1circle (parametric form) and ball
theta = np.linspace(0,2*np.pi,100)
size = 1
x = np.cos(theta)*size
y = np.sin(theta)*size
ax.plot(x,y, color='blue')

# Step 3: Initialize the ball's position
ball, = ax.plot([], [], 'ro', markersize=10)  # Unpack the list to get the Line2D object

# Step 4: Define the update function
def update(frame):
    # Parametric equations for x and y positions of the ball around the circle
    ball_x = np.cos(frame)
    ball_y = np.sin(frame)
    ball.set_data([ball_x], [ball_y])  # Update ball's position (wrap as list)
    return ball,

# Step 5: Set up the animation
frames = np.linspace(0, 2*np.pi, 200)  # 300 frames for smooth animation
ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=1)

#show
plt.show()