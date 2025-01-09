# %%
import os
import pandas as pd
import glob

# %%
start_dir = '/Users/ianliu/Medical Research/Data/17-plus7/derivatives/petsurfer'
# list of first-level directory names under start_dir
subjs = [f for f in os.listdir(start_dir) if os.path.isdir(os.path.join(start_dir, f))]

tac_files = glob.glob("/Users/ianliu/Medical Research/Data/17-plus7/derivatives/petsurfer/*/ses-baseline/pet/*_ses-baselinebrain_pvc-nopvc_desc-mc_tacs.tsv")
# tac_files = glob.glob("/Volumes/PortableSSD/data/17plus7_Blokers/*/petsurfer/pet/*_ses-baselinebrain_pvc-nopvc_desc-mc_tacs.tsv")
tac_files = sorted(tac_files)

header = pd.read_csv("~/Medical Research/Data/Blood/derivatives/petsurfer/sub-PS40/ses-baseline/pet/sub-PS40_ses-baselinebrain_pvc-nopvc_desc-mc_tacs.tsv",
                     sep='\t', nrows=1)
header.drop(columns=['frame_start', 'frame_end', 'highbinding', 'reference'], inplace=True)
header = header.columns


ref_files = glob.glob(
    "/Users/ianliu/Medical Research/Data/17-plus7/derivatives/petsurfer/*/ses-baseline/pet/gtm-no-pvc/km.ref.tac.dat"
    # "/Volumes/PortableSSD/data/17plus7_Blokers/*/petsurfer/pet/gtm-no-pvc/km.ref.tac.dat"
    )
ref_files = sorted(ref_files)

hb_files = glob.glob(
    "/Users/ianliu/Medical Research/Data/17-plus7/derivatives/petsurfer/*/ses-baseline/pet/gtm-no-pvc/km.hb.tac.dat"
    # "/Volumes/PortableSSD/data/17plus7_Blokers/*/petsurfer/pet/gtm-no-pvc/km.hb.tac.dat"
    )
hb_files = sorted(hb_files)
assert(len(tac_files) == len(ref_files) == len(hb_files))

df_28_rows = pd.read_csv("~/Medical Research/Data/Blood/derivatives/petsurfer/sub-PS40/ses-baseline/pet/sub-PS40_ses-baselinebrain_pvc-nopvc_desc-mc_tacs.tsv",
                     sep='\t', nrows=28)
frame_start = df_28_rows['frame_start']
frame_end = df_28_rows['frame_end']

# read tac_file
# convert every 100 lines to a new row of TSV separated by tabs
# (right now it's separated by newlines)

for indx, tac_file in enumerate(tac_files):
    new_tsv = pd.DataFrame(columns=header)
    with open(tac_file, 'r', encoding='utf-8') as f:
        vals = f.read().split()
        for i in range(0, len(vals), 100):
            # append row to new_tsv
            new_tsv = new_tsv.append(pd.Series(vals[i:i+100], index=header), ignore_index=True)
    with open(ref_files[indx], 'r', encoding='utf-8') as f:
        vals = f.read().split()
        new_tsv['reference'] = vals
        
    with open(hb_files[indx], 'r', encoding='utf-8') as f:
        vals = f.read().split()
        new_tsv['highbinding'] = vals
        
    new_tsv['frame_start'] = frame_start
    new_tsv['frame_end'] = frame_end
    new_tsv.to_csv(tac_file, sep='\t', index=False)
    
# %%

        

# %%
