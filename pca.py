import numpy as np
from sklearn.decomposition import PCA

data = np.load('stcs_early_2_normal.npy')
n_components = 5


data = np.reshape(data, (data.shape[-1], data.shape[-2], data.shape[-3]))
print(data.shape)

data_2d = np.array([features_2d.flatten() for features_2d in data])

print(data_2d.shape)

pca = PCA(n_components=n_components)
pca.fit(data_2d)
data_pca = pca.transform(data_2d)

print(data_pca.shape)

np.save(data_pca, 'path/stcs_early_2_pca')