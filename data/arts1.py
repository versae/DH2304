import numpy as np
import pandas as pd

arts = pd.DataFrame()


# Clean the dates so you only see numbers.
def clean_years(value):
    result = value
    chars_to_replace = ["c.", "©", ", CARCC", "no date", "n.d.", " SODRAC", ", CA", " CARCC", ""]
    chars_to_split = ["-", "/"]
    if isinstance(result, str):
        for char in chars_to_split:
            if char in result:
                result = result.split(char)[1].strip()
        for char in chars_to_replace:
            result = result.replace(char, "")
        if result == "":
            return np.nan
        else:
            return int(result)
    else:
        return result

arts['execution_date'] = arts['execution_date'].apply(clean_years)
arts.head()

# If a year is lower than 100, then is referred to 1900. For example, 78 is actually 1978, and that needs to be fixed too.
def clean_year_99(value):
    if value < 100:
        return value + 1900
    else:
        return value

arts["execution_date"] = arts["execution_date"].apply(clean_year_99)
arts.head()
