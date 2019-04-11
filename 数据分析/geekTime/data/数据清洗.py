Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> import pandas as pd
>>> from pandas import Series,DataFrame
>>> df = DataFrame(pd.read_excel('/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/accountMessage.xlsx'))
>>> print (df)
    \t     0               1     2           3    4    5    6    7    8    9
0    0   1.0    Mickey Mouse  56.0       70kgs   72   69   71    -    -    -
1    1   2.0    Donald Dunck  34.0   154.89lbs    -    -    -   85   84   76
2    2   3.0      Mini Mouse  16.0         NaN    -    -    -   65   69   72
3    3   4.0  Scrooge McDuck   NaN       78kgs   78   79   72    -    -    -
4    4   5.0    Pink Panther  54.0  198.658lbs    -    -    -   69  NaN   75
5    5   6.0    Huey  McDuck  52.0      189lbs    -    -    -   68   75   72
6    6   7.0    Dewey McDuck  19.0       56kgs    -    -    -   71   78   75
7    7   8.0      Scoopy Doo  32.0       78kgs   78   76   75    -    -    -
8    8   NaN             NaN   NaN         NaN  NaN  NaN  NaN  NaN  NaN  NaN
9    9   9.0    Huey  McDuck  52.0      189lbs    -    -    -   68   75   72
10  10  10.0    Louie McDuck  12.0       45kgs    -    -    -   92   95   87
>>> df.drop(columns=[0,'\t'],inplace=True)
>>> df.rename(columns={1:'name',2:'age',3:'weights',4:'m0006',5:'m0612',6:'m1218',7:'f0006',8:'f0612',9:'f1218'},inplace=True)
>>> df['age'].fillna(df['age'].mean(),inplace=True)
>>> df['weights'].fillna(df['weights'].value_counts().index[0],inplace=True)
>>> df.dropna(how='all',inplace=True)
>>> lbs_row = df['weights'].str.contains('lbs').fillna(False)
>>> print (df[lbs_row])
           name        age     weights m0006 m0612 m1218 f0006 f0612 f1218
1  Donald Dunck  34.000000   154.89lbs     -     -     -    85    84    76
2    Mini Mouse  16.000000      189lbs     -     -     -    65    69    72
4  Pink Panther  54.000000  198.658lbs     -     -     -    69   NaN    75
5  Huey  McDuck  52.000000      189lbs     -     -     -    68    75    72
8           NaN  36.333333      189lbs   NaN   NaN   NaN   NaN   NaN   NaN
9  Huey  McDuck  52.000000      189lbs     -     -     -    68    75    72
>>> df.drop(index=[8],inplace=True)
>>> print (df)
              name        age     weights m0006 m0612 m1218 f0006 f0612 f1218
0     Mickey Mouse  56.000000       70kgs    72    69    71     -     -     -
1     Donald Dunck  34.000000   154.89lbs     -     -     -    85    84    76
2       Mini Mouse  16.000000      189lbs     -     -     -    65    69    72
3   Scrooge McDuck  36.333333       78kgs    78    79    72     -     -     -
4     Pink Panther  54.000000  198.658lbs     -     -     -    69   NaN    75
5     Huey  McDuck  52.000000      189lbs     -     -     -    68    75    72
6     Dewey McDuck  19.000000       56kgs     -     -     -    71    78    75
7       Scoopy Doo  32.000000       78kgs    78    76    75     -     -     -
9     Huey  McDuck  52.000000      189lbs     -     -     -    68    75    72
10    Louie McDuck  12.000000       45kgs     -     -     -    92    95    87
>>> print (df[lbs_row])

Warning (from warnings module):
  File "__main__", line 1
UserWarning: Boolean Series key will be reindexed to match DataFrame index.
           name   age     weights m0006 m0612 m1218 f0006 f0612 f1218
1  Donald Dunck  34.0   154.89lbs     -     -     -    85    84    76
2    Mini Mouse  16.0      189lbs     -     -     -    65    69    72
4  Pink Panther  54.0  198.658lbs     -     -     -    69   NaN    75
5  Huey  McDuck  52.0      189lbs     -     -     -    68    75    72
9  Huey  McDuck  52.0      189lbs     -     -     -    68    75    72

>>> for i,row in df[lbs_row].iterrrows():
	weight = int(float(lbs_row['weights'][:-3])/2.2)
	df.at[i,'weights']='{}kgs'.format(weight)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for i,row in df[lbs_row].iterrrows():
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'iterrrows'
>>> for i,row in df[lbs_row].iterrows():
	weight = int(float(lbs_row['weights'][:-3])/2.2)
	df.at[i,'weights']='{}kgs'.format(weight)

	
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    weight = int(float(lbs_row['weights'][:-3])/2.2)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/series.py", line 868, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 4375, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas/_libs/index.pyx", line 81, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 89, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 129, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 91, in pandas._libs.index.Int64Engine._check_type
KeyError: 'weights'
>>> print (lib_row)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print (lib_row)
NameError: name 'lib_row' is not defined
>>> print (libs_row)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print (libs_row)
NameError: name 'libs_row' is not defined
>>> print (df[lbs_row])
           name   age     weights m0006 m0612 m1218 f0006 f0612 f1218
