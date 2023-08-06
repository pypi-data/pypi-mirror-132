# **LINEAR REGRESSOR**
This is a module of numerical statistic prediction using linear regression by determinant matrix method with intercept, slope, correlation coefficient, and determination coefficient calculations
### **By Zaafirrahman**


## **Installation**

This library can be installed by the pip command, open your terminal and type in the following command...

```python
pip install linearregressor
```

## **Functions of this library**

First import the library using this command 
```python
import linearregressor as lr
```
 and then proceed to call the functions
 
 
## **The parameters**

**x (train independent variable)** - Dataframe of independent variable from train data

**y (train dependent variable)** - Series of dependent variable from train data

**test (test independent variable)** - Dataframe of independent variable from test data


## Prediction

## `lr.predict(x,y,test)`

This function can be used to predict dependent test data from given independent test data (test) by coefficient calculation from given dependent (y) and independent train data (x)

**Example :**

Given a train data with correlation between dependent and independent variable as shown below:

| X1   | X2   | Y    |
| ---- | ---- | ---- |
| 10   | 7    | 23   |
| 2    | 3    | 7    |
| 4    | 2    | 15   |
| 6    | 4    | 17   |
| 8    | 6    | 23   |
| 7    | 5    | 22   |
| 4    | 3    | 10   |
| 6    | 3    | 14   |
| 7    | 4    | 20   |
| 6    | 3    | 19   |

Based on train data above, predict the dependent value from test data below:

| X1   | X2   |
| ---- | ---- |
| 9    | 6    |
| 5    | 4    |
| 7    | 5    |
| 8    | 6    |
| 5    | 6    |
| 4    | 2    |
| 9    | 5    |
| 10   | 8    |
| 6    | 7    |
| 7    | 3    |

Code:
```python
# Create train data as pandas dataframe format
df = pd.DataFrame({'Y':[23,7,15,17,23,22,10,14,20,19],
                   'X1':[10,2,4,6,8,7,4,6,7,6],
                   'X2':[7,3,2,4,6,5,3,3,4,3]})
# For simplest way, you can just import your csv file using pd.read_csv() function

# Split between dependent and independent data
y = df['Y']
x = df.drop(['Y'],axis=1)

# Create test data as pandas dataframe format and predict the dependent value
df_test = pd.DataFrame({'X1':[9,5,7,8,5,4,9,10,6,7],
                        'X2':[6,4,5,6,6,2,5,8,7,3]})
lr.predict(x,y,df_test)
```
Output:
```
[23.540636042402866,
 14.508833922261505,
 19.024734982332188,
 21.04946996466434,
 13.575971731448758,
 12.950530035335726,
 24.00706713780924,
 25.098939929328644,
 15.600706713780912,
 19.957597173144933]
```

## Intercept

## `lr.intercept(x,y)`

This function can be used to find intercept value from dependent (y) and independent train data (x)

**Example:**

With the same train data, you can find the intercept value of the data

```python
>>> lr.intercept(x,y)
3.918727915194365
```
As shown in the output, it can be concluded that if the value of the independent variable is constant, then the average value of the dependent variable is `3.918727915194365`


## Slope

## `lr.slope(x,y)`

This function can be used to find slope value from dependent (y) and independent train data (x)

**Example:**

With the same train data, you can find the slope value of the data

```python
>>> lr.slope(x,y)
[2.4911660777385274, -0.46643109540637395]
```
As shown in the output, it can be concluded that if the value of X1 increases by 1 unit, it will **increase** the value of the dependent variable by `2.4911660777385274` because the coefficient is marked (+) which means the effect is **positive**.
Meanwhile, if the value of X2 increases by 1 unit, it will **decrease** the value of the dependent variable by `0.46643109540637395` because the coefficient is marked (-) which means the effect is **negative**.


## Correlation Coefficient

## `lr.r(x,y)`

This function can be used to find correlation coefficient from dependent (y) and independent train data (x)

**Example:**

With the same train data, you can find the correlation coefficient of the data

```python
>>> lr.r(x,y)
0.9145723194701728
```
As shown in the output, it can be concluded that between the independent variable and the dependent variable, which has a very strong correlation because the correlation coefficient is very close to 1.


## Determination Coefficient

## `lr.rsquare(x,y)`

This function can be used to find determination coefficient from dependent (y) and independent train data (x)

**Example:**

With the same train data, you can find the determination coefficient of the data

```python
>>> lr.rsquare(x,y)
0.8364425275410518
```
As shown in the output, it can be concluded that the value of the independent variable affects `0.8364425275410518` or `83.64%` of the value of the dependent variable, while the remaining `16.36%` is influenced by other variables.


## Regression Information

## `lr.info(x,y)`

This function can be used to easily show the information of your data such as constant (intercept), coefficient (slope), multiple r (correlation coefficient), and r squared (determination coefficient) together in just one function

**Example:**

With the same train data, you can show the whole regression information about your data

```python
>>> lr.info(x,y)
Constant :  3.918727915194365
Coefficient_1 : 2.4911660777385274
Coefficient_2 : -0.46643109540637395
Multiple R :  0.9145723194701728
R Squared :  0.8364425275410518
```
