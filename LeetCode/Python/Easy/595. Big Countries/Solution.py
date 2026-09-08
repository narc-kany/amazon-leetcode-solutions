import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    bc_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return bc_df[['name', 'population', 'area']]
    