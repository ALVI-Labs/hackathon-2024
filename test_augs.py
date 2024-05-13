import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d

def make_electrode_shifting(data, min_angle, max_angle):
    n_sensors, _ = data.shape
    original_angles = np.linspace(0, 360, num=n_sensors, endpoint=False)
    

    signs = np.random.choice([-1, 1], size=n_sensors)
    random_angles = np.random.uniform(low=min_angle, high=max_angle, size=n_sensors)

    delta_array = signs * random_angles
    new_angles = original_angles + delta_array

    # Vectorized correction to ensure angles are within the 0-360 degree range
    new_angles = (new_angles + 360) % 360

    
    # Vectorized computation of angular distances for all new angles to all original angles
    distances = np.abs(new_angles[:, np.newaxis] - original_angles)
    distances = np.minimum(distances, 360 - distances) / (360 / n_sensors)

    weights = 1 - distances  # Invert distances to get weights
    weights = np.clip(weights, 0, 1)

    rotated_data = np.dot(weights, data)
    
    return rotated_data


def make_electrode_shifting(data, min_angle, max_angle, p=1):
    """
    Apply rotation of the sensors by one angle.

    Also we can aplly some small pertubration for each sensors.
    Also it migh be interestin to use temporal inforamtion and apply
    distraction in spatial and temporal dimension.

    Rotate 8 electrodes by circle with rollover.
    min_angle - in degree
    max_angle - maximum
    prob

    data [8, N]

    """

    # print('WWW', data.shape)
    n_sensors = data.shape[0]
    angles = np.linspace(0, 360, n_sensors+1)[:-1]

    # just only one angle for rotation.
    delta = np.random.choice([-1,1]) * np.random.uniform(low=min_angle, high=max_angle)
    new_angles = np.array([phi + delta  for phi in angles])

    new_angles = np.where(new_angles<0, new_angles+360, new_angles)
    new_angles = np.where(new_angles>360, new_angles-360, new_angles)

    # interpoaltion
    # add 360 degree for interpoaltion.
    x_ = np.append(angles, 360.)
    data_expand = np.concatenate([data, data[:1]])

    f1 = interp1d(x_, data_expand, kind='cubic', axis=0)
    res = f1(new_angles)

    return res


import matplotlib.pyplot as plt
from time import time 
# Set seed for reproducibility
np.random.seed(42)

# Generate data consisting of 8 random sine waves with 256 time points
t = np.linspace(0, 2 * np.pi, 256)
data = np.array([np.sin(t + np.random.uniform(0, 2 * np.pi)) for _ in range(8)])

# Apply both the original and optimized matrix interpolation functions to the data
st = time()
for i in range(1000):
    original_output = build_and_apply_rotation_matrix(data, 0, 20)
print(time() - st)

st = time()
for i in range(1000):
    output = make_electrode_shifting(data, 0, 20)
print(time() - st)

# Visualization using imshow
fig, axs = plt.subplots(1, 2, figsize=(18, 6))

# Original data
axs[0].imshow(data, aspect='auto', cmap='viridis')
axs[0].set_title('Original Data')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Electrodes')

# Output from the original matrix interpolation function
axs[1].imshow(original_output, aspect='auto', cmap='viridis')
axs[1].set_title('Original Matrix Interpolation Output')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Electrodes')

plt.tight_layout()
plt.show()
