from splines import CatmullRom
import matplotlib.pyplot as plt
import numpy as np
from time import time

from ray_catmullrom_intersection import intersection
from helper import plot_spline_2d, plot_tangent_2d
np.set_printoptions(precision=4)

from ipdb import set_trace

points1 = [
    (-1, -0.5),
    (0, 2.3),
    (1, 1),
    (4, 1.3),
    (3.8, -0.2),
    (2.5, 0.1),
]

pts1 = np.array(points1)

s1 = CatmullRom(points1, endconditions='natural')

# ray description
rayo = np.array([0,0])
rayd = np.array([1,2])
rayd = rayd/np.linalg.norm(rayd)

# intersection test
start = time()
intersection_pt = intersection(s1, pts1, rayo, rayd)
if intersection_pt[0] is not None:
  print("Intersection exists")

end = time()
print(f"Time taken: {end-start:.3f}")
# visualization

fig, ax = plt.subplots()
plot_spline_2d(s1, ax=ax, linestyle='-')

# draw ray
maxvals = np.max(pts1, axis=0)
t = (maxvals[0] - rayo[0])/rayd[0]

# plt.plot([rayo[0], maxvals[0]], [rayo[1], rayo[1] + t*rayd[1]], 'r')
plt.arrow(rayo[0], rayo[1], t*rayd[0], t*rayd[1], edgecolor ='r', head_width=0.1, head_length=0.1)

if intersection_pt[0] is not None:
  plt.scatter(intersection_pt[0], intersection_pt[1], c='black')
plt.show()

# -----

