# Project Summary: Gaussian Mixture Models

Status: Complete for repository organization, documentation, privacy cleanup, and structural validation.

## Purpose

Group bag-of-words style observations with a probabilistic mixture model.

## Pipeline

Load `Clustering_gmm.csv`, fit a four-component Gaussian Mixture Model, inspect component means, and assign labels.

## Validation

Run `python -m pytest -q` for the notebook structure check. The full notebook run uses the included CSV file.

## Limitation

Component count and initialization affect the clusters; unsupervised labels are not automatically ground truth.
