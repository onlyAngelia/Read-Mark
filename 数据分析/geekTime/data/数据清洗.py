Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> import pandas as pd
>>> from pandas import Series,DataFrame
>>> df = DataFrame(pd.read_excel('/Users/apple/Desktop/GitHubProject/Read mark/数据分析/data/accountMessage.xlsx'))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df = DataFrame(pd.read_excel('/Users/apple/Desktop/GitHubProject/Read mark/数据分析/data/accountMessage.xlsx'))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/util/_decorators.py", line 188, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/util/_decorators.py", line 188, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/io/excel.py", line 350, in read_excel
    io = ExcelFile(io, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/io/excel.py", line 653, in __init__
    self._reader = self._engines[engine](self._io)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/io/excel.py", line 424, in __init__
    self.book = xlrd.open_workbook(filepath_or_buffer)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/xlrd/__init__.py", line 111, in open_workbook
    with open(filename, "rb") as f:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/apple/Desktop/GitHubProject/Read mark/数据分析/data/accountMessage.xlsx'
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
>>> df.drop(columns=[0,'\t'])
                 1     2           3    4    5    6    7    8    9
0     Mickey Mouse  56.0       70kgs   72   69   71    -    -    -
1     Donald Dunck  34.0   154.89lbs    -    -    -   85   84   76
2       Mini Mouse  16.0         NaN    -    -    -   65   69   72
3   Scrooge McDuck   NaN       78kgs   78   79   72    -    -    -
4     Pink Panther  54.0  198.658lbs    -    -    -   69  NaN   75
5     Huey  McDuck  52.0      189lbs    -    -    -   68   75   72
6     Dewey McDuck  19.0       56kgs    -    -    -   71   78   75
7       Scoopy Doo  32.0       78kgs   78   76   75    -    -    -
8              NaN   NaN         NaN  NaN  NaN  NaN  NaN  NaN  NaN
9     Huey  McDuck  52.0      189lbs    -    -    -   68   75   72
10    Louie McDuck  12.0       45kgs    -    -    -   92   95   87
>>> df.drop(columns=[0,'\t'],inplace=True)
>>> df.rename(columns={1:'name',2:'age';3:'weights',4:'m0006',5:'m0612',6:'m1218',7:'f0006',8:'f0612',9:'f1218'},inplace=True)
SyntaxError: invalid syntax
>>> df.rename(columns={1:'name',2:'age',3:'weights',4:'m0006',5:'m0612',6:'m1218',7:'f0006',8:'f0612',9:'f1218'},inplace=True)
>>> df['age'].fillna(df['age'].mean(),inplace=True)
>>> df['weight'].fillna(df['weight'].value_counts().index[0])
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'weight'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df['weight'].fillna(df['weight'].value_counts().index[0])
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'weight'
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
>>> for i, row in df[lbs_row].iterrows():
	weight = int(float(lbs_row['weight'][:-3])/2.2)
	df.at[i,'weights'] = '{}kgs'.format(weight)

	
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    weight = int(float(lbs_row['weight'][:-3])/2.2)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/series.py", line 868, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 4375, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas/_libs/index.pyx", line 81, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 89, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 129, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 91, in pandas._libs.index.Int64Engine._check_type
KeyError: 'weight'
>>> for i,row in df[lbs_row].iterrows();
SyntaxError: invalid syntax
>>> for i,row in df[lbs_row].iterrows():
	weight = int(float(lbs_row['weight'][:-3])/2.2)
	df.at[i,'weight']='{}kgs'.format(weight)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    weight = int(float(lbs_row['weight'][:-3])/2.2)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/series.py", line 868, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 4375, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas/_libs/index.pyx", line 81, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 89, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 129, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 91, in pandas._libs.index.Int64Engine._check_type
KeyError: 'weight'
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
>>> df['age'].astype(int)
0     56
1     34
2     16
3     36
4     54
5     52
6     19
7     32
9     52
10    12
Name: age, dtype: int64
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
>>> df['age'].astype(int,inplace=True)
0     56
1     34
2     16
3     36
4     54
5     52
6     19
7     32
9     52
10    12
Name: age, dtype: int64
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
>>> df2 = df['age'].astype(int)
>>> print (df2)
0     56
1     34
2     16
3     36
4     54
5     52
6     19
7     32
9     52
10    12
Name: age, dtype: int64
>>> df['age'] = df['age'].astype(int)
>>> print (df)
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

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    df['f0612'].fillna(df['f0612'].mean())
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/generic.py", line 10956, in stat_func
    numeric_only=numeric_only)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/series.py", line 3630, in _reduce
    return op(delegate, skipna=skipna, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/nanops.py", line 76, in _f
    return f(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/nanops.py", line 130, in f
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
>>> columns.inser(0,columns.pop(columns.index('first_name')))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    columns.inser(0,columns.pop(columns.index('first_name')))
AttributeError: 'list' object has no attribute 'inser'
>>> columns.insert(0,columns.pop(columns.index('first_name')))
>>> df = df.ix[:,cols]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    df = df.ix[:,cols]
NameError: name 'cols' is not defined
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
>>> df[len(str(df['f0612'])) > 0]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: True

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    df[len(str(df['f0612'])) > 0]
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: True
>>> df[len(str(df['f0612'])) > 0]['f0612']
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: True

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    df[len(str(df['f0612'])) > 0]['f0612']
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: True
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
>>> df.set_index(drop=True)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    df.set_index(drop=True)
TypeError: set_index() missing 1 required positional argument: 'keys'
>>> print (pd.index())
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print (pd.index())
AttributeError: module 'pandas' has no attribute 'index'
>>> print (pd.Index())
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print (pd.Index())
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 468, in __new__
    cls._scalar_data_error(data)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 3799, in _scalar_data_error
    repr(data)))
TypeError: Index(...) must be called with a collection of some kind, None was passed
>>> pd.reindex()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    pd.reindex()
AttributeError: module 'pandas' has no attribute 'reindex'
>>> df.reindex()
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
>>> df.reindex=(index={'0','1','2'},columns=states).bfill()
SyntaxError: invalid syntax
>>> df.reindex=(index=['0','1','2'],columns=states).bfill()
SyntaxError: invalid syntax
>>> index = ['0','1','2']
>>> df.reindex(index.columns=states).bfill()
SyntaxError: keyword can't be an expression
>>> df.reindex(['0','1','2'],bfill)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    df.reindex(['0','1','2'],bfill)
NameError: name 'bfill' is not defined
>>> df.reindex([0,1,2,3],bfill())
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    df.reindex([0,1,2,3],bfill())
NameError: name 'bfill' is not defined
>>> df.reindex([0,1,2,3],method = bfill())
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    df.reindex([0,1,2,3],method = bfill())
NameError: name 'bfill' is not defined
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
>>> 
