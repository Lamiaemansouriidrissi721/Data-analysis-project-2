```python
import pandas as pd 

```


```python
data= pd.read_csv(r"C:\Users\kumak\Desktop\selfstudy\Python\project 2.csv")
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265.0</td>
      <td>17.0</td>
      <td>23.0</td>
      <td>4451.0</td>
      <td>106.0</td>
      <td>189.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>20.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>20.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>432 rows × 15 columns</p>
</div>




```python
data.isnull().sum()
```




    Make           4
    Model          4
    Type           4
    Origin         4
    DriveTrain     4
    MSRP           4
    Invoice        4
    EngineSize     4
    Cylinders      6
    Horsepower     4
    MPG_City       4
    MPG_Highway    4
    Weight         4
    Wheelbase      4
    Length         4
    dtype: int64




```python
data.dtypes
```




    Make            object
    Model           object
    Type            object
    Origin          object
    DriveTrain      object
    MSRP            object
    Invoice         object
    EngineSize     float64
    Cylinders      float64
    Horsepower     float64
    MPG_City       float64
    MPG_Highway    float64
    Weight         float64
    Wheelbase      float64
    Length         float64
    dtype: object




```python
data.fillna(data.mean(), inplace=True)
data
```

    C:\Users\kumak\AppData\Local\Temp\ipykernel_14980\3452971976.py:1: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
      data.fillna(data.mean(), inplace=True)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265.0</td>
      <td>17.0</td>
      <td>23.0</td>
      <td>4451.0</td>
      <td>106.0</td>
      <td>189.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>20.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>20.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>432 rows × 15 columns</p>
</div>




```python
data.isnull().sum()
```




    Make           4
    Model          4
    Type           4
    Origin         4
    DriveTrain     4
    MSRP           4
    Invoice        4
    EngineSize     0
    Cylinders      0
    Horsepower     0
    MPG_City       0
    MPG_Highway    0
    Weight         0
    Wheelbase      0
    Length         0
    dtype: int64




```python
#slice the data to better control what iam working on without effecting other values
selected_columns = ['Make', 'Model', 'Type', 'Origin', 'DriveTrain', 'MSRP', 'Invoice']
sliced_data = data[selected_columns]

sliced_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
    </tr>
  </tbody>
</table>
<p>432 rows × 7 columns</p>
</div>




```python
sliced_data.isnull().sum()
```




    Make          4
    Model         4
    Type          4
    Origin        4
    DriveTrain    4
    MSRP          4
    Invoice       4
    dtype: int64




```python
sliced_data.dtypes
```




    Make          object
    Model         object
    Type          object
    Origin        object
    DriveTrain    object
    MSRP          object
    Invoice       object
    dtype: object




```python
# Fill missing values in object columns with a specific value (e.g., 'Unknown')
object_columns = data.select_dtypes(include=['object']).columns
data[object_columns] = data[object_columns].fillna('Unknown')
```


```python
data.isnull().sum()
```




    Make           0
    Model          0
    Type           0
    Origin         0
    DriveTrain     0
    MSRP           0
    Invoice        0
    EngineSize     0
    Cylinders      0
    Horsepower     0
    MPG_City       0
    MPG_Highway    0
    Weight         0
    Wheelbase      0
    Length         0
    dtype: int64




```python
# Fill missing values in numerical columns with the mean
numerical_columns = data.select_dtypes(include=['int', 'float']).columns
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].mean())

# Fill missing values in object columns with 'Unknown'
object_columns = data.select_dtypes(include=['object']).columns
data[object_columns] = data[object_columns].fillna('Unknown')

data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265.0</td>
      <td>17.0</td>
      <td>23.0</td>
      <td>4451.0</td>
      <td>106.0</td>
      <td>189.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>20.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>20.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>432 rows × 15 columns</p>
</div>




```python
data.isnull().sum()
```




    Make           0
    Model          0
    Type           0
    Origin         0
    DriveTrain     0
    MSRP           0
    Invoice        0
    EngineSize     0
    Cylinders      0
    Horsepower     0
    MPG_City       0
    MPG_Highway    0
    Weight         0
    Wheelbase      0
    Length         0
    dtype: int64




```python
#Check what are the different types of Make are there in our dataset
```


```python
data['Make'].dtypes
```




    dtype('O')




```python
unique_makes = data['Make'].unique()
print(unique_makes)

