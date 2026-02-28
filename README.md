Missing values are handled using different methods.
Median is used for numerical columns like age and hourly_rate because it is not affected by extreme values (outliers).
Mode is used for categorical/binary columns like is_active because it fills missing values with the most common value.
One-Hot Encoding:Best for small nominal categories.
Label Encoding:Simple and good for tree-based models.
Ordinal Encoding: is used when categories have order.
Frequency Encoding → Helpful when categories are many.
Target Encoding → Useful because it shows relation with target variable.
Outliers were detected using the IQR method.
Extreme values in salary/hourly_rate were capped.
This made the data more stable and balanced.
Outliers were detected using the IQR method.
Extreme values in salary/hourly_rate were capped.
This made the data more stable and balanced.
