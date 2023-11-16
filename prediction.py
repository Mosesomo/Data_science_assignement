import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Maintenance History record of the machine
maintance_data = pd.read_csv('PdM_maint.csv')

# Sensor data of the machine
sensor_data = pd.read_csv('sensor-data.csv')

# DataFrames
maint_frame = pd.DataFrame(maintance_data)
sensor_frame = pd.DataFrame(sensor_data)

# Converting columns to datetime type
maint_frame['datetime'] = pd.to_datetime(maint_frame['datetime'])
sensor_frame['time'] = pd.to_datetime(sensor_data['time'])

# Merging the datasets
merged_data = pd.merge(sensor_frame, maint_frame, left_on='time', right_on='datetime', how='inner')
merged_data = merged_data.drop('time', axis=1)

# Hanndling missing data
merged_data['comp'].fillna('No maint', inplace=True)

# Extracting features and targeted variables
X = merged_data[['power', 'temp', 'humidity', 'light', 'CO2', 'dust']]
y = (merged_data['comp'] != 'No maint')

# Splitting the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Training our model
clf.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = clf.predict(X_test)

# Calculating the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy)

# Printing the result based on the predicted values
if accuracy > 0.5:
    print("Maintenance needed")
else:
    print("No Maintenance needed")
