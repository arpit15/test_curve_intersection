import numpy as np
from time import time
from ipdb import set_trace
largeval = 1e7

def intersection(curve, verts, rayo, rayd, timeit=True, verbose=False):
  # STEP 1: condiser intersection with lines going through control points
  # STEP 2: find exact root for that segment only

  start = time()
  # verts = vertices
  # find line-ray intersection 
  tvals = []
  numverts = verts.shape[0]
  # can be done in parallel
  for i in range(numverts-1):
    v0 = verts[i]
    v1 = verts[i+1]

    A = np.vstack( (v0-v1, - rayd)).T
    b = rayo - v1

    u,t = np.linalg.inv(A)@b

    if u>=0 and u<=1 and t>=0:
      tvals.append(t)
    else:
      tvals.append(largeval)

  # use smallest t val
  tmin_id = np.argmin(tvals)
  tmin = tvals[tmin_id]

  end_line = time()
  if timeit: print(f"Line intersection time: {end_line - start:.3f}")

  if tmin == largeval:
    print("No intersection was found")
    return [None, None]
  else:
    print(f"Segment {tmin_id} intersects")
    # fake pt
    # tmin = tvals[tmin_id]
    # pt = rayo + tmin*rayd
    # return pt


  basis = curve.segments[tmin_id]

  # solve cubic for this segment
  # find cubic coefficient
  b1, b2 = np.hsplit(basis, 2)
  d1, d2 = rayd
  o1, o2 = rayo

  lhs = b2*d1 - b1*d2
  rhs = o2*d1 - o1*d2

  lhs[-1] = lhs[-1] - rhs
  
  tcubic = np.roots(lhs.flatten())
  if verbose: print(tcubic)

  end_cubic = time()
  if timeit: print(f"Line intersection time: {end_cubic - end_line:.3f}")

  treal = largeval
  for sol in tcubic:
    if np.imag(sol) == 0 and np.real(sol) > 0:
      treal = np.minimum(np.real(sol), treal)

  if treal == largeval or treal<0 or treal>1:
    print("No real sol found")
    return [None, None]
  else:
    print(f"real tcubic solution : {treal}")
    x = np.polyval(basis[:,0], treal)
    y = np.polyval(basis[:,1], treal)
    return [x,y]


  

