# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG),
# acting on behalf of its Max Planck Institute for Intelligent Systems and the
# Max Planck Institute for Biological Cybernetics. All rights reserved.
#
# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is holder of all proprietary rights
# on this computer program. You can only use this computer program if you have closed a license agreement
# with MPG or you get the right to use the computer program from someone who is authorized to grant you that right.
# Any use of the computer program without a valid license is prohibited and liable to prosecution.
# Contact: ps-license@tuebingen.mpg.de
#
#
# If you use this code in a research publication please consider citing the following:
#
# STAR: Sparse Trained  Articulated Human Body Regressor <https://arxiv.org/pdf/2008.08535.pdf>
#
#
# Code Developed by:
# Ahmed A. A. Osman

path_model = '/ps/scratch/aosman/STAR/eccv2020_release/star/male/model.npy'
from pytorch.star import STAR 
'''
    Remove dependency on opencv 
    Add the shape component 
'''
import tensorflow as tf 
batch_size = 10

star = STAR()
import torch
import numpy as np 
from torch.autograd import Variable

poses = torch.cuda.FloatTensor(np.zeros((batch_size,72)))
poses = Variable(poses,requires_grad=True)
betas = torch.cuda.FloatTensor(np.zeros((batch_size,10)))
betas = Variable(betas,requires_grad=True)

trans = torch.cuda.FloatTensor(np.zeros((batch_size,3)))
trans = Variable(trans,requires_grad=True)
d = star(poses, betas,trans)

       