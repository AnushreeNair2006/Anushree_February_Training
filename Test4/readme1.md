Student Exam Score(Supervised learning)
The dataset contains columns:student_id,hours_studied,sleep_hours,attendance_percent,previous_scores,exam_score.
The dataset has zero null values and missing values.
This dataset contai only one object datatype column i.e student_id which is been dropped.
For dataset cleaning: dropping of duplicates, student_id was performed.
As there was no wrong datatype entry this was not done, and encoding was also not needed for this dataset.
The Algorithms used were multiple and simple linear regression, decision tree and random forest.
For Simple linear regression:Training Set Matrics:
MAE: 2.29
MSE: 7.20
RMSE: 2.68
R² Score: 0.84
Test Set Matrics:
MAE: 2.31
MSE: 7.76
RMSE: 2.79
R² Score: 0.85
For Decision tree:Training Set Matrics:
MAE: 0.00
MSE: 0.00
RMSE: 0.00
R² Score: 1.00
Test Set Matrics:
MAE: 4.25
MSE: 25.65
RMSE: 5.06
R² Score: 0.52
Training Set (Best Tree) Matrics:
MAE: 2.21
MSE: 7.64
RMSE: 2.76
R² Score: 0.83
Test Set (Best Tree) Matrics:
MAE: 3.84
MSE: 18.93
RMSE: 4.35
R² Score: 0.64
For Random forest:Training Set Metrics:
MAE: 1.03
MSE: 1.62
RMSE: 1.27
R² Score: 0.96
Test Set Metrics:
MAE: 2.97
MSE: 11.03
RMSE: 3.32
R² Score: 0.79
Training Set Metrics:
MAE: 1.52
MSE: 3.73
RMSE: 1.93
R² Score: 0.92
Test Set Metrics:
MAE: 2.84
MSE: 10.51
RMSE: 3.24
R² Score: 0.80
Multiple factors such as hours studied, sleep, attendance, and previous scores responsible for students exam performance. Multiple Linear Regression provided a baseline for understanding linear relationships between features and exam scores.Decision Tree Regression initially overfit the training data, but after hyperparameter tuning, it generalized better to test data with improved R² and lower errors.Random Forest Regression further improved performance by averaging multiple trees, reducing overfitting, and achieving the best test set accuracy. This helps in model selection acc. to which random forest fits well the dataset and correct reading