#!/usr/bin/env python3
"""Extract inline 'run:' script blocks from composite action YAML files.

Outputs each block as a standalone .sh file for ShellCheck analysis.

Usage:
    python3 scripts/extract-inline-scripts.py <action_file> <output_dir>
"""

import os
import sys

import yaml


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <action_file> <output_dir>", file=sys.stderr)
        sys.exit(1)

    action_file = sys.argv[1]
    output_dir = sys.argv[2]

    with open(action_file) as f:
        data = yaml.safe_load(f)

    steps = data.get("runs", {}).get("steps", [])
    for i, step in enumerate(steps):
        if "run" in step:
            name = os.path.basename(os.path.dirname(action_file))
            out = os.path.join(output_dir, f"{name}_{i}.sh")
            with open(out, "w") as o:
                o.write("#!/usr/bin/env bash\n")
                o.write(step["run"])


if __name__ == "__main__":
    main()
