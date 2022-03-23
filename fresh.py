"""
speechemotionrecognition module.
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
                                                functionality to save the model to the disk, load the model from the
                                                        disk and train the model and evaluate the model to return appropriate
                                                                measure like accuracy, f1 score, etc.
                                                                
                                                                    Attributes:
                                                                            model (Any): instance variable that holds the model.
                                                                                    save_path (str): path to save the model.
                                                                                            name (str): name of the model.
                                                                                                    trained (bool): True if model has been trained, false otherwise.
                                                                                                        """
                                                                                                        
                                                                                                            def __init__(self, save_path: str = '', name: str = 'Not Specified'):
                                                                                                                        """
                                                                                                                                Default constructor for abstract class Model.
                                                                                                                                
                                                                                                                                        Args:
                                                                                                                                                    save_path(str): path to save the model to.
                                                                                                                                                                name(str): name of the model given as string.
                                                                                                                                                                
                                                                                                                                                                        """
                                                                                                                                                                                ~ Place holder for model
                                                                                                                                                                                        self.model = None
                                                                                                                                                                                                ~ Place holder on where to save the model
                                                                                                                                                                                                        self.save_path = save_path
                                                                                                                                                                                                                ~ Place holder for name of the model
                                                                                                                                                                                                                        self.name = name
                                                                                                                                                                                                                                ~ Model has been trained or not
                                                                                                                                                                                                                                        self.trained = False
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                            def train(self, x_train: numpy.ndarray, y_train: numpy.ndarray,
                                                                                                                                                                                                                                                                    x_val: numpy.ndarray = None,
                                                                                                                                                                                                                                                                                  y_val: numpy.ndarray = None) -> None:
                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                Trains the model with the given training data.
                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                        Args:
                                                                                                                                                                                                                                                                                    x_train (numpy.ndarray): samples of training data.
                                                                                                                                                                                                                                                                                                y_train (numpy.ndarray): labels for training data.
                                                                                                                                                                                                                                                                                                            x_val (numpy.ndarray): Optional, samples in the validation data.
                                                                                                                                                                                                                                                                                                                        y_val (numpy.ndarray): Optional, labels of the validation data.
                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                """
                                                                                                                                                                                                                                                                                                                                        ~ This will be specific to model so should be implemented by
                                                                                                                                                                                                                                                                                                                                                ~ child classes
                                                                                                                                                                                                                                                                                                                                                        raise NotImplementedError()
                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                        def predict(self, samples: numpy.ndarray) -> Tuple:
                                                                                                                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                                                                                                                            Predict labels for given data.
                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                    Args:
                                                                                                                                                                                                                                                                                                                                                                                    ")