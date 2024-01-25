import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os
import shutil

# Load the data
df = pd.read_csv('dabarobjects_data.csv', parse_dates=['date of sales'])
df.sort_values(by='date of sales', inplace=True)

# Define a function to forecast for each store
def forecast_by_store(store_id):
    store_data = df[df['storeId'] == store_id]
    store_data.set_index('date of sales', inplace=True)

    # Split the data into training and testing sets (adjust as needed)
    train_size = int(len(store_data) * 0.8)
    train, test = store_data[:train_size], store_data[train_size:]

    # Fit the ARIMA model
    model = ARIMA(train['Price in Naira'], order=(5, 1, 1))  # Adjust order as needed
    model_fit = model.fit()

    # Forecast future values
    forecast_steps = len(test)
    forecast = model_fit.get_forecast(steps=forecast_steps)

    # Save forecast data to CSV
    forecast_df = pd.DataFrame({
        'Date': forecast.predicted_mean.index,
        'Actual': test['Price in Naira'],
        'Forecast': forecast.predicted_mean.values
    })
    forecast_csv_path = f'forecast/forecast_store_{store_id}.csv'
    forecast_df.to_csv(forecast_csv_path, index=False)

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train['Price in Naira'], label='Training Data')
    plt.plot(test.index, test['Price in Naira'], label='Actual Data')
    plt.plot(forecast.predicted_mean.index, forecast.predicted_mean.values, label='Forecasted Data')
    plt.title(f'ARIMA Forecast for Store ID {store_id}')
    plt.xlabel('Date of Sales')
    plt.ylabel('Price in Naira')
    plt.legend()
    forecast_png_path = f'forecast/forecast_store_{store_id}.png'
    plt.savefig(forecast_png_path)
    plt.close()

# Create 'forecast' folder
output_folder = 'forecast'
os.makedirs(output_folder, exist_ok=True)

# Loop through each unique storeId and perform the forecast
unique_store_ids = df['storeId'].unique()
for store_id in unique_store_ids:
    forecast_by_store(store_id)

# Zip the 'forecast' folder
zip_file_path = shutil.make_archive(output_folder, 'zip', output_folder)

# Unzip the 'forecast' folder
shutil.unpack_archive(zip_file_path, output_folder)

print(f"Forecasting completed, CSV and PNG files saved to {output_folder} and automatically unzipped.")
