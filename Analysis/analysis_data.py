from pathlib import Path

import numpy as np
import pandas as pd

if __name__ == '__main__':
    channel_file_path = Path("channels.csv")
    with open(channel_file_path, "r", encoding="utf-8") as f:
        channels = pd.read_csv(f)
    channel_without_capacity = channels.loc[channels['capacity'].isnull()]
    channel_with_capacity = channels.loc[channels['capacity'].notna()]
    hided_capacity = list(
        channel_with_capacity["capacity"] - channel_with_capacity["htlc_maximum_msat"]/1000)
    print(min(hided_capacity))
    print(max(hided_capacity))
    print(np.nanmean(hided_capacity))
    print(np.nanmedian(hided_capacity))
