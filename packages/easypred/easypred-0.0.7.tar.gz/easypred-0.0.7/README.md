# EasyPred: track your predictions with ease
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub license](https://badgen.net/github/license/FilippoPisello/EasyPred)](https://github.com/FilippoPisello/EasyPred/blob/main/LICENSE)
[![PyPI version fury.io](https://badge.fury.io/py/easypred.svg)](https://pypi.org/project/easypred/)
[![Documentation Status](https://readthedocs.org/projects/easypred/badge/?version=latest)](https://easypred.readthedocs.io/en/latest/?badge=latest)
## What is it?
EasyPred is a Python package that allows to easily store, investigate, assess and compare the predictions obtained through your Machine Learning models.

The package allows to create different types of model-agnostic prediction objects simply by passing the real and fitted data. These objects have properties and methods that return various accuracy and error metrics.

Why EasyPred can be useful:
- **All-in-one bundle**: having data and accuracy metrics in a single object means less stuff you need to keep an eye on
- **Minimize code redundancy**: pass the data once and get all the information and metrics you want
- **Easy and flexible comparison**: create the predictions first and then decide what to compare. Changed your mind? The object is there, simply access another method

## Quick Start
### Installation
You can install EasyPred via `pip`
```
pip install easypred
```
Alternatively, you can install EasyPred by cloning the project to your local directory
```
git clone https://github.com/FilippoPisello/EasyPred
```
And then run `setup.py`
```
python setup.py install
```
### Usage
At the moment, three types of predictions are implemented:
- **Prediction** -> any prediction
- **BinaryPrediction** -> fitted and real data attain only two values
- **NumericPrediction** -> fitted and real data are numeric

#### Prediction
Consider the example of a generic prediction over text categories:
```python
>>> real_data = ["Foo", "Foo", "Bar", "Bar", "Baz"]
>>> fitted_data = ["Baz", "Bar", "Foo", "Bar", "Bar"]

>>> from easypred import Prediction
>>> pred = Prediction(real_data, fitted_data)
```
Let's check the rate of correctly classified observations:
```python
>>> pred.accuracy_score
0.2
```
More detail is needed, let's investigate where predictions and real match:
```python
>>> pred.matches()
array([False, False, False,  True, False])
```
Still not clear enough, display everything in a data frame:
```python
>>> pred.as_dataframe()
  Real Values Fitted Values  Prediction Matches
0         Foo           Baz               False
1         Foo           Bar               False
2         Bar           Foo               False
3         Bar           Bar                True
4         Baz           Bar               False
```
#### BinaryPrediction
Consider the case of a classic binary context (note: the two values can be any value, no need to be 0 and 1):
```python
>>> real_data = [1, 1, 0, 0]
>>> fitted_data = [0, 1, 0, 0]
>>> from easypred import BinaryPrediction
>>> bin_pred = BinaryPrediction(real_data, fitted_data, value_positive=1)
```
What are the false positive and false negative rates? What about sensitivity and specificity?
```python
>>> bin_pred.false_positive_rate
0.0
>>> bin_pred.false_negative_rate
0.5
>>> bin_pred.recall_score
0.5
>>> bin_pred.specificity_score
1.0
```
Let's look now at the confusion matrix as a pandas data frame:
```python
>>> bin_pred.confusion_matrix(as_dataframe=True)
        Pred 0  Pred 1
Real 0       2       0
Real 1       1       1
```
#### NumericPrediction
Let's look at the numeric use case:
```python
>>> real_data = [1, 2, 3, 4, 5, 6, 7]
>>> fitted_data = [1, 2, 4, 3, 7, 2, 5]
>>> from easypred import NumericPrediction
>>> num_pred = NumericPrediction(real_data, fitted_data)
```
We can access the residuals with various flavours, let's go for the basic values:
```python
>>> num_pred.residuals(squared=False, absolute=False, relative=False)
array([ 0,  0, -1,  1, -2,  4,  2])
```
The data frame representation has now more information:
```python
>>> num_pred.as_dataframe()
   Fitted Values  Real Values  Prediction Matches  Absolute Difference  Relative Difference
0              1            1                True                    0             0.000000
1              2            2                True                    0             0.000000
2              4            3               False                   -1            -0.333333
3              3            4               False                    1             0.250000
4              7            5               False                   -2            -0.400000
5              2            6               False                    4             0.666667
6              5            7               False                    2             0.285714
```
There are then a number of dedicated error and accuracy metrics:
```python
>>> num_pred.mae
1.4285714285714286
>>> num_pred.mse
3.7142857142857144
>>> num_pred.rmse
1.927248223318863
>>> num_pred.mape
0.27653061224489794
>>> num_pred.r_squared
0.31250000000000017
```
Use the `help()` function to get more information over the prediction objects and their functionalities.

## Dependencies
EasyPred depends on the following libraries:
- NumPy
- pandas
- matplotlib

## Documentation
Find the complete documentation on [read the docs](https://easypred.readthedocs.io/en/latest/easypred.html).

## License
[MIT](LICENSE)