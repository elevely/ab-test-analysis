# A/B Test Analysis: Banking Onboarding

## Overview

This project analyzes an A/B experiment conducted to evaluate whether a new onboarding flow improves the registration conversion rate of a banking application.

Users were randomly assigned to either:

- **Control** — existing onboarding flow
- **Treatment** — new onboarding flow

The main goal is to determine whether the observed difference in conversion is statistically significant and whether the new onboarding should be rolled out to all users.

---

## Business Problem

The product team introduced a redesigned onboarding flow aimed at improving the registration experience and increasing the number of users who successfully complete registration.

The key business question is:

> **Does the new onboarding flow increase registration conversion compared with the existing flow?**

The analysis is designed to support a product decision based on both statistical evidence and practical business impact.

---

## Experiment Design

The experiment contains **100,000 users** who started the registration process.

Users were randomly assigned to two groups:

| Group | Description |
|---|---|
| Control | Existing onboarding flow |
| Treatment | New onboarding flow |

The expected allocation ratio was **50/50**.

### Hypotheses

**Null hypothesis (H₀):**

There is no difference in registration conversion between the Control and Treatment groups.

$$
H_0: p_{control} = p_{treatment}
$$

**Alternative hypothesis (H₁):**

Registration conversion differs between the two groups.

$$
H_1: p_{control} \neq p_{treatment}
$$

The significance level was set to:

$$
\alpha = 0.05
$$

---

## Dataset

The dataset is synthetic and was generated specifically for this project to simulate a realistic banking A/B experiment.

It contains the following fields:

| Column | Description |
|---|---|
| `user_id` | Unique user identifier |
| `group` | Experiment group: control or treatment |
| `registration_started` | Whether the user started registration |
| `registration_completed` | Whether the user successfully completed registration |
| `device` | User device: iOS, Android, or Web |
| `source` | User acquisition source |
| `experiment_date` | Date of experiment exposure |

The dataset contains **100,000 observations** and does not include missing values or duplicate users.

---

## Primary Metric

The primary metric is **Registration Conversion Rate**:

$$
Conversion\ Rate =
\frac{Successful\ Registrations}
{Registration\ Starts}
$$

The metric is calculated separately for the Control and Treatment groups.

---

## Methodology

The analysis includes:

1. Data quality validation
2. Exploratory data analysis
3. Experiment group balance checks
4. Registration conversion calculation
5. Absolute and relative uplift calculation
6. Two-proportion z-test
7. P-value evaluation
8. 95% confidence interval estimation
9. Sample Ratio Mismatch (SRM) check
10. Segment-level analysis
11. Business impact estimation
12. Final product recommendation

---

## Data Quality Check

The dataset was checked for:

- Duplicate `user_id` values
- Missing values
- Invalid experiment groups
- Invalid device and source values
- Invalid binary values
- Logically inconsistent registration states
- Incorrect date formats

All data quality checks passed successfully.

---

## Results

### Conversion Rate

| Metric | Control | Treatment |
|---|---:|---:|
| Conversion Rate | 8.29% | 8.89% |

The Treatment group achieved a higher registration conversion than the Control group.

### Effect Size

**Absolute uplift:**

**+0.60 percentage points**

**Relative uplift:**

**+7.23%**

### Statistical Significance

A two-proportion z-test was used to determine whether the observed difference could be explained by random variation.

- **Z-statistic:** -3.3811
- **P-value:** 0.000722
- **Significance level:** 0.05

Since:

$$
p < 0.05
$$

the null hypothesis is rejected.

The observed difference in conversion rates is statistically significant.

### Confidence Interval

The 95% confidence interval for the difference in conversion rates (Treatment − Control) is:

**[+0.25 p.p.; +0.95 p.p.]**

The interval does not include zero, which is consistent with the statistical significance test.

---

## Sample Ratio Mismatch

The observed experiment allocation was approximately 50/50 between Control and Treatment.

A chi-square goodness-of-fit test was used to check for Sample Ratio Mismatch (SRM).

**Result: No significant Sample Ratio Mismatch was detected.**

This provides no evidence of a problem with the expected experiment group allocation.

---

## Segment Analysis

The Treatment group showed higher conversion across the analyzed device segments:

| Device | Control | Treatment |
|---|---:|---:|
| Android | 7.98% | 8.51% |
| iOS | 9.43% | 10.16% |
| Web | 6.72% | 7.27% |

The Treatment group also showed higher conversion across all analyzed acquisition sources.

This suggests that the overall result is not driven by a single device or acquisition segment.

---

## Business Impact

To translate the experimental effect into business terms, consider a scenario where **1,000,000 users start registration per month**.

The observed conversion uplift of approximately **0.60 percentage points** corresponds to:

**~5,993 additional successful registrations per month.**

Based on the 95% confidence interval, the estimated incremental registrations could range from approximately:

**2,519 to 9,467 additional registrations per month.**

---

## Final Decision

### Recommendation: Roll Out

The new onboarding flow increased registration conversion from **8.29% to 8.89%**.

The estimated improvement is:

- **+0.60 p.p. absolute uplift**
- **+7.23% relative uplift**
- **p-value = 0.000722**
- **95% CI = [+0.25 p.p.; +0.95 p.p.]**

The result is statistically significant and has a meaningful potential business impact.

**Recommendation: roll out the new onboarding flow to all users.**

---

## Project Structure

```text
ab-test-analysis/
│
├── data/
│   └── ab_test_data.csv
│
├── notebooks/
│   └── 01_ab_test_analysis.ipynb
│
├── README.md
├── requirements.txt
└── generate_data.py
```

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels
- Jupyter Notebook

---

## Notebook

The complete analysis is available in the Jupyter Notebook:

[01_ab_test_analysis.ipynb](notebooks/01_ab_test_analysis.ipynb)

---

## How to Run

Clone the repository:

```bash
git clone <repository-url>
cd ab-test-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```bash
notebooks/01_ab_test_analysis.ipynb
```

---

## Key Takeaways

This project demonstrates practical Product Analytics skills:

- Designing and analyzing an A/B experiment
- Defining a product metric
- Performing data quality checks
- Comparing conversion rates
- Testing statistical significance
- Interpreting p-values and confidence intervals
- Distinguishing statistical from practical significance
- Evaluating experiment allocation with SRM
- Analyzing results across user segments
- Translating experiment results into business impact
- Making a product rollout recommendation based on experimental evidence