# %% Imports
import logging
import sys
from pathlib import Path

import pandas as pd

from plotnine import *

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# %% Import data

# file_dir = Path(__file__).parent.resolve()
# data_source = os.environ.get('DATA_SOURCE', None) or file_dir

data = Path("localstack-2.0.1-lambda-v2/test_invoke_warm_start_arm64/2023-04-13T11-17-31_test_invoke_warm_start.csv")
plots_path = Path("plots")

data_mapping = {
    "v1_docker": "localstack-2.0.1-lambda-legacy/test_invoke_warm_start/2023-04-12T23-01-33_test_invoke_warm_start.csv",
    "v2_docker_warm": "localstack-2.0.1-lambda-v2/test_invoke_warm_start/2023-04-12T22-56-16_test_invoke_warm_start.csv",
    "v2_docker_cold": "localstack-2.0.1-lambda-v2/test_invoke_cold_start/2023-04-12T23-37-52_test_invoke_cold_start.csv",
    "v2_docker_cold_arm64": "localstack-2.0.1-lambda-v2/test_invoke_cold_start_arm64/2023-04-13T12-45-22_test_invoke_cold_start.csv",
    "v2_docker_warm_arm64": "localstack-2.0.1-lambda-v2/test_invoke_warm_start_arm64/2023-04-13T11-17-31_test_invoke_warm_start.csv",
    "v2_host_cold_linux": "localstack-f61bb5b5-lambda-v2/test_invoke_cold_start_host_linux/2023-04-13T13-14-03_test_invoke_cold_start.csv",
    "v2_host_cold_arm64": "localstack-f61bb5b5-lambda-v2/test_invoke_cold_start_host_arm64/2023-04-13T15-24-51_test_invoke_cold_start.csv",
}

dfs = []
for label, data_path in data_mapping.items():
    df = pd.read_csv(data_path, header=None, names=["time_seconds"])
    df["label"] = label
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

# %% Plot

p = (
    ggplot(df, aes(x="label", y="time_seconds"))
    + geom_violin(df)
    + theme(axis_text_x=element_text(rotation=90, hjust=1))
)
p.save(path=plots_path, filename=f"invoke_time.pdf")
p

# %% Summary Stats

df_grouped = df.groupby('label')["time_seconds"].quantile([0, 0.5, 0.95, 0.99, 1]).reset_index()
df_grouped

# pip install tabulate
# print(df_grouped.to_markdown())

# %%
