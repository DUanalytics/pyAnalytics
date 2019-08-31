#Topic ----
# importing the statistics module 
import statistics 
#%%Median is often referred to as the robust measure of central location and is less affected by the presence of outliers in data.
#statistics module in Python allows three options to deal with median / middle elements in a data set, which are median(), median_low() and median_high().
#The low median is always a member of the data set. When the number of data points is odd, the middle value is returned. When it is even, the smaller of the two middle values is returned. 
#%%%
# simple list of a set of integers 
set1 = [1, 3, 3, 4, 5, 7] 
set1
# Note: low median will always be  a member of the data-set. 
# Print low median of the data-set 
print("Low median of the data-set is % s "   % (statistics.median_low(set1))) 
# lie within the data-set 
print("Median of the set is % s"       % (statistics.median(set1))) 
print("Low median of the data-set is % s "   % (statistics.median_high(set1))) 
#%%%



#%%%

