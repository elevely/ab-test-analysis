import numpy as np
import pandas as pd

np.random.seed(42)

N = 100_000

# User IDs
user_id = np.arange(1, N + 1)

# Random assignment to experiment groups
group = np.random.choice(
    ["control", "treatment"],
    size=N,
    p=[0.5, 0.5]
)

# Device
device = np.random.choice(
    ["ios", "android", "web"],
    size=N,
    p=[0.35, 0.50, 0.15]
)

# Acquisition source
source = np.random.choice(
    ["organic", "paid_search", "social", "referral", "email"],
    size=N,
    p=[0.30, 0.25, 0.20, 0.15, 0.10]
)

# Experiment dates
experiment_date = pd.to_datetime(
    np.random.choice(
        pd.date_range("2026-07-01", "2026-07-30"),
        size=N
    )
)

# Everyone in the dataset started registration
registration_started = np.ones(N, dtype=int)

# Base conversion rate
base_conversion = 0.08

# Treatment effect
treatment_uplift = 0.005

# Small realistic differences by device
device_effect = {
    "ios": 0.010,
    "android": 0.000,
    "web": -0.015
}

# Small differences by acquisition source
source_effect = {
    "organic": 0.010,
    "paid_search": -0.005,
    "social": -0.010,
    "referral": 0.015,
    "email": 0.005
}

# Calculate individual conversion probability
probability = np.full(N, base_conversion)

probability += np.where(
    group == "treatment",
    treatment_uplift,
    0
)

probability += np.array([device_effect[d] for d in device])
probability += np.array([source_effect[s] for s in source])

# Keep probabilities within realistic bounds
probability = np.clip(probability, 0.01, 0.20)

# Generate conversion outcome
registration_completed = (
    np.random.random(N) < probability
).astype(int)

# Create dataset
df = pd.DataFrame({
    "user_id": user_id,
    "group": group,
    "registration_started": registration_started,
    "registration_completed": registration_completed,
    "device": device,
    "source": source,
    "experiment_date": experiment_date
})

# Sort by date and user
df = df.sort_values(
    ["experiment_date", "user_id"]
).reset_index(drop=True)

# Save
df.to_csv(
    "data/ab_test_data.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print()
print(df.head())