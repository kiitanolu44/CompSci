σ=10.
ρ=28.
β=8./3.
dt = 1e-2

xs = [-12.]
ys = [-13.]
zs = [31.]

xs2 = [-12.2]
ys2 = [-13.2]
zs2 = [31.2]

i = 0
while i < 1000:
   i += 1

   x = xs[i-1]
   y = ys[i-1]
   z = zs[i-1]

   new_x = y - x
   new_x *= σ
   new_x *= dt
   new_x += x

   new_y = ρ - z
   new_y *= x
   new_y -= y
   new_y *= dt
   new_y += y

   new_z = x * y
   new_z -= β * z
   new_z *= dt
   new_z += z

   xs.append(new_x)
   ys.append(new_y)
   zs.append(new_z)     

i = 0
while i < 1000:
   i += 1

   x = xs2[i-1]
   y = ys2[i-1]
   z = zs2[i-1]

   new_x = y - x
   new_x *= σ
   new_x *= dt
   new_x += x

   new_y = ρ - z
   new_y *= x
   new_y -= y
   new_y *= dt
   new_y += y

   new_z = x * y
   new_z -= β * z
   new_z *= dt
   new_z += z

   xs2.append(new_x)
   ys2.append(new_y)
   zs2.append(new_z)


print(xs[-1],ys[-1],zs[-1])
print(xs2[-1],ys2[-1],zs2[-1])

from matplotlib.pyplot import figure,show
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs)
ax.scatter(xs2, ys2, zs2)
show()    
