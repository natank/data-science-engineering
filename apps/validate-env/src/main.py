import sys

packages = [
    ("numpy", "np"),
    ("pandas", "pd"),
    ("scipy", None),
    ("statsmodels.api", "sm"),
    ("matplotlib", "plt"),
    ("seaborn", "sns"),
    ("sklearn", None),
]

print("=" * 50)
print("Data Science Environment Validation")
print("=" * 50)

all_ok = True
for module, alias in packages:
    try:
        mod = __import__(module)
        version = getattr(mod, "__version__", "unknown")
        print(f"  [OK] {module} ({version})")
    except ImportError as e:
        print(f"  [MISSING] {module} - {e}")
        all_ok = False

print("=" * 50)
if all_ok:
    print("All required packages are installed. Ready to go!")
else:
    print("Some packages are missing. Run: pip install -r requirements.txt")
    sys.exit(1)
