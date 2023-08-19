# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12jtQf6tT4MGOPTiGzGohUl_MP8GUuGaK
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import os
import struct
from scipy.io import wavfile as wav
import IPython.display as ipd
from IPython.display import Image
import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
# %matplotlib inline

import pandas as pd
meta_data=pd.read_csv('https://drive.google.com/drive/folders/1MAptmPLf4c1GMhvw6f46z6M0q0H8bwY8?usp=drive_link', on_bad_lines='skip')
audio_dataset_path='UrbanSound8K/audio/'
print(meta_data.shape)
meta_data.head(10)

meta_data.isnull().sum()

### Check whether the dataset is imbalanced
meta_data['class'].value_counts()

