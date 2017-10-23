---
title: "NetTools"
excerpt: "Package which groups different tools for network study. It is composed by network structure and network evolution."
collection: software
type: "Software package"
date: 2016-03-01
permalink: /software/NetTools
header:
  overlay_image: software/complex-network2.png
  overlay_filter: 0.4
  caption: ""
  cta_label: "Download"
  cta_url: "https://github.com/tgquintela/NetTools/archive/master.zip"
---

[![Build Status](https://travis-ci.org/tgquintela/NetTools.svg?branch=master)](https://travis-ci.org/tgquintela/NetTools)
[![Coverage Status](https://coveralls.io/repos/github/tgquintela/NetTools/badge.svg?branch=master)](https://coveralls.io/github/tgquintela/NetTools?branch=master)


Package which groups different tools for network study. It is composed by network structure and network evolution.

# Version
__version__ = '0.0.0'


# Example
```python
from NetTools.NetSymulationTools.dynamics_evolution import meta_evolution
from NetTools.NetSymulationTools.net_formation import grid_2d_graph_2order
from NetTools.NetSymulationTools.aux_functions import initialization_states

net = grid_2d_graph_2order(n, m)
init = initialization_states(n*m)

dyn = meta_evolution(net, n_steps=steps, pre_states=init, t_mem=5)
```

# TODO
* possibility to change network along the dynamics
* general variables of the system

