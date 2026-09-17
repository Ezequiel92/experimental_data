J/ApJ/701/1965   Radial dust properties of SINGS galaxies  (Munoz-Mateos+, 2009)
================================================================================
Radial distribution of stars, gas, and dust in SINGS galaxies.
II. Derived dust properties.
    Munoz-Mateos J.C., Gil de Paz A., Boissier S., Zamorano J., Dale D.A.,
    Perez-Gonzalez P.G., Gallego J., Madore B.F., Bendo G., Thornley M.D.,
    Draine B.T., Boselli A., Buat V., Calzetti D., Moustakas J., Kennicutt R.C.
   <Astrophys. J., 701, 1965-1991 (2009)>
   =2009ApJ...701.1965M
================================================================================
ADC_Keywords: Galaxies, nearby ; Photometry, surface ; Ultraviolet ;
              Infrared sources ; Interstellar medium ; Extinction
Keywords: dust, extinction - galaxies: ISM - infrared: galaxies -
          ultraviolet: galaxies

Abstract:
    We present a detailed analysis of the radial distribution of dust
    properties in the SINGS sample, performed on a set of ultraviolet
    (UV), infrared (IR), and HI surface brightness profiles, combined with
    published molecular gas profiles and metallicity gradients. By
    applying physical dust models to our radial spectral energy
    distributions, we have derived radial profiles of the total dust mass
    surface density, the fraction of the total dust mass contributed by
    polycyclic aromatic hydrocarbons (PAHs), and the intensity of the
    radiation field heating the grains.

Description:
    The SINGS sample (Kennicutt et al. 2003PASP..115..928K) consists of 75
    nearby galaxies. Eighteen SINGS galaxies were not suitable for our
    purposes and were excluded from the present study. Nearly all SINGS
    galaxies have been observed in the far-UV (FUV; {lambda}_eff_=151.6nm)
    and near-UV (NUV; {lambda}_eff_=226.7nm) by GALEX (see Table 1). The
    reader is referred to Paper I (2009, Cat. J/ApJ/703/1569) for a more
    detailed description of the Spitzer data used here. Mid- and far-IR
    observations of the SINGS sample were carried out using the Spitzer
    Space Telescope (IRAC and MIPS). The HI Nearby Galaxy Survey (THINGS;
    Walter et al. 2008, Cat. J/AJ/136/2563) used the Very Large Array
    (VLA) to map HI 21cm line emission from 34 nearby (D<15Mpc) galaxies,
    most of which were also targets of SINGS and the GALEX Nearby Galaxies
    Survey.

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe         80        .   This file
table1.dat     78       57   Sample
table2.dat    120      520   Degraded GALEX, IRAC and MIPS profiles
table3.dat    103      479   Extinction profiles
table4.dat    148      379   Model parameters profiles
--------------------------------------------------------------------------------

See also:
 VII/155 : Third Reference Cat. of Bright Galaxies (RC3) (de Vaucouleurs+ 1991)
 J/ApJS/190/233 : Spectroscopy and abundances of SINGS galaxies (Moustakas+,
                  2010)
 J/ApJ/703/1569 : Radial distribution in SINGS galaxies. I (Munoz-Mateos+, 2009)
 J/AJ/136/2563  : HI Nearby Galaxy Survey, THINGS (Walter+, 2008)
 J/ApJS/173/185 : GALEX ultraviolet atlas of nearby galaxies (Gil de Paz+, 2007)
 J/ApJ/669/959  : Warm molecular hydrogen in SINGS galaxies (Roussel+, 2007)
 J/AJ/108/2128  : RC3 corrections and additions (Corwin+ 1994)

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label   Explanations
--------------------------------------------------------------------------------
   1- 11  A11   ---     Name    Galaxy name
      12  A1    ---   f_Name    [*] Flag for NGC 5194 (1)
  14- 15  I2    h       RAh     Galaxy center hour of right ascension (J2000)
  17- 18  I2    min     RAm     Galaxy center minute of right ascension (J2000)
  20- 23  F4.1  s       RAs     Galaxy center second of right ascension (J2000)
      25  A1    ---     DE-     Galaxy center sign of declination (J2000)
  26- 27  I2    deg     DEd     Galaxy center degree of declination (J2000)
  29- 30  I2    arcmin  DEm     Galaxy center arcminute of declination (J2000)
  32- 35  F4.1  arcsec  DEs     Galaxy center arcsecond of declination (J2000)
  37- 40  F4.1  arcmin  2a      Apparent major isophotal diameter (2)
  42- 45  F4.1  arcmin  2b      Apparent minor isophotal diameter (2)
  47- 49  I3    deg     PA      [0,360] Position angle from the RC3 catalog
  51- 55  F5.3  mag     E(B-V)  Galactic color excess from Schlegel et al.
                                (1998ApJ...500..525S)
  57- 60  F4.1  ---     TType   Morphological type T from RC3 catalog (VII/155)
  62- 66  F5.2  Mpc     Dist    Distance to the galaxy (3)
  68- 70  A3    ---     GALEX   Available GALEX images (Yes or NUV)
  72- 74  A3    ---     THINGS  Available HI maps from THINGS (Yes or No)
  76- 78  A3    ---   r_CO      [1-7, ] References for the CO data (4)
