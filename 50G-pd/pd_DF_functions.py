#Topic: Pandas Data Frame
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars


#%%%
DataFrame([data, index, columns, dtype, copy])	Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
#%%Attributes and underlying data
#Axes

#DataFrame.index	The index (row labels) of the DataFrame.
df.index

#DataFrame.columns	The column labels of the DataFrame.
df.columns

#DataFrame.dtypes	Return the dtypes in the DataFrame.
df.dtypes

#DataFrame.ftypes	(DEPRECATED) Return the ftypes (indication of sparse/                 dense and dtype) in DataFrame.
df.ftypes

#DataFrame.get_dtype_counts(self)	(DEPRECATED) Return counts of unique dtypes in this object.
df.get_dtype_counts()

#DataFrame.get_ftype_counts(self)	(DEPRECATED) Return counts of unique ftypes in this object.
df.get_ftypes_counts()

#DataFrame.select_dtypes(self[, include, exclude])	Return a subset of the DataFrame’s columns based on the column dtypes.
df.dtypes
df.select_dtypes(include=['float64'])
df.select_dtypes(exclude=['int'])

#DataFrame.values	Return a Numpy representation of the DataFrame.
df.values

#DataFrame.get_values(self)	(DEPRECATED) Return an ndarray after converting sparse values to dense.
df.get_values()

#DataFrame.axes	Return a list representing the axes of the DataFrame.
df.axes

#DataFrame.ndim	Return an int representing the number of axes / array dimensions.
df.ndim

#DataFrame.size	Return an int representing the number of elements in this object.
df.size

#DataFrame.shape	Return a tuple representing the dimensionality of the DataFrame.
df.shape

#DataFrame.memory_usage(self[, index, deep])	Return the memory usage of each column in bytes.
df.memory_usage()

#DataFrame.empty	Indicator whether DataFrame is empty.
df.empty

#DataFrame.is_copy	Return the copy.
df.is_copy

#%%
#Conversion
#DataFrame.astype(self, dtype[, copy, errors])	Cast a pandas object to a specified dtype dtype.
df.astype('int')

#DataFrame.infer_objects(self)	Attempt to infer better dtypes for object columns.
df
df.infer_objects
#good

#DataFrame.copy(self[, deep])	Make a copy of this object’s indices and data.
df1=df.copy()
id(df), id(df1)

#DataFrame.isna(self)	Detect missing values.
df.isna()

#DataFrame.notna(self)	Detect existing (non-missing) values.
df.notna()

#DataFrame.bool(self)	Return the bool of a single element PandasObject.
(df > 5).bool

#%%#Indexing, iteration

#DataFrame.head(self[, n])	Return the first n rows.
df.head()

#DataFrame.at	Access a single value for a row/column label pair.
df.index
df.at['Mazda RX4', 'mpg']

#DataFrame.iat	Access a single value for a row/column pair by integer position.
df.iat[0,0]