1  Donald Dunck  34.0   154.89lbs     -     -     -    85    84    76
2    Mini Mouse  16.0      189lbs     -     -     -    65    69    72
4  Pink Panther  54.0  198.658lbs     -     -     -    69   NaN    75
5  Huey  McDuck  52.0      189lbs     -     -     -    68    75    72
9  Huey  McDuck  52.0      189lbs     -     -     -    68    75    72
>>> print (lbs_row)
0     False
1      True
2      True
3     False
4      True
5      True
6     False
7     False
8      True
9      True
10    False
Name: weights, dtype: bool
>>> for i, row in df[lbs_row].iterrows():
	weight = int(float(row['weights'][:-3])/2.2)
	df.at[i,'weights'] = '{}kgs'.format(weight)

>>> print (df)
              name        age weights m0006 m0612 m1218 f0006 f0612 f1218
0     Mickey Mouse  56.000000   70kgs    72    69    71     -     -     -
1     Donald Dunck  34.000000   70kgs     -     -     -    85    84    76
2       Mini Mouse  16.000000   85kgs     -     -     -    65    69    72
3   Scrooge McDuck  36.333333   78kgs    78    79    72     -     -     -
4     Pink Panther  54.000000   90kgs     -     -     -    69   NaN    75
5     Huey  McDuck  52.000000   85kgs     -     -     -    68    75    72
6     Dewey McDuck  19.000000   56kgs     -     -     -    71    78    75
7       Scoopy Doo  32.000000   78kgs    78    76    75     -     -     -
9     Huey  McDuck  52.000000   85kgs     -     -     -    68    75    72
10    Louie McDuck  12.000000   45kgs     -     -     -    92    95    87

>>> df.replace({r'[^\x00-\x7F]+':''},regex=True)
              name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0     Mickey Mouse   56   70kgs    72    69    71     -     -     -
1     Donald Dunck   34   70kgs     -     -     -    85    84    76
2       Mini Mouse   16   85kgs     -     -     -    65    69    72
3   Scrooge McDuck   36   78kgs    78    79    72     -     -     -
4     Pink Panther   54   90kgs     -     -     -    69   NaN    75
5     Huey  McDuck   52   85kgs     -     -     -    68    75    72
6     Dewey McDuck   19   56kgs     -     -     -    71    78    75
7       Scoopy Doo   32   78kgs    78    76    75     -     -     -
9     Huey  McDuck   52   85kgs     -     -     -    68    75    72
10    Louie McDuck   12   45kgs     -     -     -    92    95    87
>>> df['f0612'].fillna(df['f0612'].mean())
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/nanops.py", line 127, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/nanops.py", line 479, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/numpy/core/_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int
>>> df[['first_name','last_name']] = df['name'].str.split(expand=True)
>>> df.drop('name',axis=1,inplace=True)
>>> df.drop_duplicates()
    age weights m0006 m0612 m1218 f0006 f0612 f1218 first_name last_name
