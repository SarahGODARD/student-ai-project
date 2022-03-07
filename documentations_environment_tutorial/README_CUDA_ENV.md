# INSTALL CUDA

## Install CUDA toolkit 10.1

First, you have to install the CUDA toolkit. Follow this [link] (https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork)

## Download cuDNN

Second, you have to download the cuDNN library. Remember that you have to become a NVDIA developer member to access to it. Follow this [link] (https://developer.nvidia.com/rdp/cudnn-download)

## Install cuDNN

As you see, the cuDNN library is a zip folder. To install it, unzip this file. Note that the NVIDIA GPU ComputingToolkit folder will be created where you choose to install CUDA. Now transfert the files inside as follow :

- [unzip_folder]/bin/* -> NVIDIA GPU ComputingToolkit\CUDA\v10.1\bin

- [unzip_folder]/include/* -> NVIDIA GPU ComputingToolkit\CUDA\v10.1\include

- [unzip_folder]/lib/* -> NVIDIA GPU ComputingToolkit\CUDA\v10.1\lib

## Add CUDA to your environment

You must add those two path to your windows environment. Look for the environment variables on windows and add :
 - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin
 - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\libnvvp

## Verify the installation

### With tensorflow-gpu

The easiest way to verify the installation AND the usage of the gpu is to download tensorflow-gpu as : pip install tensorflow-gpu. Note that you need to have download Python before.

Now, open a python console and execute :
> from tensorflow-gpu import *

If you do not have any error, the installation succeed.

### command line

You can verify your CUDA version with the following command line :

> nvidia-smi

or :

 > nvcc -V