--------------------------------------------------------------------------------
Note (1): The PA and axis ratio for NGC 5194 differ from those in the RC3,
          which are affected by the presence of NGC 5195.
Note (2): Apparent major and minor isophotal diameters at
          {mu}_B_=25mag/arcsec^2^ from the RC3 catalog.
Note (3): Distance to the galaxy, rounded to the nearest Mpc when larger than
          10Mpc, taken from Gil de Paz et al. (2007, Cat. J/ApJS/173/185) and
          Kennicutt et al. (2003PASP..115..928K).
Note (4): References for the CO data as follows:
    1 = Regan et al. 2001ApJ...561..218R;
    2 = Sage 1993A&A...272..123S;
    3 = Young et al. 1995ApJS...98..219Y;
    4 = Bajaja et al. 1995A&AS..114..147B;
    5 = Young & Scoville 1982ApJ...260L..41Y;
    6 = Kenney & Young 1988ApJS...66..261K;
    7 = Paglione et al. 2001ApJS..135..183P
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table2.dat
--------------------------------------------------------------------------------
   Bytes Format Units        Label  Explanations
--------------------------------------------------------------------------------
   1- 11  A11   ---          Name   Galaxy name
  13- 16  I4    arcsec       Arad   Angular radius along semi-major axis
  18- 21  F4.1  kpc          Lrad   Linear radius along semi-major axis
  23- 27  F5.2 mag/arcsec2   muFUV  ? FUV surface brightness (1)
  29- 32  F4.2 mag/arcsec2 e_muFUV  ? Uncertainty in muFUV
  34- 38  F5.2 mag/arcsec2   muNUV  ? NUV surface brightness (1)
  40- 43  F4.2 mag/arcsec2 e_muNUV  ? Uncertainty in muNUV (2)
  45- 49  F5.2 mag/arcsec2   mu3.6  ? 3.6 micron surface brightness (1)
  51- 54  F4.2 mag/arcsec2 e_mu3.6  ? Uncertainty in mu3.6 (2)
  56- 60  F5.2 mag/arcsec2   mu4.5  ? 4.5 micron surface brightness (1)
  62- 65  F4.2 mag/arcsec2 e_mu4.5  ? Uncertainty in mu4.5 (2)
  67- 71  F5.2 mag/arcsec2   mu5.8  ? 5.8 micron surface brightness (1)
  73- 76  F4.2 mag/arcsec2 e_mu5.8  ? Uncertainty in mu5.8 (2)
  78- 82  F5.2 mag/arcsec2   mu8.0  ? 8.0 micron surface brightness (1)
  84- 87  F4.2 mag/arcsec2 e_mu8.0  ? Uncertainty in mu8.0 (2)
  89- 93  F5.2 mag/arcsec2   mu24   ? 24 micron surface brightness (1)
  95- 98  F4.2 mag/arcsec2 e_mu24   ? Uncertainty in mu24 (2)
 100-104  F5.2 mag/arcsec2   mu70   ? 70 micron surface brightness (1)
 106-109  F4.2 mag/arcsec2 e_mu70   ? Uncertainty in mu70 (2)
 111-115  F5.2 mag/arcsec2   mu160  ? 160 micron surface brightness (1)
 117-120  F4.2 mag/arcsec2 e_mu160  ? Uncertainty in mu160 (2)
--------------------------------------------------------------------------------
Note (1): In AB magnitudes.
Note (2): The uncertainties include photometric and background errors, but
     not zero-point uncertainties, which are added in quadrature when needed.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table3.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1- 11  A11   ---     Name      Galaxy name
  13- 16  I4    arcsec  Arad      Angular radius along semi-major axis
  18- 21  F4.1  kpc     Lrad      Linear radius along semi-major axis
  23- 27  F5.2  [-]     TIR/FUV   ? Log of total IR to FUV luminosities
  29- 32  F4.2  [-]   e_TIR/FUV   ? Uncertainty in TIR/FUV
  34- 38  F5.2  [-]     TIR/NUV   ? Log of total IR to NUV luminosities
  40- 43  F4.2  [-]   e_TIR/NUV   ? Uncertainty in TIR/NUV
  45- 48  F4.2  mag     B05-AFUV  ? Buat et al. (B05) FUV extinction (1)
  50- 53  F4.2  mag   E_B05-AFUV  ? Upper limit uncertainty in B05-AFUV
  55- 58  F4.2  mag   e_B05-AFUV  ? Lower limit uncertainty in B05-AFUV
  60- 63  F4.2  mag     B05-ANUV  ? Buat et al. (B05) NUV extinction (1)
  65- 68  F4.2  mag   E_B05-ANUV  ? Upper limit uncertainty in B05-ANUV
  70- 73  F4.2  mag   e_B05-ANUV  ? Lower limit uncertainty in B05-ANUV
  75- 78  F4.2  mag     C08-AFUV  ? Cortese et al. (C08) FUV extinction (2)
  80- 83  F4.2  mag   E_C08-AFUV  ? Upper limit uncertainty in C08-AFUV
  85- 88  F4.2  mag   e_C08-AFUV  ? Lower limit uncertainty in C08-AFUV
  90- 93  F4.2  mag     C08-ANUV  ? Cortese et al. (C08) NUV extinction (2)
  95- 98  F4.2  mag   E_C08-ANUV  ? Upper limit uncertainty in C08-ANUV
 100-103  F4.2  mag   e_C08-ANUV  ? Lower limit uncertainty in C08-ANUV
