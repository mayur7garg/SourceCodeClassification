FROM tensorflow/tensorflow:2.8.0-gpu

#Issue: https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/
#Resolution reference: https://stackoverflow.com/questions/72051754/apt-update-in-azure-nvidia-gives-publickey-error
RUN apt-get install -y wget
RUN apt-key del 7fa2af80
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt-get update && apt-get install -y git graphviz
RUN pip install --upgrade pip
RUN mkdir /project
COPY ../requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt