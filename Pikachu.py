import pandas as pd; import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas import Series
from scipy.cluster.vq import kmeans, vq, whiten
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

## Themes for plots
from jupyterthemes import jtplot
# onedork | grade3 | oceans16 | chesterish | monokai | solarizedl | solarizedd
jtplot.style(theme='grade3')
