# lesion-segmentation-challenge-miccai21

## Introducción:

Este repositorio contiene instrucciones y scripts para la segmentacion automatica de lesiones en esclerosis multiple longitudinal. Se ha usado la herramienta open-source nnUNet https://github.com/MIC-DKFZ/nnUNet para el entrenamiento del modelo y los datos de las imagenes del desafio *Longitudinal Multiple Sclerosis Lesion Segmentation Challenge - MICCAI 2021.* 

## Instalación y ejecución

Para construir la imagen docker ejecute:

<code>docker build -t nnunet . </code>

Para correr la imagen docker siga los siguientes pasos:

1. ponga sus dos imagenes flair  (flair_time01.nii.gz and flair_time02.nii.gz) en la carpeta /data/input/. 
El nombre de las imagenes debe tener el siguiente formato *EM_{PACIENTE}_{PUNTO TEMPORAL}.{EXTENSION}*, ej:

- flair_time01.nii.gz -> EM_083_0000.nii.gz
- flair_time02.nii.gz -> EM_083_0001.nii.gz

2. Ejecute el siguiente comando:

<code>docker run --gpus 1 --entrypoint=/bin/sh --rm -v ${PWD}\data\input:/nnUNet/data/nnUNet_raw/nnUNet_raw_data/Task001_EM/imagesTs/ -v ${PWD}\data\output:/nnUNet/data/nnUNet_raw/nnUNet_raw_data/Task001_EM/output/ nnunet process.sh </code>

o el equivalente:

<code>docker-compose up</code>


