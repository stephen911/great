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
                    
                        1.  Set the model instance variable to the corresponding model class which
                                which will provide methods `fit` and `predict`.
                                
                                    2.  Should implement the following abstract methods `load_model`,
                                            `save_model` `train` and `evaluate`. These methods provide the
                                            