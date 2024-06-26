# -*- coding: utf-8 -*-
"""util.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r2OPa-L-NvbndmdXE-9GW1JInvSZZDJU
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
import timesfm
import warnings
warnings.filterwarnings('ignore')

class CustomData:
    def __init__(self):
        # self.data = None
        self.window_size = 500
        self.step_size = 14
      #   self. tfm = timesfm.TimesFm(
      #     context_len=480,
      #     horizon_len=14,
      #     input_patch_len=32,
      #     output_patch_len=128,
      #     num_layers=20,
      #     model_dims=1280,
      #     backend="cpu",
      # )
      #   self.tfm.load_from_checkpoint(repo_id="google/timesfm-1.0-200m")
        self.data_path = 'Gold_price_data.csv'

    def read_file(self, file_path=None):
        if file_path is None:
            file_path = self.data_path
        try:
            self.data = pd.read_csv(file_path)
            print("File read successfully.")
            self.data['ds'] = pd.to_datetime(self.data['Date'])
            self.data.drop(columns=['Date'], inplace=True)
            self.data.rename(columns={'Price': 'y'},inplace=True)
        except Exception as e:
            print(f"An error occurred: {e}")
        return self.data