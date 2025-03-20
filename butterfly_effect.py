def butterfly_effect(
      xs: list[float], 
      ys: list[float], 
      zs: list[float], 
      iterations: int
) -> tuple[list[float], list[float], list[float]]:
   for i in range(iterations):
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

   return xs, ys, zs


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

xs, ys, zs = butterfly_effect(xs=xs, ys=ys, zs=zs, iterations=1000)
xs2, ys2, zs2 = butterfly_effect(xs=xs2, ys=ys2, zs=zs2, iterations=1000)

print(xs[-1],ys[-1],zs[-1])
print(xs2[-1],ys2[-1],zs2[-1])

from matplotlib.pyplot import figure,show
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs)
ax.scatter(xs2, ys2, zs2)
show()    
