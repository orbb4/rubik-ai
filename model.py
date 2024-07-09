import numpy as np
from keras import layers, models


def kociemba_to_onehot(kociemba_str: str) -> np.ndarray:
    """
    Traduce una string kociemba a la secuencia correspondiente
    de acciones.
    """
    color_mapping = {
        "B": [1, 0, 0, 0, 0, 0],
        "L": [0, 1, 0, 0, 0, 0],
        "F": [0, 0, 1, 0, 0, 0],
        "U": [0, 0, 0, 1, 0, 0],
        "R": [0, 0, 0, 0, 1, 0],
        "D": [0, 0, 0, 0, 0, 1],
    }

    onehot_vec = np.concatenate([color_mapping[char] for char in kociemba_str])

    return onehot_vec


patterns = []
steps = []


with open("./data/cube2M.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            pattern, step_count = line.split("-")
            step_count = min(int(step_count) + 1, 20)

            patterns.append(kociemba_to_onehot(pattern))
            steps.append(int(step_count))

X = np.array(patterns)
y = np.array(steps)

model = models.Sequential()
model.add(layers.Flatten(input_shape=(len(X[0]),)))  # Aplanar la entrada
model.add(layers.Dense(1024, activation="relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation="relu"))


model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mae"])


model.fit(X, y, epochs=50, batch_size=128, validation_split=0.2)
model.save("./rubik_solver_model2Mrelu.h5")
