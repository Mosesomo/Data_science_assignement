Predictive Maintainance Model

---------------------------------------------------------------------
Overview
========================================================
This respiratory contains code for predictive mainatainance model applied to manufacturing equipements. The model utilizes a Decision Tree Classifier to predict whether maintainance is neede based on the sensor data and maintainance history records.

Files
========================================================
`prediction.py`: This is a python script containing the code for the predictive maintaince model.
`PdM_maint.csv`: This is a csv file containing maintainance history records.
`sensor-data.csv`: This is anothe csv file containing sensor data.

Machine learning Algorithm
===========================================
I applied Decision Tree Classifier algorithm. This algorithm is more suitable for binary classificatiom tasks, making it a good choice for predicting maintainace needs in manufacturing equipment.

Relevant Features
=================================================================
The relevant features from the sensor data used are:
.Power
.Temperature
.Humidity
.Light
.CO2
.Dust

These features are crucial in capturing enviromental conditions and performanace indicators of the manufacturing equipment.

Handling Missing data
========================================================
Missing values in the 'comp' column are filled with label 'No maint' Meaning no maintainance needed. This ensure that data is not lost and allows for the inclusion of the instances with no recorded mainatainance.

Integration Into Manufacturing Process.
============================================================================
The predictive maintainace model can be integrated into manufacturing process to maximize its impact. This can be achieved by:
 ->Real-time Monitoring
 ->Automated alerts.
 ->Schedule inspection.
