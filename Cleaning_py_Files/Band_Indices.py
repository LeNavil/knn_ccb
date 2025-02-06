dates = set(col.split("_")[-1] for col in train_df.columns if col.startswith("img_red_mean_"))

# Function to compute indices and drop original RGB columns
def compute_indices(train_df, date):
    R = train_df[f"img_red_mean_{date}"]
    G = train_df[f"img_green_mean_{date}"]
    B = train_df[f"img_blue_mean_{date}"]

    # Compute the selected indices
    train_df[f"ExG_{date}"] = 2 * G - (R + B)  # Excess Green Index
    train_df[f"ExR_{date}"] = 1.4 * R - G  # Excess Red Index
    train_df[f"GLI_{date}"] = (2 * G - R - B) / (2 * G + R + B)  # Green Leaf Index
    train_df[f"VARI_{date}"] = (G - R) / (G + R - B)  # Visible Atmospherically Resistant Index
    train_df[f"NDI_RG_{date}"] = (R - G) / (R + G)  # Normalized Difference Index (Red-Green)

    # Drop the original RGB columns
    train_df.drop(columns=[f"img_red_mean_{date}", f"img_green_mean_{date}", f"img_blue_mean_{date}"], inplace=True)

# Apply function for each date
for date in dates:
    compute_indices(train_df, date)