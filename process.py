from subprocess import call
from pathlib import Path
import argparse
import shutil
import sys
import os
import nibabel as nib
from pathlib import Path

parser = argparse.ArgumentParser(description="Detect new MS lesions from two FLAIR images.")

# parser.add_argument('-t1', '--time01', type=str, help="First time step (path to the FLAIR image).", required=True)
# parser.add_argument('-t2', '--time02', type=str, help="Second time step (path to the FLAIR image).", required=True)
# parser.add_argument('-o', '--output', type=str, help="Path of the output segmentation.", required=True)
# parser.add_argument('-d', '--data_folder', type=str, help="Path of the data folder.", default='/nnUNet/data/')
parser.add_argument('-d', '--data_folder', type=str, help="Path of the data folder.", default='/nnUNet/data/nnUNet_raw/nnUNet_raw_data/Task001_EM/')

args = parser.parse_args()

# flair_time01 = Path(args.time01)
# flair_time02 = Path(args.time02)
# output = Path(args.output)
data_folder = Path(args.data_folder)

# Create nnUNet directory stucture
#  input files must follow the following naming convention: case_identifier_XXXX.nii.gz
#  see [nnUNet documentation](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_conversion.md)

input_folder = data_folder / 'imagesTs'
# input_folder = data_folder / 'input' / 'nnUNet_raw_data'
# input_folder = data_folder /'nnUNet_raw'/'nnUNet_raw_data'/'Task001_EM'/'imagesTs'
# input_folder.mkdir(exist_ok=True, parents=True)
# input_file = input_folder / flair_time01.name.replace('.nii.gz', '_0000.nii.gz')
# shutil.copy(flair_time01, input_file)

# root=Path("E:\Master Ciencia de Datos\TFM\implementacion\project\data\input")
# root_dest=Path("E:\Master Ciencia de Datos\TFM\implementacion\project\data\input")
# for f in sorted(os.listdir(root)):
#   patient = f.split('_')[0].replace('atlas','').rjust(3, '0')
#   ext=f.split('FL')[1]
  
#   if '_00_' in f:
#     os.rename(os.path.join(root, f),
#               os.path.join(root_dest, f"{'EM'}_{patient}_0000{ext}"))
#   elif '_01_' in f:
#     os.rename(os.path.join(root, f),
#             os.path.join(root_dest, f"{'EM'}_{patient}_0001{ext}"))

output_folder = data_folder / 'output'
output_folder.mkdir(exist_ok=True)

#nnUNet_predict -i data/nnUNet_raw/nnUNet_raw_data/Task001_EM/imagesTr -o data/nnUNet_raw/nnUNet_raw_data/Task001_EM/output -t 001 -m 3d_fullres -f 5 --save_npz
call(['nnUNet_predict', '-i', str(input_folder), '-o', str(output_folder), '-t', '001', '-m', '3d_fullres', '-tr', 'nnUNetTrainerV2', '-f', '5'])

# output_nnunet = output_folder / flair_time01.name

# shutil.move(output_nnunet, output)

def save2nifti(data, affine, file_name):
  """
  Save data to a nifti file.

  """
  img = nib.Nifti1Image(data, affine)
  nib.save(img, file_name)

# root_pred_test_nifti = Path('/nnUNet/data/nnUNet_raw/nnUNet_raw_data/Task001_EM/output_test_nifti/')
root_pred_test = Path(output_folder)

# if not os.path.exists(root_pred_test_nifti):
#     # os.makedirs(root_pred_test_nifti, exist_ok=True)
#     root_pred_test_nifti.mkdir(parents=True)

# for out in list(sorted(root_pred_test.glob("*.nii.gz"))):
for f in sorted(os.listdir(root_pred_test)):
    # pred = nib.load(out)
    # mask = pred.get_fdata()

    # affine=pred.affine
    if f.find('nii.gz') != -1:
      patient=f.split('_')[1]
      # f='mask_'+patient+'.nii.gz'
      # file_name=os.path.join(root_pred_test_nifti,f)
      #   print(file_name)
      # save2nifti(mask, affine, file_name)
      os.rename(os.path.join(root_pred_test, f),
                os.path.join(root_pred_test, f"{'mask'}_{patient}"))