0    56   70kgs    72    69    71     -     -     -     Mickey     Mouse
1    34   70kgs     -     -     -    85    84    76     Donald     Dunck
2    16   85kgs     -     -     -    65    69    72       Mini     Mouse
3    36   78kgs    78    79    72     -     -     -    Scrooge    McDuck
4    54   90kgs     -     -     -    69   NaN    75       Pink   Panther
5    52   85kgs     -     -     -    68    75    72       Huey    McDuck
6    19   56kgs     -     -     -    71    78    75      Dewey    McDuck
7    32   78kgs    78    76    75     -     -     -     Scoopy       Doo
10   12   45kgs     -     -     -    92    95    87      Louie    McDuck
>>> df.drop_duplicates(inplace=True)
>>> columns = list(df)
>>> columns.insert(0,columns.pop(columns.index('last_name')))
>>> columns
['last_name', 'age', 'weights', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218', 'first_name']
>>> columns.insert(0,columns.pop(columns.index('first_name')))
>>> df = df.ix[:,columns]
>>> print (df)
   first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0      Mickey     Mouse   56   70kgs    72    69    71     -     -     -
1      Donald     Dunck   34   70kgs     -     -     -    85    84    76
2        Mini     Mouse   16   85kgs     -     -     -    65    69    72
3     Scrooge    McDuck   36   78kgs    78    79    72     -     -     -
4        Pink   Panther   54   90kgs     -     -     -    69   NaN    75
5        Huey    McDuck   52   85kgs     -     -     -    68    75    72
6       Dewey    McDuck   19   56kgs     -     -     -    71    78    75
7      Scoopy       Doo   32   78kgs    78    76    75     -     -     -
10      Louie    McDuck   12   45kgs     -     -     -    92    95    87
>>> f0612_rows = df['f0612'].str.isalnum().fillna(False)
>>> print (f0612_rows)
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
10    False
Name: f0612, dtype: bool
>>> f0612_rows = df['f0612'].str.isalnum().fillna(True)
>>> print (f0612_rows)
0     False
1      True
2      True
3     False
4      True
5      True
6      True
7     False
10     True
Name: f0612, dtype: bool
>>> print (df[f0612_rows])
   first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
1      Donald     Dunck   34   70kgs     -     -     -    85    84    76
2        Mini     Mouse   16   85kgs     -     -     -    65    69    72
4        Pink   Panther   54   90kgs     -     -     -    69   NaN    75
5        Huey    McDuck   52   85kgs     -     -     -    68    75    72
6       Dewey    McDuck   19   56kgs     -     -     -    71    78    75
10      Louie    McDuck   12   45kgs     -     -     -    92    95    87
>>> f0612_mean = df[f0612_rows]['f0612'].mean()
>>> print (f0612_mean)
80.2
>>> df['f0612'].fillna(f0612_mean,inplace=True)
>>> print (df)
   first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0      Mickey     Mouse   56   70kgs    72    69    71     -     -     -
1      Donald     Dunck   34   70kgs     -     -     -    85    84    76
2        Mini     Mouse   16   85kgs     -     -     -    65    69    72
3     Scrooge    McDuck   36   78kgs    78    79    72     -     -     -
4        Pink   Panther   54   90kgs     -     -     -    69  80.2    75
5        Huey    McDuck   52   85kgs     -     -     -    68    75    72
6       Dewey    McDuck   19   56kgs     -     -     -    71    78    75
7      Scoopy       Doo   32   78kgs    78    76    75     -     -     -
10      Louie    McDuck   12   45kgs     -     -     -    92    95    87
>>> df.replace('-','',inplace = True)
>>> print (df)
   first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0      Mickey     Mouse   56   70kgs    72    69    71                  
1      Donald     Dunck   34   70kgs                      85    84    76
2        Mini     Mouse   16   85kgs                      65    69    72
3     Scrooge    McDuck   36   78kgs    78    79    72                  
4        Pink   Panther   54   90kgs                      69  80.2    75
5        Huey    McDuck   52   85kgs                      68    75    72
6       Dewey    McDuck   19   56kgs                      71    78    75
7      Scoopy       Doo   32   78kgs    78    76    75                  
10      Louie    McDuck   12   45kgs                      92    95    87
>>> df.reindex([0,1,2,4],method = 'bfill')
  first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0     Mickey     Mouse   56   70kgs    72    69    71                  
1     Donald     Dunck   34   70kgs                      85    84    76
2       Mini     Mouse   16   85kgs                      65    69    72
4       Pink   Panther   54   90kgs                      69  80.2    75
>>> print (df)
   first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0      Mickey     Mouse   56   70kgs    72    69    71                  
1      Donald     Dunck   34   70kgs                      85    84    76
2        Mini     Mouse   16   85kgs                      65    69    72
3     Scrooge    McDuck   36   78kgs    78    79    72                  
4        Pink   Panther   54   90kgs                      69  80.2    75
5        Huey    McDuck   52   85kgs                      68    75    72
6       Dewey    McDuck   19   56kgs                      71    78    75
7      Scoopy       Doo   32   78kgs    78    76    75                  
10      Louie    McDuck   12   45kgs                      92    95    87
>>> df.reindex(range(df.shape[0]),method = 'bfill')
  first_name last_name  age weights m0006 m0612 m1218 f0006 f0612 f1218
0     Mickey     Mouse   56   70kgs    72    69    71                  
1     Donald     Dunck   34   70kgs                      85    84    76
2       Mini     Mouse   16   85kgs                      65    69    72
3    Scrooge    McDuck   36   78kgs    78    79    72                  
4       Pink   Panther   54   90kgs                      69  80.2    75
5       Huey    McDuck   52   85kgs                      68    75    72
6      Dewey    McDuck   19   56kgs                      71    78    75
7     Scoopy       Doo   32   78kgs    78    76    75                  
8      Louie    McDuck   12   45kgs                      92    95    87
>>> df.to_excel('/Users/apple/Desktop/GitHubProject/Read mark/数据分析/geekTime/data/accountMessage_new.xlsx')
