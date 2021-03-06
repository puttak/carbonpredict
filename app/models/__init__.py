
from abc import ABC, abstractmethod

class CarbonModelBase(ABC):

    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load(base_dir):
        """
        Load existing model
        @param filename name of the existing model
        """
        pass

    @abstractmethod
    def train(X, y, base_dir=None):
        """
        Train and save the model to
        a given location. 

        @param X Training data
        @param y Training labels
        @param base_dir Directory to save the model
        """
        pass

    @abstractmethod
    def eval(X, y):
        """
        Evaluate the model and return S^2 score. 

        @param X Training data
        @param y Training labels
        @return S^2 score 
        """
        pass

     
    @abstractmethod
    def predict(X):
        """
        Predict from loaded model. Make sure
        to load() or train() the model first.

        @param X Data to predict from.
        @return prediction 
        """
        pass

# Import your models here
from .dummy import DummyModel
from .lgbm_default import LGBMDefault

# Add your model to AVAILABLE_MODELS as name: Model entry. 
# Name is used in the command line to select the model.
AVAILABLE_MODELS = {'dummy': DummyModel, 
                    'lgbm_default': LGBMDefault}