--------------------------------------------------------------------------------
Note (1): Computed with the (star formation history) SFH-independent fits
     of Buat et al. (B05; 2005ApJ...619L..51B).
Note (2): Computed with the (star formation history) SFH-dependent
     prescriptions of Cortese et al. (C08; 2008MNRAS.386.1157C).
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table4.dat
--------------------------------------------------------------------------------
   Bytes Format Units        Label   Explanations
--------------------------------------------------------------------------------
   1- 11  A11   ---          Name    Galaxy name
  13- 15  I3    arcsec       Arad    Angular radius along semi-major axis
  17- 20  F4.1  kpc          Lrad    Linear radius along semi-major axis
  22- 24  F3.1  %            qPAH    Fraction of dust mass in form of PAHs
  26- 28  F3.1  %          E_qPAH    Upper limit uncertainty in qPAH
  30- 32  F3.1  %          e_qPAH    Lower limit uncertainty in qPAH
      34  A1    ---        f_qPAH    [d] Non-reliable value of qPAH (1)
  36- 38  F3.1  %            gamma   Fraction of dust mass heated by very
                                     intense starlight
  40- 42  F3.1  %          E_gamma   Upper limit uncertainty in gamma
  44- 46  F3.1  %          e_gamma   Lower limit uncertainty in gamma
  48- 51  F4.1  %            U>100   Fraction of dust luminosity contributed by
                                     regions heated by starlight with U>100 (2)
  53- 56  F4.1  %          E_U>100   Upper limit uncertainty in U>100
  58- 61  F4.1  %          e_U>100   Lower limit uncertainty in U>100
  63- 66  F4.1  ---          Umin    Minimum value for the starlight scale
                                     factor (2)
  68- 71  F4.1  ---        E_Umin    Upper limit uncertainty in Umin
  73- 76  F4.1  ---        e_Umin    Lower limit uncertainty in Umin
  78- 81  F4.1  ---          <U>     Dust-weighted average scale factor for
                                     starlight intensity (2)
  83- 86  F4.1  ---        E_<U>     Upper limit uncertainty in <U>
  88- 91  F4.1  ---        e_<U>     Lower limit uncertainty in <U>
  93- 97  F5.2 [Lsun/kpc2]   Ldust   Log of dust luminosity surface density (3)
  99-103  F5.2 [Lsun/kpc2] E_Ldust   Upper limit uncertainty in Ldust
 105-109  F5.2 [Lsun/kpc2] e_Ldust   Lower limit uncertainty in Ldust
 111-115  F5.2 [Msun/kpc2]   Mdust   Log of dust mass surface density (3)
 117-121  F5.2 [Msun/kpc2] E_Mdust   Upper limit uncertainty in Mdust
 123-127  F5.2 [Msun/kpc2] e_Mdust   Lower limit uncertainty in Mdust
 129-133  F5.2  [-]          Ratio   ? Log of dust-to-gas ratio (4)
 135-139  F5.2  [-]        E_Ratio   ? Upper limit uncertainty in Ratio
 141-145  F5.2  [-]        e_Ratio   ? Lower limit uncertainty in Ratio
     148  A1    ---        f_Ratio   [D] Missing CO data (5)
--------------------------------------------------------------------------------
Note (1): Indicates value is not reliable in regions where the dust
          contribution to the observed 8 micron flux is less than half of the
          stellar emission at that band.
Note (2): U is the intensity of the radiation field, expressed in units 
          of the local Milky Way (MW) radiation field.
Note (3): Corrected for inclination.
Note (4): The dust mass is computed as M_gas_=1.36x(M_HI_+M_H_2__)
Note (5): Indicates dust mass is computed as M_gas_=1.36xM_HI_
          because CO data are not available.
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

References:
    Munoz-Mateos et al. Paper I.   2009ApJ...703.1569M  Cat. J/ApJ/703/1569
    Munoz-Mateos et al. Paper III. 2011ApJ...731...10M

================================================================================
(End)                 Greg Schwarz [AAS], Emmanuelle Perret [CDS]    23-Sep-2011
