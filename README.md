# Muscle interface hackathon


## Data

### Strcuture.

We collected data during repetitive motor task. Datasets were recorded on healthy persons and person with hand amputation. 
To evaluate your solution we chose on amputee person. We collected 3 sessions and did same movements. Each session is approximately 20-30 mins. 
We separate it on train/test/submit respectively.
train and test have labels, submit has only EMG signals. 

Each person has N .npz files. That's data for some task.

Description of the data 
['data_myo', 'data_vr', 'data_angles', 'myo_ts']

myo consists of 8 electrodes nad were recorded with 200 fps
data_myo is preprocess and interpolated 
data_vr - interpolated joints quanternions 
data_angles - angles of the joints extracted from data_vr. 
myo_ts - time series of the myo signals.

Evaluation will be in the form of angle error. 

- MAE on downsamples angles.
- 200 fps -> 25 fps so 8x downsampl. 
- Example of submission file




### Dataset description 

We train model directrly to squeeze dimension. 

Size of the input (8, 256) || Size of the output (20, 32)

In case you want to train model on all people and test on fedya only.
During dataset creation we preprocess different hands and change orientation of the electrodes for "left" hands. 

datasets=['../../data/processed/dataset_v2_blocks', 
        '../../data/processed/dataset_v1_big'],
hand_type = ['left', 'right'],
human_type = ['health', 'amputant'],
test_dataset_list = ['fedya_tropin_standart_elbow_left']