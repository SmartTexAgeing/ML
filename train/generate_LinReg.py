# Import required packages
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Create random values
values = np.arange(2, 1000, 2)
labels = np.arange(1, 500, 1)

# Create network model using keras
model = Sequential([Dense(1, input_shape=[1])])
model.compile(optimizer=keras.optimizers.Adam(lr=2), loss=keras.losses.mean_squared_error)

# Train neural network model
model.fit(labels, values, epochs=100)

# Predict and print result
result = model.predict([10])
print(result)

# Save trained model in h5-Format
model.save('Model.h5')
np.savetxt('input.txt', values, delimiter=',') 
np.savetxt('labels.txt', labels, delimiter=',') 

# Import Model
model = tf.keras.models.load_model('Model.h5')

# Convert and optimize
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Store new TFLite-Model
open("model.tflite", "wb").write(tflite_model)

# Python code to use TFLite-Model
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

input_data = np.array([[100]], dtype=np.float32)
interpreter.set_tensor(input_index, input_data)
interpreter.invoke()

# Output Performance from Lite-Model
print(interpreter.get_tensor(output_index))
