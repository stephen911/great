"""speechemotionrecognition module.
Provides a library to perform speech emotion recognition on `emodb` data set
"""
import sys
from typing import Tuple

import numpy
from sklearn.metrics import accuracy_score, confusion_matrix



class Model(object):
            """
                Model is the abstract class which determines how a model should be.
                    Any model inheriting this class should do the following.
                    