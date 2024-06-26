<div align="center">

# PKG-SUPPORT-RESISTANCE

![Github Actions](https://github.com/pdm-project/pdm/workflows/Tests/badge.svg)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
</div>

## Description
Collection of algorithms to calculate supports and resistances in financial markets.


> [!IMPORTANT]
> ## Supported Algorithms
> | Supported Algorithms   | `Operational`   |
> |:-----------------------|:------------------|
> | `Vanilla Clustering`             | ✅                |
> | `KMeans ML Clustering`               | ✅                |
> | `DBSCAN ML Clustering`               | ✅                |
> | `KNN (DK-Nearest Neighbors) ML`               | ❌                |
> | `RandomForest ML`               | ❌                |
> | `...`               | ❌                |
----


## Installation
```js
pip install pkg-support-resistance
```

## Quick usage
Here's an example to get the gist of using the package.

```python
from pkg_support_resistance import VanillaSupportResistance, KMeansSupportResistance, DBSCANSupportResistance
from pkg_support_resistance.data_set import sr_input_example

# Example input type
# sr_input_example = {
#     "open": [42780, 42834.94, ...],
#     "close": [42834.94, 42961.84, ...],
#     "high": [42901.1, 42986.06, ...],
#     "low": [42730.03, 42795.41, ...],
#     "volume": [173.63661, 169.47648, ...]
# }


# Vanilla algorithms:
sr_result: list[dict] = VanillaSupportResistance.exec_pipeline(input_data=sr_input_example, cluster_threshold=1)
print(sr_result, len(sr_result))


# KMeans ML algorithms:
sr_result: list[dict] = KMeansSupportResistance.exec_pipeline(input_data=sr_input_example, n_clusters=9)
print(sr_result, len(sr_result))


# DBSCAN  ML algorithms:
sr_result: list[dict] = DBSCANSupportResistance.exec_pipeline(input_data=sr_input_example, eps=1000, min_samples=1)
print(sr_result, len(sr_result))

```

## Input example:
```javascript
To see in: "/src/pkg_support_resistance/data_set/example.json"
```

## Output example (Using VanillaSupportResistance algorithm and dataset from '/dataset/example.json'):
```javascript
[
   {
      "pivotPrice": 48184.0,
      "limitsUp": 48495.0,
      "limitsDown": 47347.53,
      "score": 67,
      "accumulatedVolume": 44687.15635
   },
   {
      "pivotPrice": 47534.34,
      "limitsUp": 47874.98,
      "limitsDown": 46763.68,
      "score": 41,
      "accumulatedVolume": 23864.294279999995
   },
   {
      "pivotPrice": 45000.0,
      "limitsUp": 45000.0,
      "limitsDown": 44700.0,
      "score": 8,
      "accumulatedVolume": 6010.54166
   },
   {
      "pivotPrice": 43996.5,
      "limitsUp": 44141.37,
      "limitsDown": 43100.0,
      "score": 40,
      "accumulatedVolume": 17909.42211
   },
   {
      "pivotPrice": 43473.45,
      "limitsUp": 43580.0,
      "limitsDown": 42697.01,
      "score": 37,
      "accumulatedVolume": 18501.36496
   },
   {
      "pivotPrice": 42819.86,
      "limitsUp": 42850.0,
      "limitsDown": 42041.7,
      "score": 15,
      "accumulatedVolume": 6355.429050000001
   },
   {
      "pivotPrice": 42259.58,
      "limitsUp": 42787.38,
      "limitsDown": 42017.33,
      "score": 24,
      "accumulatedVolume": 12506.830009999998
   },
   {
      "pivotPrice": 41619.99,
      "limitsUp": 42365.48,
      "limitsDown": 41115.0,
      "score": 91,
      "accumulatedVolume": 42944.990900000004
   },
   {
      "pivotPrice": 41071.29,
      "limitsUp": 41157.26,
      "limitsDown": 40753.88,
      "score": 8,
      "accumulatedVolume": 4474.11918
   }
]
```

### pivotPrice:
Support/resistance line.

### limitsUp/limitsDown:
Support/resistance zone.

### Score, support/resistance score:
If the score is high it means that many candles have been traded in that area with a high volume being traded, on the other hand a low score may be due to the fact that it is not a highly traded area or that it belongs to a higher maximum or lower minimum (very important zones, but not surpassed in the short term and low negotiation).

### accumulatedVolume:
Accumulated volume traded in the consolidated zone between limitsUp/limitsDown.

## Graph of the 'pivotPrice' S/R (Using VanillaSupportResistance algorithm and dataset from '/dataset/example.json'):
<img src="src/pkg_support_resistance/vanilla/plot/vanilla_algo_plot.png">


## Cythonize this package [OPTIONAL].
Cythonizing the package will improve the performance of the algorithms, but keep in mind that the algorithms are already highly efficient and optimal, so the improvement with Cythonization will be minimal and imperceptible.

Right click on the root of pkg_support_resistance (in the virtual environment), and open in the integrated terminal.

```bash
# Root, I.e.: venv/lib/python3.12/site-packages/pkg_support_resistance/setup.py
# In the integrated terminal run:

pip install cython
python setup.py build_ext --inplace
```


```python
from pkg_support_resistance import VanillaSupportResistance


# Vanilla algorithms is cythonized?
module_is_cythonized: bool = VanillaSupportResistance.is_cythonized()
print(module_is_cythonized)

> True # This algorithm is cythonized

```
