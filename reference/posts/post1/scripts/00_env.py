"""Step 00: check the environment.
What this does: imports each package we will use and prints its version, then prints
where Python is running from. If anything is missing it stops with a clear message.
Why: every later script assumes these exist; we want to know now, not on day 3."""
import sys, importlib

REQUIRED = ["pandas", "numpy", "statsmodels", "scipy", "matplotlib"]

print("Python", sys.version.split()[0], "at", sys.executable)
missing = []
for name in REQUIRED:
    try:
        mod = importlib.import_module(name)
        print(f"  {name:12s} {mod.__version__}")
    except ImportError:
        missing.append(name)

# ---- check block: the script must not end quietly if something is wrong
assert not missing, f"Missing packages: {missing}. Run: pip install {' '.join(missing)}"
assert sys.version_info >= (3, 9), "Python 3.9 or newer is needed"
print("CHECK OK: environment ready")
