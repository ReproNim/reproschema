# Analyze Collected Data

Process and analyze data collected from your ReproSchema protocol.

## Goal

Extract insights from protocol responses and prepare them for analysis.

## Prerequisites

- Completed data collection
- Exported protocol responses
- Basic knowledge of data analysis tools (R, Python, etc.)

## Steps

### 1. Export Data

#### From reproschema-server
```bash
# Login to your server
ssh your-server

# Export responses
docker exec reproschema-server python manage.py export_responses --output-dir ./exports
```

#### From GitHub Pages
Data is stored in browser localStorage. Use the export function in the UI:
1. Open protocol in reproschema-ui
2. Click "Export Data"
3. Download JSON or CSV format

### 2. Load Data in Python

```python
import json
import pandas as pd

# Load JSON export
with open('responses.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['responses'])

# Preview data
print(df.head())
```

### 3. Load Data in R

```r
library(jsonlite)

# Load JSON export
data <- fromJSON("responses.json")

# Convert to data frame
df <- as.data.frame(data$responses)

# Preview data
head(df)
```

### 4. Data Cleaning

#### Handle Missing Values
```python
# Identify missing values
df.isnull().sum()

# Fill or drop
df = df.dropna(subset=['important_column'])
```

#### Convert Data Types
```python
# Convert to appropriate types
df['response_time'] = pd.to_datetime(df['response_time'])
df['score'] = df['score'].astype(float)
```

### 5. Score Calculation

#### Example: PHQ-9 Scoring
```python
# PHQ-9 items
phq9_items = ['phq9_1', 'phq9_2', 'phq9_3', 'phq9_4',
              'phq9_5', 'phq9_6', 'phq9_7', 'phq9_8', 'phq9_9']

# Calculate total score
df['phq9_total'] = df[phq9_items].sum(axis=1)

# Interpret scores
def interpret_phq9(score):
    if score <= 4:
        return 'Minimal'
    elif score <= 9:
        return 'Mild'
    elif score <= 14:
        return 'Moderate'
    else:
        return 'Severe'

df['phq9_severity'] = df['phq9_total'].apply(interpret_phq9)
```

### 6. Exploratory Analysis

#### Summary Statistics
```python
# Descriptive statistics
df.describe()

# Distribution
df['phq9_total'].hist()
```

#### Correlation Analysis
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation matrix
corr = df[phq9_items].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
```

### 7. Visualization

#### Score Distribution
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='group', y='phq9_total', data=df)
plt.title('PHQ-9 Scores by Group')
plt.show()
```

#### Time Series
```python
df.groupby('response_date')['phq9_total'].mean().plot()
plt.title('Average PHQ-9 Over Time')
plt.xlabel('Date')
plt.ylabel('Score')
plt.show()
```

### 8. Statistical Testing

#### t-test
```python
from scipy import stats

group1 = df[df['group'] == 'control']['phq9_total']
group2 = df[df['group'] == 'treatment']['phq9_total']

t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t-statistic: {t_stat:.2f}, p-value: {p_value:.3f}")
```

#### ANOVA
```python
from scipy import stats

groups = [group['phq9_total'].values for name, group in df.groupby('condition')]
f_stat, p_value = stats.f_oneway(*groups)
print(f"F-statistic: {f_stat:.2f}, p-value: {p_value:.3f}")
```

## Advanced Analysis

### Mixed Effects Models
```python
import statsmodels.formula.api as smf

# Linear mixed model
model = smf.mixedlm("phq9_total ~ time + group", data=df,
                    groups=df["participant_id"])
results = model.fit()
print(results.summary())
```

### Longitudinal Analysis
```python
# Track changes over time
df['change'] = df.groupby('participant_id')['phq9_total'].diff()

# Plot trajectories
for participant in df['participant_id'].unique():
    data = df[df['participant_id'] == participant]
    plt.plot(data['time'], data['phq9_total'], alpha=0.3)

plt.title('Individual PHQ-9 Trajectories')
plt.show()
```

## Data Privacy

### Anonymization
```python
# Remove identifying information
df = df.drop(columns=['name', 'email', 'ip_address'])

# Hash identifiers
import hashlib
df['participant_id'] = df['participant_id'].apply(
    lambda x: hashlib.sha256(x.encode()).hexdigest()
)
```

### Secure Storage
- Store data on encrypted drives
- Use secure cloud storage with proper permissions
- Follow GDPR/HIPAA guidelines
- Keep audit logs

## Best Practices

1. **Document Everything**: Keep a analysis script/logbook
2. **Version Control**: Track analysis code in git
3. **Reproducibility**: Use random seeds, document versions
4. **Quality Control**: Validate data entry, check outliers
5. **Ethics**: Follow IRB guidelines, protect participant privacy

## Resources

- [Pandas Documentation](https://pandas.pydata.org/)
- [Statsmodels](https://www.statsmodels.org/)
- [R for Data Science](https://r4ds.had.co.nz/)

## Next Steps

- [Share findings in a report](../explanation/core-concepts.md)
- [Publish data openly](deploy-protocol.md)
