from subprocess import call
from pathlib import Path
import argparse
import shutil
import sys
import os
import nibabel as nib
from pathlib import Path

parser = argparse.ArgumentParser(description="Detect new MS lesions from two FLAIR images.")

parser.add_argument('-d', '--data_folder', type=str, help="Path of the data folder.", default='/nnUNet/data/nnUNet_raw/nnUNet_raw_data/Task001_EM/')

args = parser.parse_args()

data_folder = Path(args.data_folder)

input_folder = data_folder / 'imagesTs'

output_folder = data_folder / 'output'
output_folder.mkdir(exist_ok=True)

call(['nnUNet_predict', '-i', str(input_folder), '-o', str(output_folder), '-t', '001', '-m', '3d_fullres', '-tr', 'nnUNetTrainerV2', '-f', '5'])

root_pred_test = Path(output_folder)

# renombramos los ficheros de salida
for f in sorted(os.listdir(root_pred_test)):

    if f.find('nii.gz') != -1:
      patient=f.split('_')[1]
      os.rename(os.path.join(root_pred_test, f),
                os.path.join(root_pred_test, f"{'mask'}_{patient}"))