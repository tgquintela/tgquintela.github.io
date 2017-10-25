---
layout: default
title: "Preprocessing Timeseries"
collection: notebooks
permalink: /notebooks/preprocessing_ts
date: 2017-10-01
---

{% include base_path %}

# Data Scientist Challenge

In this coding challenge, you will analyze the real Blood Glucose variability and the iPhone-detected motion
activities of somobody. He's not a diabetic, but you never know. You will develop some Python functions and
modules, and some very basic statistical analysis. The main point of this challenge is to check your coding
skills, and how much you are at ease with performing some elementary statistical analysis.

## Input data

You have two files available:
* `blood-glucose.csv` is a CSV file with each line reporting a timestamp and a blood glucose level
(expressed in mg/dL), measured every 15 minutes. Please note that some values are missing.
* `motion.tsv` is a TSV file with each line reporting a timestamp and 5 boolean values. Each of these
boolean values refer to a type of activity, respectively 'stationary', 'walking', 'running', 'automotive' and
'cycling'. These must be interpreted in this way: when the user starts to walk, a line with 1 in the
walking position is reported; when the user stops walking, a line with 0 in that position is reported.
The whole period in between should be interpreted as walking. The same goes for the other activities.

Consider that it is possible to have multiple activities at the same time (for example, stationary and
automotive: think of being on a bus), and it's also possible to have no activities recognized at a given
time (meaning we don't know).


```python
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import matplotlib.pyplot as plt
from ts_tools import get_ts_range, get_times_by_interval, get_floor_range, get_ceil_range
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

```


```python
## Functions definition
import datetime
import numpy as np


def get_ts_range(init_dt, end_dt, ts_range=900):
    time_ranges = []
    i = 0
    while (init_dt+i*datetime.timedelta(seconds=ts_range)) <= end_dt:
        time_ranges.append(init_dt+i*datetime.timedelta(seconds=ts_range))
        i += 1
    return time_ranges


def get_times_by_interval(dt_ini, dt_end):
    # Compute floor and ceil interval limits
    init = datetime.datetime(dt_ini.year, dt_ini.month, dt_ini.day, dt_ini.hour, dt_ini.minute - (dt_ini.minute % 15), 0)
    endt = datetime.datetime(dt_end.year, dt_end.month, dt_end.day, dt_end.hour, dt_end.minute - (dt_end.minute % 15), 0)
    endt = endt + datetime.timedelta(seconds=900)
    
    # Assign times
    interval_ranges = get_ts_range(init, endt, 900)
    times = np.zeros(len(interval_ranges))
    times[0] = (dt_ini - interval_ranges[0]).total_seconds()
    times[-1] = (interval_ranges[-1] - dt_end).total_seconds()
    times[1:-1] = 900
    
    return interval_ranges, times

```


```python
blood_glucose = pd.read_csv('input/blood-glucose.csv', header=None, names=['times', 'blood_glucose'])
blood_glucose = blood_glucose[~ pd.isnull(blood_glucose['blood_glucose'])]
blood_glucose['times'] = blood_glucose['times'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+00:00'))
```


```python
blood_glucose.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>times</th>
      <th>blood_glucose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>42</th>
      <td>2017-05-23 10:30:00</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>2017-05-23 10:45:00</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2017-05-23 11:00:00</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2017-05-23 11:15:00</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>2017-05-23 11:30:00</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
motion = pd.read_csv('input/motion.tsv', sep='\t', names=['times', 'stationary', 'walking', 'running', 'automotive', 'cycling'], header=None)
motion['times'] = motion['times'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f+00:00'))
```


```python
motion.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>times</th>
      <th>stationary</th>
      <th>walking</th>
      <th>running</th>
      <th>automotive</th>
      <th>cycling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13117</th>
      <td>2017-06-02 23:52:16.418372</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13118</th>
      <td>2017-06-02 23:54:18.267440</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13119</th>
      <td>2017-06-02 23:54:21.136673</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13120</th>
      <td>2017-06-02 23:57:19.966934</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13121</th>
      <td>2017-06-02 23:57:25.666652</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get time ranges of the whole data
init_dt = datetime.datetime(2017, 5, 23, 0, 0)
end_dt = datetime.datetime(2017, 6, 3, 0, 0)
time_ranges = get_ts_range(init_dt, end_dt, 900)
```


```python
times = list(motion['times'])
times_intervals = np.zeros((len(time_ranges), 5))
col_activities = ['stationary', 'walking', 'running', 'automotive', 'cycling']

for i_col, col in enumerate(col_activities):
    idxs = np.where(np.diff(motion[col].as_matrix()) == -1)[0]
    # For each interval of activity
    for i in idxs:
        dt_ini = times[i]
        dt_end = times[i+1]
        # Fill times activity
        interval_ranges, times_intervals_range = get_times_by_interval(dt_ini, dt_end)
        
        i_init = time_ranges.index(interval_ranges[0])
        for i_i in range(len(times_intervals_range)):
            times_intervals[i_init + i_i, i_col] += times_intervals_range[i_i]

```


```python
times_activities_48h = time_ranges[192:]
times_intervals_48h = np.zeros((len(times_intervals)-192, 5))
std_intervals_48h = np.zeros((len(times_intervals)-192, 5))

for i in range(len(times_intervals)-192):
    times_intervals_48h[i] = times_intervals[i:i+192].sum(0)
    std_intervals_48h[i] = times_intervals[i:i+192].std(0)

```


```python
# Compute and interpolate blood glucose
init_time = get_floor_range(blood_glucose.times.iloc[0], 15)
endt_time = get_ceil_range(blood_glucose.times.iloc[-1], 15)
time_ranges_blood = get_ts_range(init_time, endt_time, 900)

blood_glucose_interp = np.zeros(len(time_ranges_blood))
blood_times = list(blood_glucose.times)
for i_time in range(len(blood_times)):
    try:
        idx = time_ranges_blood.index(blood_times[i_time])
        blood_glucose_interp[idx] = blood_glucose.blood_glucose.iloc[i_time]
    except:
        pass

idxs = np.where(blood_glucose_interp)[0]
# TOImprove: better interpolation
blood_glucose_interp = np.interp(range(len(blood_glucose_interp)), idxs, blood_glucose_interp[idxs])

```


```python
# Compute the std of the blood glucose level on the last 48h
blood_glucose_std_48h = np.zeros(len(blood_glucose_interp)-192)
for i in range(len(blood_glucose_interp)-192):
    blood_glucose_std_48h[i] = blood_glucose_interp[i:i+192].std(0)
time_ranges_blood_48h = time_ranges_blood[192:]
```


```python
# Compute std blood glucose
walking_time_48h = np.zeros(len(time_ranges_blood_48h))
for i_time in range(len(times_intervals_48h)):
    try:
        idx = time_ranges_blood_48h.index(times_48h[i_time])
        walking_time_48h[idx] = times_intervals_48h[i_time, 1]
    except:
        pass
    
times_48h = time_ranges_blood_48h

```


```python
walking_time_at_interval = np.zeros(len(times_48h))
for i_time in range(len(walking_time_at_interval)):
    try:
        idx = times_48h.index(time_ranges[i_time])
        walking_time_at_interval[idx] = times_intervals[i_time, 1]
    except:
        pass
```

### Plots of computed values


```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

for i_col in range(5):
    plt.plot(times_activities_48h, times_intervals_48h[:, i_col], label=col_activities[i_col])

_ = plt.legend()

```

<img src="{{base_path}}/images/notebooks/blood_glucose/output_18_0.png">



```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

for i_col in range(5):
    plt.plot(times_activities_48h, times_intervals_48h[:, i_col], label=col_activities[i_col])

ax.set_yscale('log')
_ = plt.legend()
```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_19_0.png">



```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

for i_col in range(5):
    plt.plot(times_activities_48h, std_intervals_48h[:, i_col], label=col_activities[i_col])

_ = plt.legend()
```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_20_0.png">



```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

for i_col in range(5):
    plt.plot(times_activities_48h, std_intervals_48h[:, i_col], label=col_activities[i_col])

ax.set_yscale('log')
_ = plt.legend()
```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_21_0.png">



```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

_ = plt.plot(times_48h, walking_time_at_interval)

```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_22_0.png">


### Correlation


```python
np.correlate(walking_time_48h, blood_glucose_std_48h)[0]
```




    0.0




```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))


diff_walking = np.diff(walking_time_48h)
diff_blood_glucose = np.diff(blood_glucose_std_48h)

plt.plot(times_48h[:-1], diff_walking/np.std(diff_walking), label="Walking time in the last 48h")
plt.plot(times_48h[:-1], diff_blood_glucose/np.std(diff_blood_glucose), label="std of blood glucose levels of the last 48h")

_ = plt.legend()
```

    /opt/conda/lib/python3.6/site-packages/ipykernel/__main__.py:8: RuntimeWarning: invalid value encountered in true_divide



<img src="{{base_path}}/images/notebooks/blood_glucose/output_25_1.png">



```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

_ = plt.plot(walking_time_48h, blood_glucose_std_48h, '.')

```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_26_0.png">



```python
## Plot
fig, ax = plt.subplots(figsize=(18, 10))

over_logi = blood_glucose_std_48h > 12.5
under_logi = np.logical_not(over_logi)

_ = plt.plot(walking_time_48h[under_logi], blood_glucose_std_48h[under_logi], '.')
_ = plt.plot(walking_time_48h[over_logi], blood_glucose_std_48h[over_logi], '.')

_ = plt.plot(np.linspace(walking_time_48h.min(), walking_time_48h.max(), 100), 12.5*np.ones(100), linestyle='dashed')


```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_27_0.png">



```python
## Plot of correlation of walking in that time
fig, ax = plt.subplots(figsize=(18, 10))

walking_time_at_interval

over_logi = blood_glucose_std_48h > 12.5
under_logi = np.logical_not(over_logi)

_ = plt.plot(walking_time_at_interval[under_logi], blood_glucose_std_48h[under_logi], '.')
_ = plt.plot(walking_time_at_interval[over_logi], blood_glucose_std_48h[over_logi], '.')

_ = plt.plot(np.linspace(walking_time_at_interval.min(), walking_time_at_interval.max(), 100), 12.5*np.ones(100), linestyle='dashed')

```


<img src="{{base_path}}/images/notebooks/blood_glucose/output_28_0.png">


### Prediction


```python
## Dummy model
model = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True)
param_grid = { 
    'penalty': ['l2'],
    'C': [0.1, 1., 10.]
}

CV_model = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
CV_model.fit(walking_time_48h.reshape(-1, 1), blood_glucose_std_48h>14.5)

```




    GridSearchCV(cv=5, error_score='raise',
           estimator=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False),
           fit_params={}, iid=True, n_jobs=1,
           param_grid={'penalty': ['l2'], 'C': [0.1, 1.0, 10.0]},
           pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
           scoring=None, verbose=0)




