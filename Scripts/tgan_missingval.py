import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import tensorflow as tf
from tensorflow.keras import layers

# Load your dataset from an Excel file
# Replace 'your_data.xlsx' with the path to your actual dataset
data = pd.read_excel('../data/Branching/synth.xlsx', engine='openpyxl')

# Identify missing values
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Fill missing values with mean for initial preprocessing
imputer_mean = SimpleImputer(strategy='mean')
data_mean_imputed = pd.DataFrame(imputer_mean.fit_transform(data), columns=data.columns)

# Normalize the data
data_normalized = (data_mean_imputed - data_mean_imputed.min()) / (data_mean_imputed.max() - data_mean_imputed.min())

# Define the GAN model
def build_generator():
    model = tf.keras.Sequential([
        layers.Dense(128, activation='relu', input_dim=100),
        layers.Dense(256, activation='relu'),
        layers.Dense(data_normalized.shape[1], activation='sigmoid')
    ])
    return model

def build_discriminator():
    model = tf.keras.Sequential([
        layers.Dense(256, activation='relu', input_dim=data_normalized.shape[1]),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

generator = build_generator()
discriminator = build_discriminator()

discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Combine the generator and discriminator into a GAN
gan_input = layers.Input(shape=(100,))
generated_data = generator(gan_input)
discriminator.trainable = False
gan_output = discriminator(generated_data)
gan = tf.keras.Model(gan_input, gan_output)
gan.compile(optimizer='adam', loss='binary_crossentropy')

# Train the GAN model
def train_gan(gan, generator, discriminator, data, epochs=10000, batch_size=32):
    for epoch in range(epochs):
        # Train the discriminator
        noise = np.random.normal(0, 1, (batch_size, 100))
        generated_data = generator.predict(noise)
        real_data = data[np.random.randint(0, data.shape[0], batch_size)]
        combined_data = np.concatenate([real_data, generated_data])
        labels = np.concatenate([np.ones((batch_size, 1)), np.zeros((batch_size, 1))])
        d_loss = discriminator.train_on_batch(combined_data, labels)

        # Train the generator
        noise = np.random.normal(0, 1, (batch_size, 100))
        misleading_labels = np.ones((batch_size, 1))
        g_loss = gan.train_on_batch(noise, misleading_labels)

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Discriminator Loss: {d_loss}, Generator Loss: {g_loss}")

train_gan(gan, generator, discriminator, data_normalized.values)

# Generate synthetic data
noise = np.random.normal(0, 1, (data.shape[0], 100))
synthetic_data = generator.predict(noise)
synthetic_data = synthetic_data * (data_mean_imputed.max() - data_mean_imputed.min()) + data_mean_imputed.min()
synthetic_data = pd.DataFrame(synthetic_data, columns=data.columns)

# Fill missing values with synthetic data
data_filled = data.copy()
for column in data.columns:
    missing_indices = data[data[column].isnull()].index
    data_filled.loc[missing_indices, column] = synthetic_data.loc[missing_indices, column]

# Save the filled data to a CSV file
data_filled.to_csv('../data/data_filled_with_synthetic.csv', index=False)

print("Missing values have been filled with synthetic data. The filled data is saved to 'data_filled_with_synthetic.csv'.")
