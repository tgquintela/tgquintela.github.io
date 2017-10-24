---
title: "TimeSeriesTools"
excerpt:"Package which extends python tools for time series analysis."
collection: software
type: "Software package"
date: 2016-02-01
permalink: /software/TimeSeriesTools
header:
  overlay_image: software/TimeSeries.png
  overlay_filter: 0.4
  caption: ""
  cta_label: "Download"
  cta_url: "https://github.com/tgquintela/TimeSeriesTools/archive/master.zip"
---

[![Build Status](https://travis-ci.org/tgquintela/TimeSeriesTools.svg?branch=master)](https://travis-ci.org/tgquintela/TimeSeriesTools)
[![Coverage Status](https://coveralls.io/repos/github/tgquintela/TimeSeriesTools/badge.svg?branch=master)](https://coveralls.io/github/tgquintela/TimeSeriesTools?branch=master)

Package to create tools in order to deal with groups of time series. The purpose of that software is to use, extend and complement the main tools and packages used in python.
The software structure of this package is functional oriented but it is expected to be complemented in the future. The main utilities of this package are:
* Transform the time series (Filtering, Windowing transformation, value discretization and temporal discretization).
* Measure some quantities in the time series.
* Measure distances between some time series.
* Regime detection in time series.
* Prediction of next states of the time series.
* Infer causality network structure from a timeseries system.

# Version
```python
__version__ = 0.0.0
```

# TODO
- [X] DTW
- [ ] Pattern matching
- [ ] Statistical thresholding
- [ ] More measures
- [ ] Standarize causality networks inference

