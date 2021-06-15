from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    old_channel_file_path = Path("../channels_20201203.csv")
    new_channel_file_path = Path("../channels_20210104.csv")
    capacity_file_path = Path("../Crawler/Crawler/spiders/scid_capacity.csv")
    with open(old_channel_file_path, "r", encoding="utf-8") as f:
        old_channels = pd.read_csv(f)
    with open(new_channel_file_path, "r", encoding="utf-8") as f:
        new_channels = pd.read_csv(f)
    old_channels = old_channels.rename(columns={"Unnamed: 0": "scid"})
    new_channels = new_channels.rename(columns={"Unnamed: 0": "scid"})
    numbers = 0
    changed_numbers = 0
    for index, row in old_channels.iterrows():
        old_scid = row["scid"]
        old_max_mast = row["htlc_maximum_msat"]
        new_max_mast = new_channels.loc[new_channels['scid']
                                        == old_scid]
        if len(new_max_mast.index) != 0:
            numbers += 1
            new_max_mast = list(new_max_mast["htlc_maximum_msat"])[0]
            if new_max_mast != old_max_mast:
                changed_numbers += 1
            print(changed_numbers/numbers)
    # print(numbers)
    # print(changed_numbers)
