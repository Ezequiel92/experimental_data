J/AJ/136/2782       Star formation efficiency in nearby galaxies (Leroy+, 2008)
================================================================================
The star formation efficiency in nearby galaxies:
measuring where gas forms stars effectively.
    Leroy A.K., Walter F., Brinks E., Bigiel F., De Blok W.J.G., Madore B.,
    Thornley M.D.
   <Astron. J., 136, 2782-2845 (2008)>
   =2008AJ....136.2782L
================================================================================
ADC_Keywords: Galaxies, nearby ; H I data ; Radio lines
Keywords: galaxies: evolution - galaxies: ISM - radio lines: galaxies -
          stars: formation

Abstract:
    We measure the star formation efficiency (SFE), the star formation
    rate (SFR) per unit of gas, in 23 nearby galaxies and compare it with
    expectations from proposed star formation laws and thresholds. We use
    HI maps from The HI Nearby Galaxy Survey (THINGS) and derive H_2_ maps
    of CO measured by HERA CO-Line Extragalactic Survey and
    Berkeley-Illinois-Maryland Association Survey of Nearby Galaxies. We
    estimate the SFR by combining Galaxy Evolution Explorer (GALEX)
    far-ultraviolet maps and the Spitzer Infrared Nearby Galaxies Survey
    (SINGS) 24um maps, infer stellar surface density profiles from SINGS
    3.6um data, and use kinematics from THINGS.

Description:
    We assemble maps and radial profiles of the necessary quantities in 23
    nearby, star-forming galaxies that we list in order of increasing
    stellar mass in Table 2. These are galaxies for which we could compile
    the necessary data, which means the overlap of THINGS, SINGS, the
    GALEX Nearby Galaxy Survey (NGS), and (for spirals) either BIMA SONG
    or HERACLES.

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe         80        .   This file
table2.dat     34       23   Sample galaxies
table4.dat     80       23   Properties of sample galaxies
table7.dat     82      687   Table of radial profiles
--------------------------------------------------------------------------------

See also:
    J/AJ/136/2563 : HI Nearby Galaxy Survey, THINGS (Walter+, 2008)

Byte-by-byte Description of file: table2.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  A8    ---     Name  Galaxy (1)
       9  A1    ---   n_Name  [e] e for IR data from Spitzer archive (not SINGS)
  12- 13  I2    arcsec  Res   Angular resolution to match working spatial
                               resolution in the subsample, 400pc for dwarf
                               galaxies and 800pc for spirals
  15- 23  A9    ---     CO    Origin of CO data
  25- 26  A2    ---     RC    Rotation curve data (2)
  28- 34  A7    ---     Also  Also in Sample of (3)
--------------------------------------------------------------------------------
Note (1): In order of increasing stellar mass.
Note (2): Rotation curve data code as follows:
  dB = de Blok et al. (2008AJ....136.2648D)
   T = only THINGS first moment (Walter et al., 2008 Cat. J/AJ/136/2563)
Note (3): Sample codes as follows:
   1 = Kennicutt (1989ApJ...344..685K)
   2 = Martin & Kennicutt (2001ApJ...555..301M)
   3 = Wong & Blitz (2002ApJ...569..157W)
   4 = Boissier et al. (2003MNRAS.346.1215B)
   5 = Blitz & Rosolowsky (2006ApJ...650..933B)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table4.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label   Explanations
--------------------------------------------------------------------------------
   1-  8  A8    ---     Name    Galaxy name
  10- 13  F4.1  Mpc     Dist    Distance
  15- 16  I2    deg     i       Inclination
  18- 20  I3    deg     PA      Position angle
  22- 25  A4    ---     MType   Morphological type
  27- 31  F5.1  mag     BMAG    Absolute B magnitude
  33- 36  F4.1  kpc     r25     B-band isophotal radius at 25mag/arcsec^2^
  38- 40  I3    km/s    vflat   ?=- Free velocity parameter for our rotation
                                    curve fit
  42- 45  F4.1  kpc     lflat   ?=- Free scale length parameter for our rotation
                                    curve fit
  47- 50  F4.1  [Msun]  logM*   Stellar mass
  52- 55  F4.1  [Msun]  logMHI  HI mass
  57- 58  A2    ---   l_logMH2  [<= ] Limit flag on logMH2 (Upper limits are at
                                      5{sigma} significance)
  59- 61  F3.1  [Msun]  logMH2  ?=- H_2_ mass
      62  A1    ---   n_logMH2  [a] Note on logMH2 (1)
  64- 68  F5.3  Msun/yr SFR     Star formation rate
  70- 72  F3.1  kpc     l*      Scale length derived from exponential fits to
                                 the {Sigma}_*_ profile
  74- 76  F3.1  kpc     lSFR    Scale length derived from exponential fits to
                                 the {Sigma}_SFR_ profile
  78- 80  F3.1  kpc     lCO     ?=- Scale length derived from exponential fits
                                    to the {Sigma}_H2_(CO) profile
--------------------------------------------------------------------------------
Note (1): Unless noted logMH2 comes from
 * HERACLES (Leroy et al.  2008AJ....136.2782L) or
 * BIMA SONG (Helfer et al. 2003ApJS..145..259H).
 * NGC 3077 is from Walter et al. (2001AJ....121..727W) and
 * NGC 4449 is from Bolatto et al. (2008, Cat. J/ApJ/686/948).
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table7.dat
--------------------------------------------------------------------------------
   Bytes Format Units             Label    Explanations
--------------------------------------------------------------------------------
   1-  8  A8    ---               Name     Galaxy name
  10- 13  F4.1  kpc               r        Galactocentric radius of ring center
  15- 18  F4.2  ---               r.n      Normalized galactocentric radius
                                           (to r_25_) of ring center
  20- 24  F5.2 Msun/pc2           SigmaHI  ? Surface density of H I (2)
  26- 28  F3.1 Msun/pc2         e_SigmaHI  rms uncertainty in SigmaHI (3)
  30- 35  F6.2 Msun/pc2           SigmaH2  ? Surface density of H_2_ (2)
  37- 40  F4.1 Msun/pc2         e_SigmaH2  ? RMS uncertainty in SigmaH2
  42- 48  F7.1 Msun/pc2           Sigma*   Surface density of stars
  50- 54  F5.1 Msun/pc2         e_Sigma*   rms uncertainty in Sigma* (3)
  56- 62  F7.2 10-4Msun/yr/kpc2   FUV+24   ? Total star formation rate
                                             surface density
  64- 68  F5.1 10-4Msun/yr/kpc2 e_FUV+24   rms uncertainty in FUV+24
  70- 75  F6.2 10-4Msun/yr/kpc2   FUV      ? FUV portion of star formation
                                             rate surface density
  77- 82  F6.1 10-4Msun/yr/kpc2   24       ? 24 micron portion of star
                                             formation rate surface density
--------------------------------------------------------------------------------
Note (2): Including helium.
Note (3): 1.0 = upper limit.
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

================================================================================
(End)                  Greg Schwarz [AAS], Patricia Vannier [CDS]    18-Jun-2011
