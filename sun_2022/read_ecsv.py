#!/usr/bin/env python3
"""
Extract a subset of columns from PHANGS 'annulus_0p5kpc' mega-tables
and write one simple, metadata-free CSV per galaxy.

Usage:
    python read_ecsv.py ./data/ECSVs ./data/CSVs
"""

import sys
import glob
import os
from astropy.table import Table

COLUMNS = [
    "r_gal",
    "Zprime",
    "Sigma_mol",
    "e_Sigma_mol",
    "Sigma_atom",
    "e_Sigma_atom",
    "Sigma_star",
    "e_Sigma_star",
    "Sigma_SFR_FUVW4recal",
    "e_Sigma_SFR_FUVW4recal",
]

def main():
    if len(sys.argv) < 3:
        print("Usage: python read_ecsv.py <input_folder> <output_folder>")
        sys.exit(1)

    in_dir  = sys.argv[1]
    out_dir = sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)

    # Match any file as long as "annulus_0p5kpc" is in the name
    pattern = os.path.join(in_dir, "*annulus_0p5kpc*")
    files   = sorted(glob.glob(pattern))

    if not files:
        print(f"No files matching '*annulus_0p5kpc*' found in {in_dir}")
        sys.exit(1)

    for fpath in files:
        fname = os.path.basename(fpath)
        galaxy_name = fname.split("_annulus_0p5kpc")[0]

        t = Table.read(fpath)

        missing = [c for c in COLUMNS if c not in t.colnames]
        if missing:
            print(f"[{galaxy_name}] Warning: missing columns {missing}, skipping those.")

        cols_present = [c for c in COLUMNS if c in t.colnames]
        subset = t[cols_present]

        out_path = os.path.join(out_dir, f"{galaxy_name}.csv")
        subset.write(out_path, format="csv", overwrite=True)
        print(f"Wrote {out_path} ({len(subset)} rows, {len(cols_present)} columns)")


if __name__ == "__main__":
    main()
