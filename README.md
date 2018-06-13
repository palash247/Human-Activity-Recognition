# Human-Activity-Recognition
The project is aimed at recording sensor data for any physical activity from smartphone and then training a model to recognise same activities in real time.

The sensor data is collected using HyperIMU app from Google Play store.
While recording the data the smarphone was taped to the waist from backside.
And while testing it was fixed on that position only.
The model is trained on 2 second frame of data.
Features which were most informative was mean and standard deviation.
The sensors which are used are Accelerometer and Gyroscope.

## To Do:
1. Try using RNN
2. Update code to use HyperIMU's official Python code.
3. Add more activities
4. Try to generelise the model for different persons.
5. Be less lazy.

You can stick the phone wherever you want on your body while recordint training data. Just make sure you stick it at same position with same orientation while testing also.
