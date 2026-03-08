import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os

def run():
    """Execute linear regression analysis on SAT-GPA data"""
    print("\n" + "=" * 60)
    print("Task: Linear Regression Analysis (SAT vs GPA)")
    print("=" * 60)
    
    # Load data
    csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'docs', '1.01.+Simple+linear+regression.csv')
    data = pd.read_csv(csv_path)
    print(f"Dataset loaded: {len(data)} observations")
    
    # Define variables
    y = data['GPA']
    x1 = data['SAT']
    
    # Perform regression
    x = sm.add_constant(x1)
    results = sm.OLS(y, x).fit()
    
    print("\nRegression Results:")
    print(results.summary())
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.scatter(x1, y, alpha=0.6, label='Data points')
    
    const, slope = results.params
    yhat = slope * x1 + const
    plt.plot(x1, yhat, 'r-', lw=3, label=f'Regression: GPA = {slope:.4f} × SAT + {const:.3f}')
    
    plt.xlabel('SAT Score', fontsize=14)
    plt.ylabel('GPA', fontsize=14)
    plt.title('SAT vs GPA Linear Regression', fontsize=16)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plot_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'linear_regression.png')
    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved to: {plot_path}")
    
    plt.show()
    
    print("\n✓ Linear regression analysis complete")
