# Gaussian Mixture Models for Bag-of-Words Clustering

Use probabilistic Gaussian mixtures to cluster a bag-of-words style feature dataset.

## How It Works

The notebook loads `Clustering_gmm.csv`, fits Gaussian Mixture Models with four components, inspects component means, and assigns cluster labels to observations.

## Local Validation

~~~powershell
cd /d "path\to\repository"
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Limitations

The number of components is a notebook parameter. Clusters are probabilistic groupings and require external validation before being interpreted as classes.

## Suggested Repository Name

`gmm-bag-of-words-clustering`
