import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    
    # Create enhanced visualization with seaborn
    plt.figure(figsize=(12, 8))
    
    # Set seaborn style
    sns.set_style("whitegrid")
    sns.set_palette("husl")
    
    # Create scatter plot with regression line using seaborn
    ax = sns.regplot(x=x1, y=y, 
                    scatter_kws={'alpha':0.7, 's':80, 'color': '#2E86AB'},
                    line_kws={'color': '#A23B72', 'linewidth': 3},
                    ci=95)
    
    # Add regression equation
    const, slope = results.params
    r_squared = results.rsquared
    equation_text = f'GPA = {slope:.4f} × SAT + {const:.3f}\nR² = {r_squared:.3f}'
    plt.text(0.05, 0.95, equation_text, transform=ax.transAxes, 
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
             fontsize=12, verticalalignment='top')
    
    # Enhanced styling
    plt.xlabel('SAT Score', fontsize=14, fontweight='bold')
    plt.ylabel('GPA', fontsize=14, fontweight='bold')
    plt.title('SAT vs GPA Linear Regression Analysis', fontsize=16, fontweight='bold', pad=20)
    
    # Customize grid and spines
    ax.grid(True, alpha=0.3)
    sns.despine(top=False, right=False)
    
    plt.tight_layout()
    
    plot_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'linear_regression.png')
    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved to: {plot_path}")
    
    plt.show()
    
    print("\n✓ Linear regression analysis complete")
