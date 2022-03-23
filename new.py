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
                                                                                                                                                                                                                                                                                                                                                                                                samples (numpy.ndarray): data for which labels need to be predicted
                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                        Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                    list: list of labels predicted for the data.
                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                            """
                                                                                                                                                                                                                                                                                                                                                                                                                                    results = []
                                                                                                                                                                                                                                                                                                                                                                                                                                            for _, sample in enumerate(samples):
                                                                                                                                                                                                                                                                                                                                                                                                                                                            results.append(self.predict_one(sample))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return tuple(results)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def predict_one(self, sample) -> int:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Predict label of a single sample. The reason this method exists is
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                because often we might want to predict label for a single sample.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    sample (numpy.ndarray): Feature vector of the sample that we want to
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        predict the label for.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Returns:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            int: returns the label for the sample.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ~ This need to be implemented for the child models. The reason is that
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ~ ML models and DL models predict the labels differently.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            raise NotImplementedError()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def restore_model(self, load_path: str = None) -> None:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Restore the weights from a saved model and load them to the model.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Args:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    load_path (str): Optional, path to load the weights from a given path.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ")