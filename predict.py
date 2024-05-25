from cross_val_split import cross_val_split
import pandas as pd
import timesfm
tfm = timesfm.TimesFm(
    context_len=480,
    horizon_len=14,
    input_patch_len=32,
    output_patch_len=128,
    num_layers=20,
    model_dims=1280,
    backend="cpu",
)
tfm.load_from_checkpoint(repo_id="google/timesfm-1.0-200m")
def predict_data(data, initial_window_size, step_size):
    data['unique_id'] = 0
    window_size = initial_window_size
    predictions = pd.Series()
    while window_size < len(data):
    # Split the data into training and testing sets
        train_data, test_data, step_size = cross_val_split(data, window_size, step_size)
        # Fit the model and make predictions
        prediction = tfm.forecast_on_df(train_data, freq="D", value_name='y')['timesfm']
        predictions = pd.concat([predictions, prediction])
        window_size += step_size
    supp = len(predictions) - (window_size - initial_window_size)
    predictions = predictions[:-supp]
    predictions.index = [i for i in range(initial_window_size, window_size)]
    return predictions