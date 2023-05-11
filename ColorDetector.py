import cv2
import numpy as np
from sklearn.cluster import KMeans

# Load image
img = cv2.imread('image.jpg')

# Convert image from BGR to RGB color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshape the image to a 2D array of pixels
img = img.reshape((img.shape[0] * img.shape[1], 3))

# Determine the number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(img)
    wcss.append(kmeans.inertia_)
    
num_clusters = 3 # Choose the number of clusters to use

# Perform k-means clustering on the pixel values
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(img)

# Extract the dominant colors from the cluster centers
colors = kmeans.cluster_centers_

# Display the dominant colors
for color in colors:
    color = np.uint8(color)
    color_img = np.zeros((100, 100, 3), np.uint8)
    color_img[:, :, :] = color
    color_img = cv2.cvtColor(color_img, cv2.COLOR_RGB2BGR)
    cv2.imshow('Color', color_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