#DataFrame.loc	Access a group of rows and columns by label(s) or a boolean array.
df.loc['Mazda RX4', ['mpg','wt']

#DataFrame.iloc	Purely integer-location based indexing for selection by position.
df.iloc[1:10:2, 1:5:2]

#DataFrame.insert(self, loc, column, value[, …])	Insert column into DataFrame at specified location.
df.columns
df2= df.copy()
df2.insert(2, 'carname',df.index)
df2.head()
df.head()

#DataFrame.__iter__(self)	Iterate over info axis.
df._iter_(axis=0)
#not working

#DataFrame.items(self)	Iterator over (column name, Series) pairs.
df.items
df.items(['mpg'])
for label, content in df.items():
    print('label:', label)
    print('content:', content, sep='\n')

#DataFrame.iteritems(self)	Iterator over (column name, Series) pairs.


#DataFrame.keys(self)	Get the ‘info axis’ (see Indexing for more)


#DataFrame.iterrows(self)	Iterate over DataFrame rows as (index, Series) pairs.

#DataFrame.itertuples(self[, index, name])	Iterate over DataFrame rows as namedtuples.


#DataFrame.lookup(self, row_labels, col_labels)	Label-based “fancy indexing” function for DataFrame.

#DataFrame.pop(self, item)	Return item and drop from frame.


#DataFrame.tail(self[, n])	Return the last n rows.


#DataFrame.xs(self, key[, axis, level, …])	Return cross-section from the Series/DataFrame.


#DataFrame.get(self, key[, default])	Get item from object for given key (ex: DataFrame column).

#DataFrame.isin(self, values)	Whether each element in the DataFrame is contained in values.

#DataFrame.where(self, cond[, other, …])	Replace values where the condition is False.

#DataFrame.mask(self, cond[, other, inplace, …])	Replace values where the condition is True.
#DataFrame.query(self, expr[, inplace])	Query the columns of a DataFrame with a boolean expression.

#For more information on .at, .iat, .loc, and .iloc, see the indexing documentation.

#%%%Binary operator functions
#DataFrame.add(self, other[, axis, level, …])	Get Addition of dataframe and other, element-wise (binary operator add).


#DataFrame.sub(self, other[, axis, level, …])	Get Subtraction of dataframe and other, element-wise (binary operator sub).


#DataFrame.mul(self, other[, axis, level, …])	Get Multiplication of dataframe and other, element-wise (binary operator mul).

#DataFrame.div(self, other[, axis, level, …])	Get Floating division of dataframe and other, element-wise (binary operator truediv).

#DataFrame.truediv(self, other[, axis, …])	Get Floating division of dataframe and other, element-wise (binary operator truediv).
DataFrame.floordiv(self, other[, axis, …])	Get Integer division of dataframe and other, element-wise (binary operator floordiv).
DataFrame.mod(self, other[, axis, level, …])	Get Modulo of dataframe and other, element-wise (binary operator mod).
DataFrame.pow(self, other[, axis, level, …])	Get Exponential power of dataframe and other, element-wise (binary operator pow).
DataFrame.dot(self, other)	Compute the matrix multiplication between the DataFrame and other.
DataFrame.radd(self, other[, axis, level, …])	Get Addition of dataframe and other, element-wise (binary operator radd).
DataFrame.rsub(self, other[, axis, level, …])	Get Subtraction of dataframe and other, element-wise (binary operator rsub).
DataFrame.rmul(self, other[, axis, level, …])	Get Multiplication of dataframe and other, element-wise (binary operator rmul).
DataFrame.rdiv(self, other[, axis, level, …])	Get Floating division of dataframe and other, element-wise (binary operator rtruediv).
DataFrame.rtruediv(self, other[, axis, …])	Get Floating division of dataframe and other, element-wise (binary operator rtruediv).
DataFrame.rfloordiv(self, other[, axis, …])	Get Integer division of dataframe and other, element-wise (binary operator rfloordiv).
DataFrame.rmod(self, other[, axis, level, …])	Get Modulo of dataframe and other, element-wise (binary operator rmod).
DataFrame.rpow(self, other[, axis, level, …])	Get Exponential power of dataframe and other, element-wise (binary operator rpow).
DataFrame.lt(self, other[, axis, level])	Get Less than of dataframe and other, element-wise (binary operator lt).
DataFrame.gt(self, other[, axis, level])	Get Greater than of dataframe and other, element-wise (binary operator gt).
DataFrame.le(self, other[, axis, level])	Get Less than or equal to of dataframe and other, element-wise (binary operator le).
DataFrame.ge(self, other[, axis, level])	Get Greater than or equal to of dataframe and other, element-wise (binary operator ge).
DataFrame.ne(self, other[, axis, level])	Get Not equal to of dataframe and other, element-wise (binary operator ne).
DataFrame.eq(self, other[, axis, level])	Get Equal to of dataframe and other, element-wise (binary operator eq).
DataFrame.combine(self, other, func[, …])	Perform column-wise combine with another DataFrame.
DataFrame.combine_first(self, other)	Update null elements with value in the same location in other.
Function application, GroupBy & window
DataFrame.apply(self, func[, axis, …])	Apply a function along an axis of the DataFrame.
DataFrame.applymap(self, func)	Apply a function to a Dataframe elementwise.
DataFrame.pipe(self, func, \*args, \*\*kwargs)	Apply func(self, *args, **kwargs).
DataFrame.agg(self, func[, axis])	Aggregate using one or more operations over the specified axis.
DataFrame.aggregate(self, func[, axis])	Aggregate using one or more operations over the specified axis.
DataFrame.transform(self, func[, axis])	Call func on self producing a DataFrame with transformed values and that has the same axis length as self.
DataFrame.groupby(self[, by, axis, level, …])	Group DataFrame or Series using a mapper or by a Series of columns.
DataFrame.rolling(self, window[, …])	Provide rolling window calculations.
DataFrame.expanding(self[, min_periods, …])	Provide expanding transformations.
DataFrame.ewm(self[, com, span, halflife, …])	Provide exponential weighted functions.
Computations / descriptive stats
DataFrame.abs(self)	Return a Series/DataFrame with absolute numeric value of each element.
DataFrame.all(self[, axis, bool_only, …])	Return whether all elements are True, potentially over an axis.
DataFrame.any(self[, axis, bool_only, …])	Return whether any element is True, potentially over an axis.
DataFrame.clip(self[, lower, upper, axis, …])	Trim values at input threshold(s).
DataFrame.clip_lower(self, threshold[, …])	(DEPRECATED) Trim values below a given threshold.
DataFrame.clip_upper(self, threshold[, …])	(DEPRECATED) Trim values above a given threshold.
DataFrame.compound(self[, axis, skipna, level])	(DEPRECATED) Return the compound percentage of the values for the requested axis.
DataFrame.corr(self[, method, min_periods])	Compute pairwise correlation of columns, excluding NA/null values.
DataFrame.corrwith(self, other[, axis, …])	Compute pairwise correlation between rows or columns of DataFrame with rows or columns of Series or DataFrame.
DataFrame.count(self[, axis, level, …])	Count non-NA cells for each column or row.
DataFrame.cov(self[, min_periods])	Compute pairwise covariance of columns, excluding NA/null values.
DataFrame.cummax(self[, axis, skipna])	Return cumulative maximum over a DataFrame or Series axis.
DataFrame.cummin(self[, axis, skipna])	Return cumulative minimum over a DataFrame or Series axis.
DataFrame.cumprod(self[, axis, skipna])	Return cumulative product over a DataFrame or Series axis.
DataFrame.cumsum(self[, axis, skipna])	Return cumulative sum over a DataFrame or Series axis.
DataFrame.describe(self[, percentiles, …])	Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
DataFrame.diff(self[, periods, axis])	First discrete difference of element.
DataFrame.eval(self, expr[, inplace])	Evaluate a string describing operations on DataFrame columns.
DataFrame.kurt(self[, axis, skipna, level, …])	Return unbiased kurtosis over requested axis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
DataFrame.kurtosis(self[, axis, skipna, …])	Return unbiased kurtosis over requested axis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
DataFrame.mad(self[, axis, skipna, level])	Return the mean absolute deviation of the values for the requested axis.
DataFrame.max(self[, axis, skipna, level, …])	Return the maximum of the values for the requested axis.
DataFrame.mean(self[, axis, skipna, level, …])	Return the mean of the values for the requested axis.
DataFrame.median(self[, axis, skipna, …])	Return the median of the values for the requested axis.
DataFrame.min(self[, axis, skipna, level, …])	Return the minimum of the values for the requested axis.
DataFrame.mode(self[, axis, numeric_only, …])	Get the mode(s) of each element along the selected axis.
DataFrame.pct_change(self[, periods, …])	Percentage change between the current and a prior element.
DataFrame.prod(self[, axis, skipna, level, …])	Return the product of the values for the requested axis.
DataFrame.product(self[, axis, skipna, …])	Return the product of the values for the requested axis.
DataFrame.quantile(self[, q, axis, …])	Return values at the given quantile over requested axis.
DataFrame.rank(self[, axis, method, …])	Compute numerical data ranks (1 through n) along axis.
DataFrame.round(self[, decimals])	Round a DataFrame to a variable number of decimal places.
DataFrame.sem(self[, axis, skipna, level, …])	Return unbiased standard error of the mean over requested axis.
DataFrame.skew(self[, axis, skipna, level, …])	Return unbiased skew over requested axis Normalized by N-1.
DataFrame.sum(self[, axis, skipna, level, …])	Return the sum of the values for the requested axis.
DataFrame.std(self[, axis, skipna, level, …])	Return sample standard deviation over requested axis.
DataFrame.var(self[, axis, skipna, level, …])	Return unbiased variance over requested axis.
DataFrame.nunique(self[, axis, dropna])	Count distinct observations over requested axis.
Reindexing / selection / label manipulation
DataFrame.add_prefix(self, prefix)	Prefix labels with string prefix.
DataFrame.add_suffix(self, suffix)	Suffix labels with string suffix.
DataFrame.align(self, other[, join, axis, …])	Align two objects on their axes with the specified join method for each axis Index.
DataFrame.at_time(self, time[, asof, axis])	Select values at particular time of day (e.g.
DataFrame.between_time(self, start_time, …)	Select values between particular times of the day (e.g., 9:00-9:30 AM).
DataFrame.drop(self[, labels, axis, index, …])	Drop specified labels from rows or columns.
DataFrame.drop_duplicates(self[, subset, …])	Return DataFrame with duplicate rows removed, optionally only considering certain columns.
DataFrame.duplicated(self[, subset, keep])	Return boolean Series denoting duplicate rows, optionally only considering certain columns.
DataFrame.equals(self, other)	Test whether two objects contain the same elements.
DataFrame.filter(self[, items, like, regex, …])	Subset rows or columns of dataframe according to labels in the specified index.
DataFrame.first(self, offset)	Convenience method for subsetting initial periods of time series data based on a date offset.
DataFrame.head(self[, n])	Return the first n rows.
DataFrame.idxmax(self[, axis, skipna])	Return index of first occurrence of maximum over requested axis.
DataFrame.idxmin(self[, axis, skipna])	Return index of first occurrence of minimum over requested axis.
DataFrame.last(self, offset)	Convenience method for subsetting final periods of time series data based on a date offset.
DataFrame.reindex(self[, labels, index, …])	Conform DataFrame to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.
DataFrame.reindex_like(self, other[, …])	Return an object with matching indices as other object.
DataFrame.rename(self[, mapper, index, …])	Alter axes labels.
DataFrame.rename_axis(self[, mapper, index, …])	Set the name of the axis for the index or columns.
DataFrame.reset_index(self[, level, drop, …])	Reset the index, or a level of it.
DataFrame.sample(self[, n, frac, replace, …])	Return a random sample of items from an axis of object.
DataFrame.set_axis(self, labels[, axis, inplace])	Assign desired index to given axis.
DataFrame.set_index(self, keys[, drop, …])	Set the DataFrame index using existing columns.
DataFrame.tail(self[, n])	Return the last n rows.
DataFrame.take(self, indices[, axis, is_copy])	Return the elements in the given positional indices along an axis.
DataFrame.truncate(self[, before, after, …])	Truncate a Series or DataFrame before and after some index value.
Missing data handling
DataFrame.dropna(self[, axis, how, thresh, …])	Remove missing values.
DataFrame.fillna(self[, value, method, …])	Fill NA/NaN values using the specified method.
DataFrame.replace(self[, to_replace, value, …])	Replace values given in to_replace with value.
DataFrame.interpolate(self[, method, axis, …])	Interpolate values according to different methods.
Reshaping, sorting, transposing
DataFrame.droplevel(self, level[, axis])	Return DataFrame with requested index / column level(s) removed.
DataFrame.pivot(self[, index, columns, values])	Return reshaped DataFrame organized by given index / column values.
DataFrame.pivot_table(self[, values, index, …])	Create a spreadsheet-style pivot table as a DataFrame.
DataFrame.reorder_levels(self, order[, axis])	Rearrange index levels using input order.
DataFrame.sort_values(self, by[, axis, …])	Sort by the values along either axis.
DataFrame.sort_index(self[, axis, level, …])	Sort object by labels (along an axis).
DataFrame.nlargest(self, n, columns[, keep])	Return the first n rows ordered by columns in descending order.
DataFrame.nsmallest(self, n, columns[, keep])	Return the first n rows ordered by columns in ascending order.
DataFrame.swaplevel(self[, i, j, axis])	Swap levels i and j in a MultiIndex on a particular axis.
DataFrame.stack(self[, level, dropna])	Stack the prescribed level(s) from columns to index.
DataFrame.unstack(self[, level, fill_value])	Pivot a level of the (necessarily hierarchical) index labels, returning a DataFrame having a new level of column labels whose inner-most level consists of the pivoted index labels.
DataFrame.swapaxes(self, axis1, axis2[, copy])	Interchange axes and swap values axes appropriately.
DataFrame.melt(self[, id_vars, value_vars, …])	Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.
DataFrame.explode(self, column, Tuple])	Transform each element of a list-like to a row, replicating the index values.
DataFrame.squeeze(self[, axis])	Squeeze 1 dimensional axis objects into scalars.
DataFrame.to_xarray(self)	Return an xarray object from the pandas object.
DataFrame.T	Transpose index and columns.
DataFrame.transpose(self, \*args, \*\*kwargs)	Transpose index and columns.
Combining / joining / merging
DataFrame.append(self, other[, …])	Append rows of other to the end of caller, returning a new object.
DataFrame.assign(self, \*\*kwargs)	Assign new columns to a DataFrame.
DataFrame.join(self, other[, on, how, …])	Join columns of another DataFrame.
DataFrame.merge(self, right[, how, on, …])	Merge DataFrame or named Series objects with a database-style join.
DataFrame.update(self, other[, join, …])	Modify in place using non-NA values from another DataFrame.
Time series-related
DataFrame.asfreq(self, freq[, method, how, …])	Convert TimeSeries to specified frequency.
DataFrame.asof(self, where[, subset])	Return the last row(s) without any NaNs before where.
DataFrame.shift(self[, periods, freq, axis, …])	Shift index by desired number of periods with an optional time freq.
DataFrame.slice_shift(self[, periods, axis])	Equivalent to shift without copying data.
DataFrame.tshift(self[, periods, freq, axis])	Shift the time index, using the index’s frequency if available.
DataFrame.first_valid_index(self)	Return index for first non-NA/null value.
DataFrame.last_valid_index(self)	Return index for last non-NA/null value.
DataFrame.resample(self, rule[, how, axis, …])	Resample time-series data.
DataFrame.to_period(self[, freq, axis, copy])	Convert DataFrame from DatetimeIndex to PeriodIndex with desired frequency (inferred from index if not passed).
DataFrame.to_timestamp(self[, freq, how, …])	Cast to DatetimeIndex of timestamps, at beginning of period.
DataFrame.tz_convert(self, tz[, axis, …])	Convert tz-aware axis to target time zone.
DataFrame.tz_localize(self, tz[, axis, …])	Localize tz-naive index of a Series or DataFrame to target time zone.
Plotting
DataFrame.plot is both a callable method and a namespace attribute for specific plotting methods of the form DataFrame.plot.<kind>.

DataFrame.plot([x, y, kind, ax, ….])	DataFrame plotting accessor and method
DataFrame.plot.area(self[, x, y])	Draw a stacked area plot.
DataFrame.plot.bar(self[, x, y])	Vertical bar plot.
DataFrame.plot.barh(self[, x, y])	Make a horizontal bar plot.
DataFrame.plot.box(self[, by])	Make a box plot of the DataFrame columns.
DataFrame.plot.density(self[, bw_method, ind])	Generate Kernel Density Estimate plot using Gaussian kernels.
DataFrame.plot.hexbin(self, x, y[, C, …])	Generate a hexagonal binning plot.
DataFrame.plot.hist(self[, by, bins])	Draw one histogram of the DataFrame’s columns.
DataFrame.plot.kde(self[, bw_method, ind])	Generate Kernel Density Estimate plot using Gaussian kernels.
DataFrame.plot.line(self[, x, y])	Plot Series or DataFrame as lines.
DataFrame.plot.pie(self, \*\*kwargs)	Generate a pie plot.
DataFrame.plot.scatter(self, x, y[, s, c])	Create a scatter plot with varying marker point size and color.
DataFrame.boxplot(self[, column, by, ax, …])	Make a box plot from DataFrame columns.
DataFrame.hist(data[, column, by, grid, …])	Make a histogram of the DataFrame’s.
Sparse accessor
Sparse-dtype specific methods and attributes are provided under the DataFrame.sparse accessor.

DataFrame.sparse.density	Ratio of non-sparse points to total (dense) data points represented in the DataFrame.
DataFrame.sparse.from_spmatrix(data[, …])	Create a new DataFrame from a scipy sparse matrix.
DataFrame.sparse.to_coo(self)	Return the contents of the frame as a sparse SciPy COO matrix.
DataFrame.sparse.to_dense(self)	Convert a DataFrame with sparse values to dense.
Serialization / IO / conversion
DataFrame.from_dict(data[, orient, dtype, …])	Construct DataFrame from dict of array-like or dicts.
DataFrame.from_items(items[, columns, orient])	(DEPRECATED) Construct a DataFrame from a list of tuples.
DataFrame.from_records(data[, index, …])	Convert structured or record ndarray to DataFrame.
DataFrame.info(self[, verbose, buf, …])	Print a concise summary of a DataFrame.
DataFrame.to_parquet(self, fname[, engine, …])	Write a DataFrame to the binary parquet format.
DataFrame.to_pickle(self, path[, …])	Pickle (serialize) object to file.
DataFrame.to_csv(self[, path_or_buf, sep, …])	Write object to a comma-separated values (csv) file.
DataFrame.to_hdf(self, path_or_buf, key, …)	Write the contained data to an HDF5 file using HDFStore.
DataFrame.to_sql(self, name, con[, schema, …])	Write records stored in a DataFrame to a SQL database.
DataFrame.to_dict(self[, orient, into])	Convert the DataFrame to a dictionary.
DataFrame.to_excel(self, excel_writer[, …])	Write object to an Excel sheet.
DataFrame.to_json(self[, path_or_buf, …])	Convert the object to a JSON string.
DataFrame.to_html(self[, buf, columns, …])	Render a DataFrame as an HTML table.
DataFrame.to_feather(self, fname)	Write out the binary feather-format for DataFrames.
DataFrame.to_latex(self[, buf, columns, …])	Render an object to a LaTeX tabular environment table.
DataFrame.to_stata(self, fname[, …])	Export DataFrame object to Stata dta format.
DataFrame.to_msgpack(self[, path_or_buf, …])	(DEPRECATED) Serialize object to input file path using msgpack format.
DataFrame.to_gbq(self, destination_table[, …])	Write a DataFrame to a Google BigQuery table.
DataFrame.to_records(self[, index, …])	Convert DataFrame to a NumPy record array.
DataFrame.to_sparse(self[, fill_value, kind])	(DEPRECATED) Convert to SparseDataFrame.
DataFrame.to_dense(self)	(DEPRECATED) Return dense representation of Series/DataFrame (as opposed to sparse).
DataFrame.to_string(self[, buf, columns, …])	Render a DataFrame to a console-friendly tabular output.
DataFrame.to_clipboard(self[, excel, sep])	Copy object to the system clipboard.
DataFrame.style	Property returning a Styler object containing methods for building a styled HTML representation fo the DataFrame.
Sparse
SparseDataFrame.to_coo(self)	Return the contents of the frame as a sparse SciPy COO matrix.