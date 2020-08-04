# UTHealth Summer 2020 Research Project
[![NPM version](https://badge.fury.io/js/esta.svg)](http://badge.fury.io/js/esta)
Constructed time series analysis and recurrent neural networks in GDP prediction under the global pandemic. Grasped data from remote data access, added in employment rate, cases of infection and indices for better representation, evaluation and optimization.

# Useful concepts
- Time Series Anomaly Detection Algorithms:https://blog.statsbot.co/time-series-anomaly-detection-algorithms-1cef5519aef2
- Deep learning in python:https://github.com/neelabhpant/Deep-Learning-in-Python
- Using LSTMs to perform time series analysis:https://xiaozhuanlan.com/topic/7524093618
- Stock Market price prediction using sci-kit learn: https://blog.usejournal.com/stock-market-prediction-by-recurrent-neural-network-on-lstm-model-56de700bff68

# Remote Data Source
For personal documentation purposes, NY.GDP.MKTP.CD remote data access source:https://data.worldbank.org/indicator/NY.GDP.MKTP.CD

# Prediction Model & Pre-processing of the Data
Graphic representation of the model can be found as a pdf file in the main directory.
Normalization was achieved by `df_scaled = df/df.loc[2000]`

# Observed results Summary
After importing, normalizing and training with the world bank data(indicator ‘NY.GDP.MKTP.CD’, the test set reached losses lowest at 1.3291694813233335e-05 with RMSprop optimizer. Though the RMSprop resulted in some minor variation in the losses of both training dataset and test dataset. Stochastic gradient descent performed especially well in the training dataset with a final loss less than 6x10^5, but relatively weak when moved on to the test dataset. For the detailed table, see repository.
