"""
Data Science Lab - Main Orchestrator

This app serves as a flexible environment for running various data science tasks
from the bootcamp. Each task is a separate module that can be executed independently.
"""

import sys
from tasks import linear_regression_task

# Task registry
TASKS = {
    '1': {
        'name': 'Linear Regression (SAT vs GPA)',
        'module': linear_regression_task
    },
}

def display_menu():
    """Display available tasks"""
    print("\n" + "=" * 60)
    print("Data Science Lab - Task Menu")
    print("=" * 60)
    for key, task in TASKS.items():
        print(f"  [{key}] {task['name']}")
    print("  [0] Exit")
    print("=" * 60)

def run_task(task_key):
    """Execute a specific task"""
    if task_key == '0':
        print("\nExiting Data Science Lab. Goodbye!")
        return False
    
    if task_key not in TASKS:
        print(f"\n❌ Invalid task: {task_key}")
        return True
    
    task = TASKS[task_key]
    try:
        task['module'].run()
    except Exception as e:
        print(f"\n❌ Error running task: {e}")
        import traceback
        traceback.print_exc()
    
    return True

def main():
    """Main orchestrator - interactive mode or direct task execution"""
    print("=" * 60)
    print("Welcome to Data Science Lab")
    print("=" * 60)
    
    # Check if task specified via command line
    if len(sys.argv) > 1:
        task_key = sys.argv[1]
        print(f"\nRunning task: {TASKS.get(task_key, {}).get('name', 'Unknown')}")
        run_task(task_key)
        return
    
    # Interactive mode
    while True:
        display_menu()
        choice = input("\nSelect a task (or 0 to exit): ").strip()
        
        if not run_task(choice):
            break

if __name__ == "__main__":
    main()
