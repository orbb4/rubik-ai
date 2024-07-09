import numpy as np
from keras import callbacks, layers, models, regularizers


def kociemba_to_onehot(kociemba_str: str) -> np.ndarray:
    """Transforma de una secuencia kociemba al patrón correspondiente"""
    color_mapping = {
        "B": [1, 0, 0, 0, 0, 0],
        "L": [0, 1, 0, 0, 0, 0],
        "F": [0, 0, 1, 0, 0, 0],
        "U": [0, 0, 0, 1, 0, 0],
        "R": [0, 0, 0, 0, 1, 0],
        "D": [0, 0, 0, 0, 0, 1],
    }

    onehot_vec: np.ndarray = np.concatenate(
        [color_mapping[char] for char in kociemba_str], dtype=np.int8
    )
    return onehot_vec


patterns = []
steps = []

with open("./data/combined_data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            pattern, step_count = line.split("-")
            step_count = min(int(step_count) + 1, 20)

            patterns.append(kociemba_to_onehot(pattern))
            steps.append(step_count)

X = np.array(patterns)
y = np.array(steps)


y = y / 20.0


X = X.reshape((X.shape[0], 54, 6, 1))

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(54, 6, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.Flatten())
model.add(
    layers.Dense(
        1024,
        activation="relu",
        kernel_regularizer=regularizers.l2(0.001),
    ),
)
model.add(layers.Dropout(0.5))
model.add(
    layers.Dense(
        512,
        activation="relu",
        kernel_regularizer=regularizers.l2(0.001),
    ),
)
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation="linear"))

model.compile(
    optimizer="adam",
    loss="mean_squared_error",
    metrics=["mae"],
)


early_stopping = callbacks.EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True,
)

model.fit(
    X,
    y,
    epochs=100,
    batch_size=128,
    validation_split=0.2,
    callbacks=[early_stopping],
)
model.save("./rubik_solver_model_cnn.h5")
