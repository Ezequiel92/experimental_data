J/A+A/666/A186     MZ-SFR in SDSS star-forming galaxies  (Duarte Puertas+, 2022)
================================================================================
Mass-metallicity and star formation rate in galaxies:
A complex relation tuned to stellar age.
    Duarte Puertas S., Vilchez J.M., Iglesias-Paramo J., Molla M.,
    Perez-Montero E., Kehrig C., Pilyugin L.S., Zinchenko I.A.
    <Astron. Astrophys. 666, A186 (2022)>
    =2022A&A...666A.186D        (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Galaxy catalogs ; Redshifts ; Abundances ; Stars, masses ; Optical
Keywords: galaxies: general - galaxies: star forming - galaxies: abundances -
          galaxies: evolution

Abstract:
    In this work we study the stellar mass -- metallicity relation (MZR)
    of an extended sample of star-forming galaxies in the local Universe
    and its possible dependence with the star formation rate (SFR).

    A sample of ~195000 Sloan Digital Sky Survey (SDSS) star-forming
    galaxies has been selected up to z=0.22 with the aim of analysing the
    behaviour of the relation of MZR with respect to SFR and taking into
    account the age of their stellar populations.

    For this sample we have obtained, for the first time, aperture
    corrected oxygen and nitrogen-to-oxygen abundances (O/H and N/O,
    respectively) and SFR using the empirical prescriptions from the Calar
    Alto Legacy Integral Field Area (CALIFA) survey. To perform this study
    we make use also of the stellar mass of the galaxies and the parameter
    Dn(4000) as a proxy of the age of the stellar population.

    We derive a robust MZR locus, which is found to be fully consistent
    with the "anchoring" points of a selected set of well studied nearby
    galaxies with a direct derivation of the chemical abundance. A complex
    relation between MZR and SFR across the whole range of galaxy mass and
    metallicity has been observed, where the slope changes seen in the O/H
    -- SFR plane present a pattern which seems to be tuned to the
    galaxies' stellar age, and therefore, stellar age has to be taken into
    account in the stellar mass -- metallicity -- SFR relation.

    In order to provide an answer to the question of whether or not the
    MZR depends on the SFR it is essential to take into account the age of
    the stellar populations of galaxies. A strong dependence between the
    MZR and SFR is observed mainly for star-forming galaxies with strong
    SFR values and low Dn(4000). The youngest galaxies of our SDSS sample
    show the highest SFR measured for their stellar mass.

Description:
    Our study is based on the MPA-JHU public catalogue (Kauffmann et al..
    2003MNRAS.341...33K; Brinchmann et al., 2004MNRAS.351.1151B; Tremonti
    et al., 2004ApJ...613..898T; Salim et al., 2007ApJS..173..267S), which
    gives spectroscopic data of the galaxies in the Sloan Digital Sky
    Survey Data Release 7 (SDSS-DR7) (Abazajian et al.,
    2009ApJS..182..543A). The SDSS spectroscopic primary sample of
    galaxies is complete in Petrosian r magnitude in the range
    14.5<=r<=17.7 (Strauss et al., 2002AJ....124.1810S; Brinchmann et
    al. ArXiv e-prints [arXiv:astro-ph/0406220]). We added the photometric
    data from the SDSS-DR12 (York et al., 2000AJ....120.1579Y; Alam et
    al., 2015ApJS..219...12A, Cat. V/147) to the MPA-JHU catalogue.

    We selected a subset of 194353 star-forming galaxies. For these
    star-forming galaxies we derived aperture-corrected oxygen and
    nitrogen-to-oxygen abundances using the empirical aperture corrections
    of Iglesias-Paramo et al. (2016ApJ...826...71I, Cat. J/ApJ/826/71) and
    the calibrators of Pilyugin & Grebel (2016MNRAS.457.3678P).

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe            80        .   This file
table1.dat       126   194353   Catalogue of 194353 SDSS star-forming galaxies
                                 empirically corrected for aperture using
                                 Iglesias-Paramo et al. (2016ApJ...826...71I):
                                 oxygen and nitrogen-to-oxygen abundance and
                                 related relevant data
--------------------------------------------------------------------------------

See also:
 J/A+A/599/A71 : 209276 SDSS star-forming galaxies aperture-free (Duarte+, 2017)

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units      Label     Explanations
--------------------------------------------------------------------------------
   1- 19  I19   ---        specObjID SDSS-DR12 unique spectrum identification
  21- 28  F8.4  deg        RAdeg     Right Ascension (J2000) from SDSS
  30- 37  F8.4  deg        DEdeg     Declination (J2000) from SDSS
  39- 44  F6.4  ---        z         Spectroscopic redshift
  46- 52  F7.4  ---        logOH     12+log(O/H) corrected for aperture
                                      effects (1)
  54- 59  F6.4  ---      e_logOH     Uncertainty of 12+log(O/H) corrected for
                                      aperture effects (1)
  61- 67  F7.4  ---        logNO     Log of nitrogen-to-oxygen abundance ratio
                                      corrected for aperture effects (1)
  69- 74  F6.4  ---      e_logNO     Uncertainty of Log of nitrogen-to-oxygen
                                      abundance ratio corrected for aperture
                                      effects (1)
  76- 82  F7.4 [Msun/yr]   logSFR    Log of total star formation rate corrected
                                      for aperture effects (2)
  84- 89  F6.4 [Msun/yr] e_logSFR    Uncertainty of Log of total star formation
                                      rate corrected for aperture effects
  91- 97  F7.4  ---        Dn4000    Dn(4000) parameter (3)
  99-104  F6.4  ---      e_Dn4000    Uncertainty of Dn(4000) parameter (3)
 106-112  F7.4  [Msun]     logMass   Log of total stellar mass (3)
 114-119  F6.4  [Msun]   E_logMass   Uncertainty of Log of total stellar mass,
                                      upper limit at the 1 sigma level (3)
 121-126  F6.4  [Msun]   e_logMass   Uncertainty of Log of total stellar mass,
                                      lower limit at the 1 sigma level (3)
--------------------------------------------------------------------------------
Note (1): Derived using Pilyugin & Grebel (2016MNRAS.457.3678P) equations as:
    - For 12+log(O/H): R calibrator, equations 4 and 5
    - For log(N/O): equation 13
Note (2): Taken from Duarte Puertas et al.
    (2017A&A...599A..71D, Cat. J/A+A/599/A71).
Note (3): Taken from Max-Planck-Institut fuer Astrophysik and Johns Hopkins
    University (MPA-JHU) public catalogue Kauffmann et al., 2003MNRAS.341...33K;
    Brinchmann et al., 2004MNRAS.351.1151B; Tremonti et al.,
    2004ApJ...613..898T; Salim et al., 2007ApJS..173..267S
    - E_logmass derived as: 84th percentile - median
    - e_logmass derived as: median - 16th percentile
--------------------------------------------------------------------------------

Acknowledgements:
    Salvador Duarte Puertas, salvador-manuel.duarte-puertas.1(at)ulaval.ca

================================================================================
(End)                                        Patricia Vannier [CDS]  10-Oct-2022
