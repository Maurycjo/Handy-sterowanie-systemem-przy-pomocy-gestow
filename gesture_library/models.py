from keras.models import load_model


class ModelFactory:

    def __init__(self):
        self.rgbpath = 'trained_models/rgblstm.h5'

    def getModel(self):
        return load_model(self.rgbpath)