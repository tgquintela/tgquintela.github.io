---
title: "ChaosFunctions"
excerpt: "Package to simulate 1d and 2d dynamical processes which can produce chaotic behaviour."
collection: software
type: "Software package"
date: 2015-10-01
permalink: /software/ChaosFunctions
header:
  overlay_image: software/fractals.png
  overlay_filter: 0.4
  caption: "Fractals created with that program"
  cta_label: "Download"
  cta_url: "https://github.com/tgquintela/ChaosFunctions/archive/master.zip"
---


Collection of functions related with dynamical systems

The main utilities of this package are

* Create chaotic iterations
* Build fractals in complex plane

# Installation

```Bash
git clone https://github.com/tgquintela/ChaosFunctions
.\install.sh
```

Required extra packages
* pythonUtils
```Bash
git clone https://github.com/tgquintela/pythonUtils
```


# Examples

* Chaotic series

```python
from ChaosFunctions.chaotic_evolution import Iterator
iter_f = lambda x: x/2 if x%2==0 else 3*x+1
stop_f = lambda x: x[-1] == 1
it = Iterator(iter_f, stop_f)
sequence = it.iterate_sequence(124)
fig = plot_sequence(sequence)
```

* Build a fractal

```python
import numpy as np
from ChaosFunctions.fractals import FractalBuilder, mandelbrot_iter
ns, itermax, limits = (1000, 1000), 400, np.array([[-2, .5], [-1.25, 1.25]])
fb = FractalBuilder(mandelbrot_iter, p0_mandelbrot)
img = fb.build_fractal(ns, limits, itermax)
fig = fb.export_fractal(img, 'prueba')
```



