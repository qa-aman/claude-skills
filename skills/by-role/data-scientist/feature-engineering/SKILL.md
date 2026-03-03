---
name: feature-engineering
description: >
  Design and implement features from raw data for machine learning models. Use when the user says
  "engineer features", "feature engineering for X", "create features from this dataset", "transform
  these variables", "encode categoricals", "handle skew", "create interaction features", "lag features",
  "extract features from text or dates", "improve model performance with better features", or wants
  to move from raw columns to model-ready inputs.
---

## Overview

Based on **"Feature Engineering for Machine Learning"** by Alice Zheng and Amanda Casari. The core principle: features are the interface between raw data and model performance. The right transformation of an existing variable outperforms adding more data or tuning hyperparameters in most real-world settings. Feature engineering is domain knowledge encoded into math - and it is the highest-leverage step in the ML pipeline.

## Workflow

### Step 1: Audit raw columns for engineering opportunity

Before transforming anything, catalog what you have and what problems each column has.

For each column, note:
- Type: numeric continuous, numeric discrete, ordinal categorical, nominal categorical, datetime, text, ID
- Problem: skewed, high cardinality, missing, mixed type, free text, leaky (contains target signal from the future)
- Engineering opportunity: log transform, binning, encoding, extraction, embedding

Create a feature engineering plan as a table before writing any code:

```
| Column      | Type       | Problem          | Planned Transform         |
|-------------|-----------|------------------|---------------------------|
| revenue     | numeric    | Right-skewed     | log1p transform           |
| country     | nominal    | 150 unique vals  | Frequency encoding        |
| signup_date | datetime   | Raw timestamp    | Extract day-of-week, hour |
| description | text       | Unstructured     | TF-IDF, 500 features      |
```

### Step 2: Apply numeric transformations

**Skewed distributions:** Apply log transform to right-skewed variables. Use `np.log1p` to handle zeros.

```python
df["log_revenue"] = np.log1p(df["revenue"])
```

**Scaling:** Standardize for distance-based models (KNN, SVM, neural nets). Tree-based models (XGBoost, Random Forest) do not require scaling.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df["revenue_scaled"] = scaler.fit_transform(df[["revenue"]])
```

**Binning:** Convert continuous to ordinal when the relationship to the target is non-linear.

```python
df["age_bin"] = pd.cut(df["age"], bins=[0, 18, 35, 55, 100], labels=["<18", "18-35", "35-55", "55+"])
```

**Capping outliers:** Cap at a percentile rather than removing rows.

```python
p99 = df["session_time"].quantile(0.99)
df["session_time_capped"] = df["session_time"].clip(upper=p99)
```

### Step 3: Encode categorical variables

Match the encoding method to the cardinality and the model type.

| Cardinality | Model Type | Method |
|---|---|---|
| Low (< 10) | Any | One-hot encoding |
| Medium (10-50) | Tree-based | Ordinal / Label encoding |
| High (> 50) | Any | Frequency or target encoding |
| High (> 50) | Neural net | Embedding layer |

```python
# One-hot
df = pd.get_dummies(df, columns=["color"], drop_first=True)

# Frequency encoding
freq = df["country"].value_counts() / len(df)
df["country_freq"] = df["country"].map(freq)

# Target encoding (use cross-validation to avoid leakage)
from category_encoders import TargetEncoder
encoder = TargetEncoder(cols=["city"])
df["city_encoded"] = encoder.fit_transform(df["city"], df["target"])
```

### Step 4: Extract features from dates and text

**Datetime columns:** Raw timestamps carry no signal. Extract structured components.

```python
df["signup_hour"] = df["signup_ts"].dt.hour
df["signup_dow"] = df["signup_ts"].dt.dayofweek    # 0=Mon, 6=Sun
df["signup_is_weekend"] = df["signup_dow"].isin([5, 6]).astype(int)
df["days_since_signup"] = (pd.Timestamp.now() - df["signup_ts"]).dt.days
```

**Text columns:** Start with TF-IDF for structured text. Move to embeddings when semantic meaning matters.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=200, ngram_range=(1, 2), stop_words="english")
text_features = tfidf.fit_transform(df["description"])
```

### Step 5: Create interaction and aggregate features

Zheng and Casari's insight: the most predictive features are often combinations of existing ones, not raw columns.

**Interaction features:** Multiply or divide two numeric columns when their ratio or product has domain meaning.

```python
df["revenue_per_session"] = df["revenue"] / (df["session_count"] + 1)
df["cost_per_click"] = df["spend"] / (df["clicks"] + 1)  # +1 avoids division by zero
```

**Aggregate features (group-level statistics):** Capture behavior relative to a group.

```python
group_stats = df.groupby("user_id")["purchase_amount"].agg(["mean", "std", "count"]).reset_index()
group_stats.columns = ["user_id", "user_avg_purchase", "user_std_purchase", "user_purchase_count"]
df = df.merge(group_stats, on="user_id", how="left")
```

**Lag features for time series:**

```python
df = df.sort_values(["user_id", "date"])
df["revenue_lag_7d"] = df.groupby("user_id")["revenue"].shift(7)
df["revenue_rolling_30d"] = df.groupby("user_id")["revenue"].transform(lambda x: x.rolling(30).mean())
```

### Step 6: Validate features and check for leakage

Before training, run these checks:

1. **Leakage check:** Can any feature be computed from the target or from future data? Flag and remove.
2. **Correlation check:** Drop features with correlation > 0.95 to another feature.
3. **Importance check:** Train a simple Random Forest and check feature importances. Drop zero-importance features.
4. **Missing rate check:** Any feature > 30% missing should be dropped or imputed before inclusion.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

importance = pd.Series(model.feature_importances_, index=X_train.columns).sort_values(ascending=False)
print(importance.head(20))
```

Document the final feature set with a name, source column(s), transform applied, and rationale.

## Anti-Patterns

**1. One-hot encoding high-cardinality categoricals**
Bad: One-hot encoding a "city" column with 500 unique values - creates 500 sparse binary columns.
Good: Use frequency encoding or target encoding. Reserve one-hot for columns with fewer than 10 unique values.

**2. Using the full dataset to fit encoders**
Bad: Fitting a TF-IDF or TargetEncoder on the entire dataset before splitting into train/test.
Good: Fit only on training data. Apply (transform) to test data. This prevents leakage from test labels.

**3. Adding features without checking importance**
Bad: Engineering 50 new features and feeding all of them to the model.
Good: Run a quick feature importance check. Remove zero-importance features before final training.

**4. Ignoring domain knowledge**
Bad: Letting the model figure out that revenue/sessions is meaningful by including both raw columns.
Good: Create the ratio feature explicitly. Domain-derived features outperform raw features in most tabular settings.

## Quality Checklist

- [ ] Feature engineering plan documented as a table before any code is written
- [ ] Skewed numeric columns log-transformed or capped
- [ ] Categorical encoding method matched to cardinality and model type
- [ ] Datetime columns decomposed into structured components (hour, day-of-week, recency)
- [ ] Interaction and aggregate features created for high-signal relationships
- [ ] All encoders fitted on training data only - no test data leakage
- [ ] Feature importance check run and zero-importance features removed
- [ ] Final feature set documented with source, transform, and rationale
