import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os

def load_data():
    """Load the SAT-GPA dataset"""
    csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs', '1.01.+Simple+linear+regression.csv')
    return pd.read_csv(csv_path)

def analyze_regression(data):
    """Perform linear regression analysis"""
    # Define variables
    y = data['GPA']
    x1 = data['SAT']
    
    # Add constant and fit model
    x = sm.add_constant(x1)
    results = sm.OLS(y, x).fit()
    
    return results, x1, y

def plot_results(x1, y, results):
    """Create scatter plot with regression line"""
    plt.figure(figsize=(10, 6))
    
    # Scatter plot
    plt.scatter(x1, y, alpha=0.6, label='Data points')
    
    # Regression line
    const, slope = results.params
    yhat = slope * x1 + const
    plt.plot(x1, yhat, 'r-', lw=3, label=f'Regression line: GPA = {slope:.4f} × SAT + {const:.3f}')
    
    plt.xlabel('SAT Score', fontsize=14)
    plt.ylabel('GPA', fontsize=14)
    plt.title('SAT vs GPA Linear Regression', fontsize=16)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(os.path.dirname(__file__), 'regression_plot.png')
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {plot_path}")
    
    plt.show()

def main():
    """Main execution function"""
    print("=" * 60)
    print("Linear Regression Analysis: SAT vs GPA")
    print("=" * 60)
    
    # Load data
    data = load_data()
    print(f"Dataset loaded: {len(data)} observations")
    print("\nData preview:")
    print(data.head())
    print("\nData statistics:")
    print(data.describe())
    
    # Perform regression
    print("\n" + "=" * 60)
    print("Regression Results")
    print("=" * 60)
    
    results, x1, y = analyze_regression(data)
    print(results.summary())
    
    # Plot results
    print("\nGenerating visualization...")
    plot_results(x1, y, results)
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
