FROM python:3.7-slim-buster
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils ca-certificates wget unzip git
RUN update-ca-certificates

WORKDIR /nnUNet
RUN git clone --depth 1 https://github.com/CarlosRea/nnUNet.git .
RUN pip install gdown
RUN gdown https://drive.google.com/uc?id=106kjLHgk6s6Rv7_Jfm5GxiWDbjOyarD2 
RUN unzip -oj fold_5.zip -d data/nnUNet_trained_models/nnUNet/3d_fullres/Task001_EM/nnUNetTrainerV2__nnUNetPlansv2.1/fold_5
RUN rm fold_5.zip

RUN pip install nnunet
RUN pip install -e .
RUN pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git@more_plotted_details#egg=hiddenlayer

ENV 'nnUNet_raw_data_base'="data/nnUNet_raw"
ENV 'nnUNet_preprocessed'="data/nnUNet_preprocessed"
ENV 'RESULTS_FOLDER'="data/nnUNet_trained_models"

COPY process.py .
COPY process.sh .