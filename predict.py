import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Maintainance History record of the machine
maintance_data = pd.read_csv('PdM_maint.csv')

# sensor data of the machine
sensor_data = pd.read_csv('sensor-data.csv')

# DataFrames
maint_frame = pd.DataFrame(maintance_data)
sensor_frame = pd.DataFrame(sensor_data)

# converting columns to datetime type
maint_frame['datetime'] = pd.to_datetime(maint_frame['datetime'])
sensor_frame['time'] = pd.to_datetime(sensor_data['time'])

# merging the data sets
merged_data = pd.merge(sensor_frame, maint_frame, left_on='time', right_on='datetime', how='inner')
merged_data = merged_data.drop('time', axis=1)

# Filling the null value
merged_data['comp'].fillna('No maint', inplace=True)

# Extracting features and targeted variables
X = merged_data[['power', 'temp', 'humidity', 'light', 'CO2', 'dust']]
y = (merged_data['comp'] != 'No maint').astype(int)

# Spliting the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg = LinearRegression()
# Training our model
reg.fit(X_train, y_train)

# making prediction on the testing set
y_pred = reg.predict(X_test)
y_pred_binary = (y_pred > 0.5).astype(int)

# checks if atleast one element in the array meets the
# condition that it is greater than 0.5
if (y_pred_binary > 0.5).any():
    print("Maintainance need")
else:
    print("No Maintenance needed")
    
# calculating the accuracy score
accuracy = mean_squared_error(y_test, y_pred_binary)
print("Accuracy Score : ", accuracy)