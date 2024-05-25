# Time-Series-Forecasting-Using-LLM

# TimesFM (Time Series Foundation Model)
TimesFM  is a pretrained time-series foundation model developed by Google Research for time-series forecasting.
It is a decoder-only foundation model for time-series forecasting.It is pre-trained on a large time-series corpus of 100 billion real world time-points, that displays impressive zero-shot performance on a variety of public benchmarks from different domains and granularities.

# Pretraining data for TimesFM:
## Synthetic Data:
Helps with learning basic temporal patterns. Created using statistical models or physical simulations, it teaches the model the grammar of time series forecasting.

## Real-World Data:
Adds depth and context. A large corpus of 100 billion time-points is curated from public time series datasets, including Google Trends and Wikipedia Pageviews. These datasets reflect real-world trends and patterns, enhancing the model's ability to generalize and understand domain-specific contexts not seen during training.


Google trains a decoder-only foundation model for time-series forecasting using a large pretraining corpus of 100 billion real-world time-points, primarily composed of search interest time-series data from Google Trends and pageviews from Wikipedia. They demonstrate that even a relatively small 200 million parameter pretrained model utilizing the TimesFM architecture exhibits impressive zero-shot performance across various public benchmarks from different domains and granularities.





