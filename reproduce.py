#!/usr/bin/env python3
"""Reproduce the final coverage-aware tracking table (Table 6) from the bundled
per-frame result CSVs. Requires numpy and scipy (see requirements.txt)."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(HERE, "code", "build_final_tracking_table.py")

print("Reproducing Table 6 (coverage-aware IoU) from bundled results ...")
subprocess.check_call([sys.executable, script])
print("\nDone. Compare with docs/reproduce_output.txt and docs/tracking_table.tex.")
