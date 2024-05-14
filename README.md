# Muscle interface hackathon

## Introduction
We collected data during repetitive motor tasks. The datasets were recorded from healthy individuals and an individual with a hand amputation. To evaluate your solution, we selected data from the amputee. Three sessions were recorded, with each session lasting approximately 20-30 minutes. The data is divided into train, test, and submit sets. The train and test sets include labels, while the submit set contains only EMG signals.

## How to start.
There're 4 notebooks in notebooks folder.
- train baseline
- calculate metrics
- make submission
- visaulize prediction

## Dataset Details
Each individual has multiple `.npz` files corresponding to different tasks.

The dataset contains the following components:
- **data_myo**: Preprocessed and interpolated data from 8 electrodes, recorded at 200 fps.
- **data_vr**: Interpolated joint quaternions.
- **data_angles**: Joint angles extracted from `data_vr`.
- **myo_ts**: Time series of the myo signals.

## Evaluation
Evaluation will be based on the angle error, specifically the Mean Absolute Error (MAE) on downsampled angles. The data is downsampled from 200 fps to 25 fps (8x downsampling).

## Example Submission
Provide an example of a submission file here. See notebooks.

## Dataset Description
We train the model to directly reduce the dimensions. 

- **Input Size**: (8, 256)
- **Output Size**: (20, 32)

If you want to train the model on data from all individuals but test only on the amputee (Fedya), we preprocess different hands and adjust the electrode orientation for "left" hands.

## Additional Notes
- **Datasets**: `['../../data/processed/dataset_v2_blocks', '../../data/processed/dataset_v1_big']`
- **Hand Type**: `['left', 'right']`
- **Human Type**: `['healthy', 'amputee']`
- **Test Dataset List**: `['fedya_tropin_standart_elbow_left']`
