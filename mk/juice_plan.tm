KPL/MK

Meta-kernel for JUICE Dataset v453 -- Planning 20250306_001
============================================================================

   This meta-kernel lists the JUICE Planning SPICE kernels
   that provide information for the Planning scenario.

   The kernels listed in this meta-kernel and the order in which
   they are listed are picked to provide the best data available and
   the most complete coverage for the JUICE Planning scenario.

   This meta-kernel was generated with the Auxiliary Data Conversion
   System version: ADCSng v4.4.5.


Usage of the Meta-kernel
---------------------------------------------------------------------------

   This file is used by the SPICE system as follows: programs that make use
   of this kernel must "load" the kernel normally during program
   initialization. Loading the kernel associates the data items with
   their names in a data structure called the "kernel pool". The SPICELIB
   routine FURNSH loads a kernel into the pool.

   The kernels listed below can be obtained from the ESA SPICE Web server:

      https://spiftp.esac.esa.int/data/SPICE/JUICE/kernels/

   or from the ESA SPICE FTP server:

      ftp://spiftp.esac.esa.int/data/SPICE/JUICE/kernels/


Implementation Notes
---------------------------------------------------------------------------

   It is recommended that users make a local copy of this file and
   modify the value of the PATH_VALUES keyword to point to the actual
   location of the JUICE SPICE data set's ``data'' directory on
   their system. Replacing ``/'' with ``\'' and converting line
   terminators to the format native to the user's system may also be
   required if this meta-kernel is to be used on a non-UNIX workstation.


