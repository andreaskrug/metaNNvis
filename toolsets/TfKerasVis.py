from frameworks.TensorFlow2Framework import TensorFlow2Framework
from methods.TfKerasVisSaliency import TfKerasVisSaliency
from toolsets.Toolset import Toolset
from toolsets.toolset_keys import TF_KERAS_VIS


class TfKerasVis(Toolset):

    @staticmethod
    def get_toolset_key():
        return TF_KERAS_VIS

    @staticmethod
    def get_framework():
        return TensorFlow2Framework.get_framework_key()

    @staticmethod
    def get_methods(method_type):
        return filter(lambda x: x.get_method_type() == method_type, [TfKerasVisSaliency])
