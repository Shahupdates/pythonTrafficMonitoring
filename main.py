import tkinter as tk
from recommendation_system import recommend_handler
import grpc
from tensorflow_serving.apis import prediction_service_pb2_grpc
from tensorflow_serving.apis import predict_pb2

def create_gui():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Recommendation System")
    window.geometry("400x250")

    # Create GUI elements
    age_label = tk.Label(window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(window)
    age_entry.pack()

    gender_label = tk.Label(window, text="Gender:")
    gender_label.pack()
    gender_var = tk.StringVar()
    gender_radio_male = tk.Radiobutton(window, text="Male", variable=gender_var, value=1)
    gender_radio_male.pack()
    gender_radio_female = tk.Radiobutton(window, text="Female", variable=gender_var, value=0)
    gender_radio_female.pack()

    product_label = tk.Label(window, text="Product Interest:")
    product_label.pack()
    product_entry = tk.Entry(window)
    product_entry.pack()

    recommend_button = tk.Button(window, text="Recommend", command=lambda: recommend_with_serving(age_entry.get(), gender_var.get(), product_entry.get(), result_label))
    recommend_button.pack()

    result_label = tk.Label(window, text="Recommendations will appear here")
    result_label.pack()

    window.mainloop()

def recommend_with_serving(age, gender, product, result_label):
    # Create a gRPC channel to connect to the TensorFlow Serving server
    channel = grpc.insecure_channel('localhost:8500')

    # Create a stub for the prediction service
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

    # Create a request
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'your_model_name'
    request.model_spec.version.value = int('your_model_version')

    # Prepare input data
    input_data = {'age_in_days': int(age), 'is_male': int(gender), 'product_interest': product}
    # Set the input data in the request
    request.inputs['input_data'].CopyFrom(tf.make_tensor_proto(input_data))

    # Send the prediction request
    response = stub.Predict(request)

    # Process the response
    output_data = tf.make_ndarray(response.outputs['output_data'])

    # Update the result label with recommendations
    result_label.config(text=str(output_data))

if __name__ == '__main__':
    create_gui()
