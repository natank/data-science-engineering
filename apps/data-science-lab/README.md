# Data Science Lab

A versatile, modular environment for running data science bootcamp exercises and experiments.

## Overview

The Data Science Lab provides a structured framework for executing various data science tasks with:
- **Modular task system** - Each exercise is a separate, reusable module
- **Interactive menu** - Easy task selection and execution
- **Direct execution** - Run specific tasks via command line
- **Output management** - Organized results, plots, and artifacts

## Installation

### Prerequisites
- Python 3.8+ (recommended: Anaconda distribution)
- Node.js and npm (for NX monorepo)

### Setup
```bash
# Install Python dependencies
nx run data-science-lab:install

# Or manually with pip
pip install numpy pandas matplotlib statsmodels
```

## Usage

### Interactive Mode
```bash
# Start the interactive menu
nx run data-science-lab:run

# Or via npm
npm run lab
```

### Direct Task Execution
```bash
# Run a specific task by number
nx run data-science-lab:run 1

# Via npm
npm run lab 1
```

## Available Tasks

| Task | Description | Data Source |
|------|-------------|-------------|
| 1 | Linear Regression (SAT vs GPA) | `docs/1.01.+Simple+linear+regression.csv` |

## Project Structure

```
apps/data-science-lab/
├── src/
│   ├── main.py              # Main orchestrator and menu system
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── linear_regression_task.py
│   └── output/              # Generated plots and results
├── requirements.txt
├── project.json
└── README.md
```

## Adding New Tasks

1. **Create task module** in `src/tasks/`:
```python
# src/tasks/your_task.py
def run():
    """Execute your data science task"""
    print("Running your task...")
    # Your implementation here
    print("✓ Task complete")
```

2. **Register task** in `src/main.py`:
```python
TASKS = {
    '1': {'name': 'Linear Regression', 'module': linear_regression_task},
    '2': {'name': 'Your New Task', 'module': your_task},  # Add this line
}
```

3. **Add requirements** to `requirements.txt` if needed

## Data Sources

- **CSV files**: Place in `docs/` directory
- **Notebooks**: Reference existing Jupyter notebooks in `docs/`
- **Generated outputs**: Automatically saved to `src/output/`

## Development

### Testing a Task
```bash
# Test a specific task directly
/opt/anaconda3/bin/python3 apps/data-science-lab/src/main.py 1
```

### Adding Dependencies
```bash
# Add to requirements.txt
echo "new-package" >> apps/data-science-lab/requirements.txt

# Install
nx run data-science-lab:install
```

## Output

All generated plots, models, and results are saved to:
- `src/output/` - Plots and visualizations
- Console output - Regression results and statistics

## Examples

### Linear Regression Task
```bash
# Run the SAT vs GPA analysis
nx run data-science-lab:run 1

# Output:
# - Regression statistics
# - Scatter plot with regression line
# - Saved plot: src/output/linear_regression.png
```

## Contributing

1. Create new task modules in `src/tasks/`
2. Register in `src/main.py`
3. Add dependencies to `requirements.txt`
4. Test with `nx run data-science-lab:run <task-number>`
5. Commit changes

## Environment

This app is designed to work with the Anaconda Python distribution, which includes all necessary data science packages:
- numpy, pandas, scipy
- matplotlib, seaborn
- scikit-learn, statsmodels

For alternative Python environments, ensure the required packages are installed via `requirements.txt`.