```python
CV_model.best_score_
```




    0.89281210592686




```python
CV_model.predict_proba([[100000]])
```




    array([[ 0.86895632,  0.13104368]])




```python
CV_model.predict_proba([[350000]])
```




    array([[ 0.86895632,  0.13104368]])




```python
## Store trained model
joblib.dump(CV_model, 'model_blood_glucose.pkl')

```




    ['model_blood_glucose.pkl']




```python
### Prediction using walking times in each moment
# Dummy model
model = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True)
param_grid = { 
    'penalty': ['l2'],
    'C': [0.1, 1., 10.]
}

CV_model = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
CV_model.fit(walking_time_at_interval.reshape(-1, 1), blood_glucose_std_48h>14.5)

```




    GridSearchCV(cv=5, error_score='raise',
           estimator=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False),
           fit_params={}, iid=True, n_jobs=1,
           param_grid={'penalty': ['l2'], 'C': [0.1, 1.0, 10.0]},
           pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
           scoring=None, verbose=0)




```python
CV_model.best_score_
```




    0.89281210592686




```python
CV_model.predict_proba([[8000]])
```




    array([[ 0.91783258,  0.08216742]])




```python
CV_model.predict_proba([[0]])
```




    array([[ 0.86444132,  0.13555868]])




```python
## Store trained model
joblib.dump(CV_model, 'model_interval_blood_glucose.pkl') 
```




    ['model_interval_blood_glucose.pkl']


