# Baseline VS Blocked

A lens into $[^{11}C]$PS13 baseline va blocked 

To evaluate the impact of blocking on imaging transcriptomics, we utilized a database of 22 baseline [11C]PS13 PET images (consisting of PS11  PS17  PS19  PS20  PS21  PS23  PS24  PS26  PS27  PS28  PS29  PS31  PS38  PS39  PS40  PS42 PSBB01  PSBB02  PSBB03  PSBB05  PSBB06   PSBB07) and 7 blocked (consisting of PS53  PSBB01  PSBB02  PSBB03  PSBB05  PSBB06   PSBB07) totaling 29 images. 

Our general pipeline/workflow is as follows:
 
1. Use Bash shell scripting to semi-automate the PETsurfer processing of all subjects, up to the `mri_gtmpv` step of PETsurfer. 
2. Use a custom Python script to extract the values of `nopvc.nii.gz` (TAC of all 100 ROIs), `km.hb.tac.dat` (TAC of highbinding regions), `km.ref.tac.dat` (TAC of reference regions) and compile them into one TSV file subj_ses-sessionname_pvc-nopvc_desc-mc_tacs.tsv 
2.5: Only copy the relevant files for processing (all .json files, blood files, TAC files, PETsurfer PET folder)
3. Create a configuration file for `bloodstream` using https://mathesong.shinyapps.io/bloodstream_config/ 
4. Use the `bloodstream` R package to load the configuration file, which generate a bloodstream folder in the derivatives directory 
5. Using the `bloodstream` R package results along with TAC files, we use the `kinfitr` package to fit multilinear analysis-1(MA1) models, which uses both blood and imaging data and is known to perform better out of all available models (SRTM, SRTM2, MRTM1, MRTM2, MA1, etc.), as shown in: https://pmc.ncbi.nlm.nih.gov/articles/PMC3851894/

6. Extract all Vt values for each ROI into a CSV file
7. Convert ROI names from freesurfer ROI labels to ENIGMA labels
8. Separate ROI by session (baselinebrain and blockedbrain), for each subject: 
a) compute the mean of all ROI for this subject
b) compute the standard deviation of all ROI for this subject
c) compute the Z-score for all ROI for this subject by subtracting the subject mean and dividing by the subject standard deviation
9. Compute the average for all subjects for all sessions (convert 22 x 100 matrix or 7 x 100 matrix to 1 x 100 vector)
10. Preserve cortical and subcortical regions as defined by ENIGMA
11. Visualize and change the color scale to be from -3 to 3 

12. Using the Z-score average of all subects (two 1x 100 vectors), keep only values as required by ENIGMA Python package. 

We used data from https://figshare.com/articles/dataset/A_FreeSurfer_view_of_the_cortical_transcriptome_generated_from_the_Allen_Human_Brain_Atlas/1439749 which provided AHBA gene expression on DK atlas (only a few left regions plus all cortical regions). The genetic expression data was normalized using Z-score method (using mean and standard deviation of each ROI across all genes). The PTGS1 gene was selected based on literature review and domain knowledge. 

The Z-score of PTGS1 was visualized using ENIGMA and Spearman’s rank correlation was calculated between baseline and blocked Vt Z-scores. Results indicated that Z-scores of PTGS1 and baseline sessions had a statistically significant correlation of 0.34 while PTGS1 and blocked sessions had a statistically significant correlation of -0.36, which suggests blocked sessions altered the spatial pattern of PGTS1.




