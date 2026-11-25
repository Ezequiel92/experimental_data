# PHANGS multiwavelength data tables v4.0

---

**Reference**:
+ Sun, Leroy, Rosolowsky, et al., 2022, "Molecular Cloud Populations in the Context of Their Host Galaxy Environments: A Multiwavelength Perspective", AJ, 164, 43
+ Sun, Leroy, Ostriker, et al., 2023, "Star Formation Laws and Efficiencies across 80 Nearby Galaxies", ApJL, 945, L19

**Contact**: [Jiayi Sun](mailto:sun208@mcmaster.ca)

---

## Overview

This is the v4.0 public release of the PHANGS rich multiwavelength data tables (a.k.a. "mega-tables"). The table content and construction schemes are detailed in Sun et al. (2022), whereas the improvements over the previous release (v3.0) are summarized in Appendix B of Sun et al. (2023).

This release includes data tables for 80 PHANGS-ALMA galaxies. For each galaxy, we provide three data tables:
+ `[GALAXYNAME]_annulus_0p5kpc.ecsv` includes (region-averaged) measurements in 500 pc-wide radial bins.
+ `[GALAXYNAME]_hexagon_1p5kpc.ecsv` includes (region-averaged) measurements in 1.5 kpc-sized hexagonal apertures.
+ `[GALAXYNAME]_gauss_1p5kpc.ecsv` includes (kernel-averaged) measurements over 1.5 kpc-sized Gaussian beams.
Other than their different sampling patterns, these tables include a very similar set of measured quantities. 

---

## Basic data accessing tutorial

In each table, each column corresponds to a measured quantity, whereas each row is an independent measurement inside a particular aperture or radial bin. One can easily extract a subset of measurements from the table with the I/O tools offered by the `astropy.table` module in Python:
```
from astropy.table import Table

# read in the table
t = Table.read('PATH_TO_TABLE')

# print the content of some specific columns
print(t['Sigma_mol', 'Sigma_atom', 'Sigma_star'])

# print the content of the first ten rows
print(t[:10])
```
The table header records the names, physical units, and descriptions of the quantities in all columns (also see Appendix F in the paper). These information can be accessed with the same `astropy.table` I/O tool as follows:
```
print(t.info)
```
The table header also carries additional information in its metadata area, such as the WCS coordinates, orientation parameters, and global properties of each galaxy. These information can be accessed as follows:
```
print(t.meta)
```