# Example Workflow using `ENIGMA`, `bloodstream`, `kinfitr`, and `AHBA`

Example use shown

![image](https://github.com/user-attachments/assets/97074d13-add8-45f7-9261-df0e2ffdc3d0)

<img width="694" alt="image" src="https://github.com/user-attachments/assets/3ebb8bba-7a8a-48cc-8bde-0dc68226bcd9" />
<img width="714" alt="image" src="https://github.com/user-attachments/assets/86f2575e-f0fc-4606-8b89-6427519a6513" />


General pipeline/workflow is as follows:
 
1. Use Bash shell scripting to semi-automate the PETsurfer processing of all subjects, up to the `mri_gtmpv` step of PETsurfer. 
2. Use a custom Python script to extract the values of `nopvc.nii.gz` (TAC of all 100 ROIs), `km.hb.tac.dat` (TAC of highbinding regions), `km.ref.tac.dat` (TAC of reference regions) and compile them into one TSV file subj_ses-sessionname_pvc-nopvc_desc-mc_tacs.tsv 
2.5. Only copy the relevant files for processing (all .json files, blood files, TAC files, PETsurfer PET folder)
3. Create a configuration file for `bloodstream` using https://mathesong.shinyapps.io/bloodstream_config/ 
4. Use the `bloodstream` R package to load the configuration file, which generate a bloodstream folder in the derivatives directory 
5. Using the `bloodstream` R package results along with TAC files, we use the `kinfitr` package to fit multilinear analysis-1(MA1) models, which uses both blood and imaging data and is known to perform better out of all available models (SRTM, SRTM2, MRTM1, MRTM2, MA1, etc.), as shown in: https://pmc.ncbi.nlm.nih.gov/articles/PMC3851894/

6. Extract all Vt values for each ROI into a CSV file
7. Convert ROI names from freesurfer ROI labels to ENIGMA labels
8. Separate ROI by session, for each subject: 
a) compute the mean of all ROI for this subject
b) compute the standard deviation of all ROI for this subject
c) compute the Z-score for all ROI for this subject by subtracting the subject mean and dividing by the subject standard deviation
9. Compute the average for all subjects for all sessions (convert subject x 100 matrix to 1 x 100 vector)
10. Preserve cortical and subcortical regions as defined by ENIGMA
11. Visualize and change the color scale to be from -3 to 3 

12. Using the Z-score average of all subects (two 1x 100 vectors), keep only values as required by ENIGMA Python package. 

Data from https://figshare.com/articles/dataset/A_FreeSurfer_view_of_the_cortical_transcriptome_generated_from_the_Allen_Human_Brain_Atlas/1439749  provided AHBA gene expression on DK atlas (only a few left regions plus all cortical regions). The genetic expression data is normalized using Z-score method (using mean and standard deviation of each ROI across all genes). Here we demonstrate use with PTGS1.
The Z-score of PTGS1 was visualized using ENIGMA and Spearman’s rank correlation was calculated.
