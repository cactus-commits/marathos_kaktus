import re

# Function for snackecase
def to_snakecase(text):
    return re.sub(r"[\s/]+", "_", text.strip().casefold()) # <- casefold is better than lower in this case

# Use for all columns
def rename_columns_to_snackecase(df):
    new_columns = [to_snakecase(col) for col in df.columns]
    return df.toDF(*new_columns)
