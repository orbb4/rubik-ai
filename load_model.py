import keras
import numpy as np


# función para convertir la notación de kociemba a one-hot encoding
def kociemba_to_onehot(kociemba_str):
    color_mapping = {
        'B': [1, 0, 0, 0, 0, 0],
        'L': [0, 1, 0, 0, 0, 0],
        'F': [0, 0, 1, 0, 0, 0],
        'U': [0, 0, 0, 1, 0, 0],
        'R': [0, 0, 0, 0, 1, 0],
        'D': [0, 0, 0, 0, 0, 1]
    }
    onehot_vec = np.concatenate([color_mapping[char] for char in kociemba_str])
    return np.array([onehot_vec])


patterns = []
steps = []
with open("./data/test_data.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            pattern, step_count = line.split('-')
            step_count = str(int(step_count) + 1)
            if int(step_count) > 20:
                step_count = "20"

            patterns.append(kociemba_to_onehot(pattern))
            steps.append(int(step_count))


model = keras.models.load_model('./rubik_solver_model2Mrelu.h5')

kociemba_cube = "FFRUUULRRDLUDRRBRRBFFBFFBDDRLLBDDLDDDRUFLUFLUFLLBBUBBU"
error = 0
for i in range(len(patterns)):
    predicted_steps = model.predict(patterns[i])
    predicted_steps_value = predicted_steps[0][0]
    print(f"The model predicts this cube is approximately {predicted_steps_value:.2f} steps away from being solved.")
    error += abs(steps[i] - predicted_steps_value)
error/=len(patterns)
print("off by: " + str(error) + " steps")