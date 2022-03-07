# Requirements

- visual studio 2013 or 2015
- CUDA for GPU version (refers on the corresponding documentation)
- [Cmake] (https://cmake.org/download/) (download the zip file and follow the instructions) and Ninja
- git (for the installation)

# Caffe installation

## Command lines

 > git clone https://github.com/BVLC/caffe.git
 > cd caffe
 > git checkout windows
 > scripts\build_win.cmd

 If CUDA is not installed Caffe will default to a CPU_ONLY build. If you have CUDA installed but want a CPU only build you may use the CMake option -DCPU_ONLY=1.

 If you have any problem, you can follow this [link] (https://caffe.berkeleyvision.org/installation.html)