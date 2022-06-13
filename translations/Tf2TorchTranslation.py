import os

import torch

from frameworks.PyTorchFramework import PyTorchFramework
from frameworks.TensorFlow2Framework import TensorFlow2Framework
from translations.Translation import Translation
import tensorflow as tf
from onnx2torch.converter import convert


class Tf2TorchTranslation(Translation):

    @staticmethod
    def get_input():
        return TensorFlow2Framework.get_framework_key()

    @staticmethod
    def get_output():
        return PyTorchFramework.get_framework_key()

    @staticmethod
    def translate(model, **kwargs):
        # TODO: clean up console output
        tf_path = os.path.join('models', 'temp_tf')
        tf.saved_model.save(model, tf_path)
        os.system('python3 -m tf2onnx.convert --saved-model ./models/temp_tf --output ./models/temp_tf2onnx.onnx')

        onnx_path = os.path.join('models', 'temp_tf2onnx.onnx')
        torch_model = convert(onnx_path)

        return torch_model


if __name__ == '__main__':
    model = tf.saved_model.load(os.path.join('..', 'project_preparation_demo', 'models', 'mnist_tf_pretrained'))
    print(model)
    torch_model = Tf2TorchTranslation.translate(model)
    print(torch_model)
    input = torch.randn([1, 1, 28, 28])
    print(torch_model(input))
