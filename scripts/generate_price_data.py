import pandas as pd
import numpy as np
from datetime import datetime
import os

np.random.seed(42)
dates = pd.date_range(start="2020-01-01", end="2024-12-01", freq="MS")

def simulate_prices(base, seasonal_amp, noise_amp):
    trend = np.linspace(0, 10, len(dates))  # Simulate a slow upward trend
    seasonal = seasonal_amp * np.sin(np.linspace(0, 12 * np.pi, len(dates)))
    noise = noise_amp * np.random.randn(len(dates))
    return base + trend + seasonal + noise
df = pd.DataFrame({
    'date': dates,
    'diesel_price': simulate_prices(70, 5, 3),
    'fertilizer_price': simulate_prices(900, 30, 20),
    'seed_price': simulate_prices(500, 20, 15)
})

df[['diesel_price', 'fertilizer_price', 'seed_price']] = df[['diesel_price', 'fertilizer_price', 'seed_price']].round(2)

os.makedirs("../data/raw", exist_ok=True)
df.to_csv("data/cleaned/farm_input_prices_cleaned.csv", index=False)
print("✅ Simulated price data saved to data/cleaned/farm_input_prices_cleaned.csv")
