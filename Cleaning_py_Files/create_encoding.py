from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encode_change_status_column(df, column_name):
    # Define the custom chronological order
    chronological_order = [
        'Greenland', 
        'Prior Construction', 
        'Land Cleared', 
        'Excavation', 
        'Construction Started', 
        'Materials Dumped', 
        'Materials Introduced', 
        'Construction Midway', 
        'Construction Done', 
        'Operational'
    ]
    
    # Create a custom mapping based on the chronological order
    custom_mapping = {status: idx for idx, status in enumerate(chronological_order)}
    
    # Apply the custom mapping to the specified column
    df[column_name + '_encoded'] = df[column_name].map(custom_mapping)
    
    # Handle None values separately (assigning -1)
    df[column_name + '_encoded'] = df[column_name + '_encoded'].fillna(-1).astype(int)
    
    return df

