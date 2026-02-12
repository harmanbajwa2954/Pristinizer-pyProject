# Pristinizer

**Pristinizer** is a lightweight Python package for automatic data cleaning, exploratory data analysis (EDA), and missing data visualization for pandas DataFrames.

It helps data scientists and ML engineers quickly clean and understand datasets with minimal effort.

---

## Features

- Automatic data cleaning
  - Removes duplicate rows
  - Standardizes column names
  - Handles missing values
  - Removes empty rows and columns

- Dataset summary (EDA)
  - Column data types
  - Missing value counts and percentages
  - Unique value counts

- Missing data visualization
  - Missing value matrix
  - Missing value heatmap
  - Missing value bar chart

- Simple and easy-to-use API

---

## Installation

### From PyPI (recommended)

```bash
pip install pristinizer
```
### From Source

```bash
git clone https://github.com/harmanbajwa2954/Pristinizer-pyProject.git
cd pristinizer
pip install .
```

## Quick Start

```bash
import pandas as pd
import pristinizer as ps

# Load dataset
df = pd.read_csv("data.csv")

# Clean dataset
clean_df = ps.clean(df)

# Generate summary
summary = ps.summarize(df)
print(summary)

# Visualize missing data
ps.missing_matrix(df)
ps.missing_heatmap(df)
ps.missing_bar(df)
```
## Examples
### Input DataSet

| Name | Age | Salary | City   |
| ---- | --- | ------ | ------ |
| A    | 25  | 50000  | Delhi  |
| B    | NaN | 60000  | Mumbai |
| C    | 30  | NaN    | NaN    |

### Output
| column | datatype | missing_count | missing_% | unique_count |
| ------ | -------- | ------------- | --------- | ------------ |
| Age    | float64  | 1             | 33.33     | 2            |
| Salary | float64  | 1             | 33.33     | 2            |
| City   | object   | 1             | 33.33     | 2            |
| Name   | object   | 0             | 0.00      | 3            |


## Available Functions

### Data Cleaning
```bash
ps.clean(df)
```
Returns cleaned DataFrame.

### Dataset Summary
```bash
ps.summarize(df)
```
Returns summary DataFrame containing:

* column name
* datatype
* missing count
* missing percentage
* unique count

### Missing Data Visualization

Matrix view:
```bash
ps.missing_matrix(df)
```

Heatmap view:
```bash
ps.missing_heatmap(df)
```

Bar chart view:
```bash
ps.missing_bar(df)
```

## Project Structure

pristinizer/  
│  
├── pristinizer/  
│...... ├── init.py  
│ ......├── cleaner.py  
│.......├── eda.py  
│...... ├── visualizer.py  
│  
├── README.md  
├── pyproject.toml  
├── LICENSE



---

## Requirements

- Python ≥ 3.8
- pandas
- matplotlib
- seaborn

---

## Use Cases

- Machine learning preprocessing
- Exploratory data analysis
- Data science projects
- Data cleaning automation
- Educational purposes

---

## Future Features

- Outlier detection
- Automatic datatype conversion
- Feature importance analysis
- Full EDA reports
- Integration with ML pipelines

---

## Contributing

Contributions are welcome.

### Steps:

1. Fork the repository  
2. Create a new branch  
3. Make changes  
4. Submit a pull request  

---

## License

MIT License

---

## Author

Created as a data science utility package to simplify preprocessing workflows.  
By – Harmanpreet Singh

---

## Support

If you find this useful, consider starring the repository on GitHub.
