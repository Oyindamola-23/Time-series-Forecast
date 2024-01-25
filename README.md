# Time Series Forecasting using ARIMA

This Python script performs time series forecasting using the ARIMA (AutoRegressive Integrated Moving Average) model on sales data from multiple stores. The script loads the data, conducts store-specific forecasts, plots the results, and saves the forecasted data in CSV format along with corresponding plots.

## Requirements
- Python 3.x
- pandas
- matplotlib
- statsmodels

Install the required packages using:

```bash
pip install pandas matplotlib statsmodels
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Download Data:**

   Place your sales data in CSV format with a column named 'date of sales' and 'Price in Naira'. Save the file as `dabarobjects_data.csv`.

3. **Run the Script:**

   ```bash
   python forecast_script.py
   ```

   The script will create a 'forecast' folder containing individual CSV and PNG files for each store's forecast. The files are automatically zipped and then unzipped.

## Customization

- **Adjust ARIMA Model Parameters:**

  Modify the ARIMA model order inside the `forecast_by_store` function:

  ```python
  model = ARIMA(train['Price in Naira'], order=(p, d, q))
  ```

  Here, `p`, `d`, and `q` are the ARIMA model parameters. Fine-tune these values based on your data and requirements.

- **Training and Testing Set Split:**

  Modify the training and testing set split ratio:

  ```python
  train_size = int(len(store_data) * 0.8)
  ```

  Adjust the percentage of data used for training by changing the value `0.8`.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact:

- Your Name - KELANI SIDIKAT OYINDAMOLA
- Your Email Address - kelanisidikat883@gmail.com

Feel free to reach out if you encounter issues or have suggestions for improvement. Happy forecasting!

---

*Note: Make sure to replace "yourusername" and "your-repository" with your GitHub username and repository name in the clone instructions.*
