import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('final-employee-ds.csv')

# Load the TrainingHours column into a NumPy array
training_hours = df['TrainingHours'].values

# Convert to float datatype
training_hours_float = training_hours.astype(float)

# Find mean & standard deviation
mean_training_hours = np.mean(training_hours_float)
std_training_hours = np.std(training_hours_float)

# Final output: Two numeric values
print(f"Mean Training Hours: {mean_training_hours}")
print(f"Standard Deviation of Training Hours: {std_training_hours}")

# Display just the numeric values
print(f"\nFinal Output:")
print(f"{mean_training_hours}")
print(f"{std_training_hours}")