-------------------

   This file was created on March 6, 2025 by Alfredo Escalante Lopez ESA/ESAC.
   The original name of this file was juice_plan_v453_20250306_001.tm.


   \begindata

     PATH_VALUES       = ( '/Users/user/0-python/SPICE_python/spice/juice/kernels' )

     PATH_SYMBOLS      = ( 'KERNELS' )

     KERNELS_TO_LOAD   = (

                           '$KERNELS/ck/juice_sc_crema_5_1_150lb_23_1_default_v01.bc'
                           '$KERNELS/ck/juice_sc_crema_5_1_150lb_23_1_comms_v01.bc'
                           '$KERNELS/ck/juice_sc_crema_5_1_150lb_23_1_conjctn_v01.bc'
                           '$KERNELS/ck/juice_sc_crema_5_1_150lb_23_1_flybys_v01.bc'
                           '$KERNELS/ck/juice_sc_crema_5_1_150lb_23_1_baseline_v03.bc'
                           '$KERNELS/ck/juice_sc_ptr_soc_pcw3_s01p00_v06.bc'
                           '$KERNELS/ck/juice_sc_ptr_soc_s007_01_s06p00_v01.bc'
                           '$KERNELS/ck/juice_sc_attc_000080_230414_250425_v01.bc'
                           '$KERNELS/ck/juice_lpbooms_f160326_v01.bc'
                           '$KERNELS/ck/juice_magboom_f160326_v04.bc'
                           '$KERNELS/ck/juice_majis_scan_zero_v02.bc'
                           '$KERNELS/ck/juice_majis_scan_stp_240819_240820_v01.bc'
                           '$KERNELS/ck/juice_swi_scan_zero_v02.bc'
                           '$KERNELS/ck/juice_sa_crema_5_1_150lb_23_1_default_v01.bc'
                           '$KERNELS/ck/juice_sa_crema_5_1_150lb_23_1_baseline_v04.bc'
                           '$KERNELS/ck/juice_sa_ptr_soc_s007_01_s02p00_v01.bc'
                           '$KERNELS/ck/juice_mga_crema_5_1_150lb_23_1_default_v01.bc'
                           '$KERNELS/ck/juice_mga_crema_5_1_150lb_23_1_baseline_v04.bc'
                           '$KERNELS/ck/juice_mga_ptr_soc_s007_01_s02p00_v01.bc'

                           '$KERNELS/fk/juice_v42.tf'
                           '$KERNELS/fk/juice_sci_v17.tf'
                           '$KERNELS/fk/juice_ops_v12.tf'
                           '$KERNELS/fk/juice_dsk_surfaces_v11.tf'
                           '$KERNELS/fk/juice_roi_v02.tf'
                           '$KERNELS/fk/juice_events_crema_5_1_150lb_23_1_v02.tf'
                           '$KERNELS/fk/juice_stations_topo_v01.tf'
                           '$KERNELS/fk/rssd0002.tf'
                           '$KERNELS/fk/earth_topo_201023.tf'
                           '$KERNELS/fk/estrack_v04.tf'

                           '$KERNELS/dsk/juice_europa_plasma_torus_v03.bds'
                           '$KERNELS/dsk/juice_io_plasma_torus_v05.bds'
                           '$KERNELS/dsk/juice_jup_ama_gos_ring_v02.bds'
                           '$KERNELS/dsk/juice_jup_halo_ring_v04.bds'
                           '$KERNELS/dsk/juice_jup_main_ring_v04.bds'
                           '$KERNELS/dsk/juice_jup_the_ring_ext_v01.bds'
                           '$KERNELS/dsk/juice_jup_the_gos_ring_v02.bds'
                           '$KERNELS/dsk/juice_sc_fixed_v01.bds'
                           '$KERNELS/dsk/juice_sc_bus_v07.bds'
                           '$KERNELS/dsk/juice_sc_gala_v02.bds'
                           '$KERNELS/dsk/juice_sc_janus_v02.bds'
                           '$KERNELS/dsk/juice_sc_jmc1_v02.bds'
                           '$KERNELS/dsk/juice_sc_jmc2_v02.bds'
                           '$KERNELS/dsk/juice_sc_navcam1_v01.bds'
                           '$KERNELS/dsk/juice_sc_navcam2_v01.bds'
                           '$KERNELS/dsk/juice_sc_lpb1_v02.bds'
                           '$KERNELS/dsk/juice_sc_lpb2_v02.bds'
                           '$KERNELS/dsk/juice_sc_lpb3_v02.bds'
                           '$KERNELS/dsk/juice_sc_lpb4_v02.bds'
                           '$KERNELS/dsk/juice_sc_rwi_v04.bds'
                           '$KERNELS/dsk/juice_sc_scm_v03.bds'
                           '$KERNELS/dsk/juice_sc_mag_v06.bds'
                           '$KERNELS/dsk/juice_sc_majis_v02.bds'
                           '$KERNELS/dsk/juice_sc_mga_apm_v04.bds'
                           '$KERNELS/dsk/juice_sc_mga_dish_v04.bds'
                           '$KERNELS/dsk/juice_sc_pep_jdc_v02.bds'
                           '$KERNELS/dsk/juice_sc_pep_jei_v02.bds'
                           '$KERNELS/dsk/juice_sc_pep_jeni_v02.bds'
                           '$KERNELS/dsk/juice_sc_pep_jna_v02.bds'
                           '$KERNELS/dsk/juice_sc_pep_nim_v02.bds'
                           '$KERNELS/dsk/juice_sc_rimemx_v03.bds'
                           '$KERNELS/dsk/juice_sc_rimepx_v03.bds'
                           '$KERNELS/dsk/juice_sc_sapy_v02.bds'
                           '$KERNELS/dsk/juice_sc_samy_v02.bds'
                           '$KERNELS/dsk/juice_sc_str1_v02.bds'
                           '$KERNELS/dsk/juice_sc_str2_v02.bds'
                           '$KERNELS/dsk/juice_sc_str3_v02.bds'
                           '$KERNELS/dsk/juice_sc_swi_v03.bds'
                           '$KERNELS/dsk/juice_sc_uvs_v01.bds'

                           '$KERNELS/ik/juice_gala_v05.ti'
                           '$KERNELS/ik/juice_janus_v08.ti'
                           '$KERNELS/ik/juice_jmc_v03.ti'
                           '$KERNELS/ik/juice_jmag_v02.ti'
                           '$KERNELS/ik/juice_majis_v09.ti'
                           '$KERNELS/ik/juice_navcam_v02.ti'
                           '$KERNELS/ik/juice_pep_v14.ti'
                           '$KERNELS/ik/juice_radem_v03.ti'
                           '$KERNELS/ik/juice_rime_v04.ti'
                           '$KERNELS/ik/juice_rpwi_v03.ti'
                           '$KERNELS/ik/juice_str_v01.ti'
                           '$KERNELS/ik/juice_swi_v07.ti'
                           '$KERNELS/ik/juice_uvs_v07.ti'
                           '$KERNELS/ik/juice_aux_v02.ti'

                           '$KERNELS/lsk/naif0012.tls'

                           '$KERNELS/pck/pck00011.tpc'
                           '$KERNELS/pck/de-403-masses.tpc'
                           '$KERNELS/pck/gm_de431.tpc'

                           '$KERNELS/pck/inpop19a_moon_pa_v01.bpc'
                           '$KERNELS/pck/earth_070425_370426_predict.bpc'

                           '$KERNELS/pck/juice_jup011.tpc'
                           '$KERNELS/pck/juice_roi_v01.tpc'

                           '$KERNELS/sclk/juice_fict_160326_v02.tsc'

                           '$KERNELS/spk/juice_sci_v04.bsp'
                           '$KERNELS/spk/juice_struct_v21.bsp'
                           '$KERNELS/spk/juice_struct_internal_v01.bsp'
                           '$KERNELS/spk/juice_cog_v00.bsp'
                           '$KERNELS/spk/juice_cog_000080_230416_250409_v01.bsp'
                           '$KERNELS/spk/juice_roi_v02.bsp'
                           '$KERNELS/spk/mar085_20200101_20400101.bsp'
                           '$KERNELS/spk/earthstns_fx_201023.bsp'
                           '$KERNELS/spk/estrack_v04.bsp'
                           '$KERNELS/spk/juice_earthstns_v01.bsp'
                           '$KERNELS/spk/jup365_19900101_20500101.bsp'
                           '$KERNELS/spk/jup344_19900101_20500101.bsp'
                           '$KERNELS/spk/jup344-s2003_j24_19900101_20500101.bsp'
                           '$KERNELS/spk/jup346_19900101_20500101.bsp'
                           '$KERNELS/spk/de432s.bsp'
                           '$KERNELS/spk/inpop19a_19900101_20500101.bsp'
                           '$KERNELS/spk/noe-5-2017-gal-a-reduced_20200101_20380902.bsp'
                           '$KERNELS/spk/juice_crema_5_1_150lb_23_1_plan_v01.bsp'
                           '$KERNELS/spk/juice_orbc_000080_230414_310721_v01.bsp'

                         )

   \begintext


SPICE Kernel Dataset Version
--------------------------------------------------------------------------

   The SPICE Kernel Dataset version of the kernels present in this
   meta-kernel is provided by the following keyword (please note that
   this might not be the last version of the SPICE Kernel Dataset):

   \begindata

      SKD_VERSION = 'v453_20250306_001'

   \begintext

   The unique identifier for this meta-kernel is provided by the following
   keyword:

   \begindata

      MK_IDENTIFIER = 'juice_plan_v453_20250306_001'

   \begintext


Contact Information
--------------------------------------------------------------------------

   If you have any questions regarding this file contact the
   ESA SPICE Service (ESS) at ESAC:

           Alfredo Escalante Lopez
           (+34) 91-8131-429
           spice@cosmos.esa.int,


End of MK file.