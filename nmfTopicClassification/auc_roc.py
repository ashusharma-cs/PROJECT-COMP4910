import pandas as pd
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Load data from CSV file into a Pandas DataFrame
tweets_df = pd.read_csv('alltweets_filtered_labelled.csv')

# Drop any rows with NaN values in either column
tweets_df.dropna(subset=['relVirtualCare', 'nmf'], inplace=True)

# Convert 0.5 in "relVirtualCare" column to 1
tweets_df['relVirtualCare'] = tweets_df['relVirtualCare'].apply(lambda x: 1 if x == 0.5 else x)

# Compute AUC score and ROC curve
auc_score = roc_auc_score(tweets_df['relVirtualCare'], tweets_df['nmf'])
fpr, tpr, thresholds = roc_curve(tweets_df['relVirtualCare'], tweets_df['nmf'])

# Compute baseline ROC curve
baseline_fpr = [0, 1]
baseline_tpr = [0, 1]

# Plot ROC curve and baseline
plt.plot(fpr, tpr, label=f"AUC={auc_score:.2f}")
plt.plot(baseline_fpr, baseline_tpr, linestyle='--', color='gray', label='Baseline')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")

# Save ROC curve as PNG file
plt.savefig('roc_curve.png')

# Show ROC curve
plt.show()
