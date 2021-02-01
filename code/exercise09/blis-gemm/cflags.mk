# These flags are for Intel, GCC/Clang may need different ones
CC = icc
CFLAGS := -O3 -xBROADWELL -ffast-math -qopenmp 
USE_LIKWID = No
USE_OPENBLAS = No
