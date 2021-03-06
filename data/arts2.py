import numpy as np
import pandas as pd

arts = pd.DataFrame()


# 1. Clean the dates so you only see numbers by using string manipulations
arts["execution_date"] = arts["execution_date"].str.findall(r"([0-9]+)").str[0]
arts["execution_date"] = arts["execution_date"].astype(float)
arts.head()

# 1. If a year is lower than 100, then is referred to 1900. For example, 78 is actually 1978, and that needs to be fixed too.
arts["execution_date"] = arts["execution_date"].apply(lambda x: 1900 + x if x < 100 else x)
arts.head()

# 2. Get the average execution year per artist.
arts.groupby("artist_name").mean().head()

# 3. Get the average execution year per category.
arts.groupby("category").mean().head()

# 4. Get the number of artworks per artist. Which artist is the most prolific?
artworks_by_artist = arts.groupby("artist_name")[["title"]].aggregate(np.count_nonzero)
artworks_by_artist.sort("title", ascending=False).head()

# 5. Get the number of artworks per category. Which category has the highest number?
artworks_by_category = arts.groupby("category")[["title"]].aggregate(np.count_nonzero)
artworks_by_category.sort("title", ascending=False).head()

# 6. Get the average length of artworks titles per category and artist.
arts['title_length'] = arts['title'].str.len()
length_by_category = arts.groupby("category")[["title_length"]].aggregate(np.mean)
length_by_category.sort("title_length", ascending=False).head()

# 6. Get the year with the highest production.
artworks_by_year = arts.groupby("execution_date")[["title"]].aggregate(np.count_nonzero)
artworks_by_year.sort("title", ascending=False).head()

# 8. Get the approximate period of production for each artist. If an artist painted from 1970 to 1990, the period is 20.
period_min = arts.groupby("artist_name")[['execution_date']].aggregate(np.min)
period_max = arts.groupby("artist_name")[['execution_date']].aggregate(np.max)
(period_max - period_min).sort("execution_date", ascending=False).head()
