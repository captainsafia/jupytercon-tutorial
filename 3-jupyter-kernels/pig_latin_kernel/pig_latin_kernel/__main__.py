from ipykernel.kernelapp import IPKernelApp
from . import PigLatinKernel

IPKernelApp.launch_instance(kernel_class=PigLatinKernel)
