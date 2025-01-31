from captum.attr import LayerFeatureAblation

from methods.AbstractAttributionMethod import AbstractAttributionMethod
from methods.method_keys import LAYER_FEATURE_ABLATION


class CaptumLayerFeatureAblation(AbstractAttributionMethod):

    @staticmethod
    def get_method_key():
        return LAYER_FEATURE_ABLATION

    @staticmethod
    def execute(model, init_args=None, exec_args=None):
        if exec_args is None:
            exec_args = {}
        if init_args is None:
            init_args = {}

        feature_abl = LayerFeatureAblation(model, **init_args)
        attribution = feature_abl.attribute(**exec_args)

        return attribution

    @staticmethod
    def get_required_init_keys():
        return ['layer']

    @staticmethod
    def get_required_exec_keys():
        return ['inputs']
