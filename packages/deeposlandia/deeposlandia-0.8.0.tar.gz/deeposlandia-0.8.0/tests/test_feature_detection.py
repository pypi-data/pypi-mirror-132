"""Unit test related to the feature detection model
"""

from tensorflow import keras as K

from deeposlandia.feature_detection import FeatureDetectionNetwork


def test_simple_network_architecture(shapes_image_size, nb_channels, shapes_nb_labels):
    """Test a simple feature detection network"""
    net = FeatureDetectionNetwork(
        "fd_test",
        image_size=shapes_image_size,
        nb_channels=nb_channels,
        nb_labels=shapes_nb_labels,
    )
    model = K.models.Model(net.in_tensor, net.out_tensor)
    input_shape = model.input_shape
    output_shape = model.output_shape
    assert len(input_shape) == 4
    assert input_shape[1:] == (
        shapes_image_size,
        shapes_image_size,
        nb_channels,
    )
    assert len(output_shape) == 2
    assert output_shape[1] == shapes_nb_labels


def test_vgg16_network_architecture(
    mapillary_image_size, nb_channels, mapillary_nb_labels
):
    """Test a VGG16-inspired feature detection network"""
    net = FeatureDetectionNetwork(
        "fd_test",
        image_size=mapillary_image_size,
        nb_channels=nb_channels,
        nb_labels=mapillary_nb_labels,
        architecture="vgg",
    )
    model = K.models.Model(net.in_tensor, net.out_tensor)
    input_shape = model.input_shape
    output_shape = model.output_shape
    assert len(input_shape) == 4
    assert input_shape[1:] == (
        mapillary_image_size,
        mapillary_image_size,
        nb_channels,
    )
    assert len(output_shape) == 2
    assert output_shape[1] == mapillary_nb_labels


def test_inception_network_architecture(
    mapillary_image_size, nb_channels, mapillary_nb_labels
):
    """Test a Inception-inspired feature detection network"""
    net = FeatureDetectionNetwork(
        "fd_test",
        image_size=mapillary_image_size,
        nb_channels=nb_channels,
        nb_labels=mapillary_nb_labels,
        architecture="inception",
    )
    model = K.models.Model(net.in_tensor, net.out_tensor)
    input_shape = model.input_shape
    output_shape = model.output_shape
    assert len(input_shape) == 4
    assert input_shape[1:] == (
        mapillary_image_size,
        mapillary_image_size,
        nb_channels,
    )
    assert len(output_shape) == 2
    assert output_shape[1] == mapillary_nb_labels