```

    ['Acura' 'Audi' 'BMW' 'Unknown' 'Buick' 'Cadillac' 'Chevrolet' 'Chrysler'
     'Dodge' 'Ford' 'GMC' 'Honda' 'Hummer' 'Hyundai' 'Infiniti' 'Isuzu'
     'Jaguar' 'Jeep' 'Kia' 'Land Rover' 'Lexus' 'Lincoln' 'MINI' 'Mazda'
     'Mercedes-Benz' 'Mercury' 'Mitsubishi' 'Nissan' 'Oldsmobile' 'Pontiac'
     'Porsche' 'Saab' 'Saturn' 'Scion' 'Subaru' 'Suzuki' 'Toyota' 'Volkswagen'
     'Volvo']
    


```python
data['Make'].value_counts()
```




    Toyota           28
    Chevrolet        27
    Mercedes-Benz    26
    Ford             23
    BMW              20
    Audi             19
    Nissan           17
    Honda            17
    Chrysler         15
    Volkswagen       15
    Mitsubishi       13
    Dodge            13
    Hyundai          12
    Jaguar           12
    Volvo            12
    Kia              11
    Mazda            11
    Lexus            11
    Pontiac          11
    Subaru           11
    Lincoln           9
    Mercury           9
    Buick             9
    Saturn            8
    Infiniti          8
    GMC               8
    Cadillac          8
    Suzuki            8
    Porsche           7
    Saab              7
    Acura             7
    Unknown           4
    Oldsmobile        3
    Jeep              3
    Land Rover        3
    MINI              2
    Scion             2
    Isuzu             2
    Hummer            1
    Name: Make, dtype: int64




```python
#And, what is the count (occurrence) of each Make in the data ?
len(unique_makes)
```




    39




```python
#Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.
```


```python
filer_byOrigine= data[(data['Origin'] =='Asia') | (data['Origin'] =='Europe')]
```


```python
filer_byOrigine
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265.0</td>
      <td>17.0</td>
      <td>23.0</td>
      <td>4451.0</td>
      <td>106.0</td>
      <td>189.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>20.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>20.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>281 rows × 15 columns</p>
</div>




```python
#using .isin and storing it in records
```


```python
records=data[data['Origin'].isin(['Europe','Asia'])]
records
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265.0</td>
      <td>17.0</td>
      <td>23.0</td>
      <td>4451.0</td>
      <td>106.0</td>
      <td>189.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>20.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>20.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>281 rows × 15 columns</p>
</div>




```python
#Q. 4)  Remove all the records (rows) where Weight is above 4000.
```


```python
#i, goin to use this sign ~ inorder to delete the rows in which weight is above 4000
data[~ (data['Weight'] > 4000)]

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>20.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Acura</td>
      <td>3.5 RL w/Navigation 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$46,100</td>
      <td>$41,100</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>18.0</td>
      <td>24.0</td>
      <td>3893.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>20.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>329 rows × 15 columns</p>
</div>




```python
# Increase all the values of 'MPG_City' column by 3
```


```python
data['MPG_City']=data['MPG_City'].apply(lambda x:x+3)
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265.0</td>
      <td>20.0</td>
      <td>23.0</td>
      <td>4451.0</td>
      <td>106.0</td>
      <td>189.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>27.0</td>
      <td>31.0</td>
      <td>2778.0</td>
      <td>101.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200.0</td>
      <td>25.0</td>
      <td>29.0</td>
      <td>3230.0</td>
      <td>105.0</td>
      <td>183.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270.0</td>
      <td>23.0</td>
      <td>28.0</td>
      <td>3575.0</td>
      <td>108.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225.0</td>
      <td>21.0</td>
      <td>24.0</td>
      <td>3880.0</td>
      <td>115.0</td>
      <td>197.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197.0</td>
      <td>24.0</td>
      <td>28.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242.0</td>
      <td>23.0</td>
      <td>26.0</td>
      <td>3450.0</td>
      <td>105.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>429</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268.0</td>
      <td>22.0</td>
      <td>26.0</td>
      <td>3653.0</td>
      <td>110.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170.0</td>
      <td>25.0</td>
      <td>29.0</td>
      <td>2822.0</td>
      <td>101.0</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>431</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208.0</td>
      <td>23.0</td>
      <td>27.0</td>
      <td>3823.0</td>
      <td>109.0</td>
      <td>186.0</td>
    </tr>
  </tbody>
</table>
<p>432 rows × 15 columns</p>
</div>




```python

```
