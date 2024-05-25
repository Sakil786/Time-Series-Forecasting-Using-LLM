# -*- coding: utf-8 -*-
"""cross_val_split.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dLw7G9K9v8n0cP4EP0Kpe8-6JGHL32c9
"""

def cross_val_split(data, window_size, step_size):
    train_data = data[0 : window_size]
    if window_size + step_size > len(data):
        test_data = data[window_size :]
        step_size = len(data) - window_size
    else:
        test_data = data[window_size : window_size + step_size]
    return train_data, test_data, step_size