import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load a pre-trained MobileNetV2 model 
model = tf.keras.applications.MobileNetV2(weights='imagenet')

def diagnose_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    return decoded_predictions[0][1]  # Return the top diagnosis

# Example usage
image_path = 'path_to_medical_image.jpg'
diagnosis = diagnose_image(image_path)
print(f"Diagnosis: {diagnosis}")


# Simulate a basic patient database
patient_records = {
    "patient1": {
       "patient1": {
        "name": "Michael Mot",
        "age": 21,
        "diagnosis": "Hypertension"
        
    },
  "patient2": {
        "name": "Mokoena Rafael",
        "age": 22,
        "diagnosis": "Tuberculosis"
    }
   
}
}

def get_patient_info(patient_id):
    if patient_id in patient_records:
        return patient_records[patient_id]
    else:
        return None

# Check if patient information is found
patient_id = "patient1"
patient_info = get_patient_info(patient_id)
if patient_info:
    print(f"Patient Info: {patient_info}")
else:
    print("Patient not found.")
