from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    channel_file_path = Path("../peruned_edges.csv")
    capacity_file_path = Path("../Crawler/Crawler/spiders/scid_capacity.csv")
    with open(channel_file_path, "r", encoding="utf-8") as f:
        channels = pd.read_csv(f)
    with open(capacity_file_path, "r", encoding="utf-8") as f:
        capacities = pd.read_csv(f)
    channels = channels.rename(columns={"Unnamed: 0": "scid"})
    first_record = list(capacities.columns)
    capacities = capacities.rename(
        columns={"588630x1840x1": "scid", "500000": "capacity"})
    capacities = capacities.append(
        {"scid": first_record[0], "capacity": first_record[1]}, ignore_index=True)
    channels["capacity"] = ""
    for index, row in capacities.iterrows():
        current_scid = row["scid"]
        current_capacity = row["capacity"]
        scid_list = [current_scid+"/0", current_scid+"/1"]
        channels.loc[channels['scid'].isin(
            scid_list), 'capacity'] = current_capacity
    channels.to_csv(r'channels.csv', index=True, header=True)
