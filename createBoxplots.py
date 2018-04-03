import matplotlib.pyplot as plt
import os
import pandas as pd
import sys


def create_boxplot(filename):
    name = filename[:-4]
    print(name)
    data = pd.read_csv(filename, sep=';')
    fig = data.plot.box().get_figure()
    fig.autofmt_xdate()
    fig.savefig(name + '.png',  dpi=300)
    plt.close(fig)

directory_str = sys.argv[1]
directory = os.fsencode(directory_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        create_boxplot(os.path.join(directory_str, filename))

