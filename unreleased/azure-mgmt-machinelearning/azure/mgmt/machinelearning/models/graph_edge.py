# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphEdge(Model):
    """Defines an edge within the web service's graph.

    :param source_node_id: The source graph node's identifier.
    :type source_node_id: str
    :param source_port_id: The identifier of the source node's port that the
     edge connects from.
    :type source_port_id: str
    :param target_node_id: The destination graph node's identifier.
    :type target_node_id: str
    :param target_port_id: The identifier of the destination node's port that
     the edge connects into.
    :type target_port_id: str
    """

    _attribute_map = {
        'source_node_id': {'key': 'sourceNodeId', 'type': 'str'},
        'source_port_id': {'key': 'sourcePortId', 'type': 'str'},
        'target_node_id': {'key': 'targetNodeId', 'type': 'str'},
        'target_port_id': {'key': 'targetPortId', 'type': 'str'},
    }

    def __init__(self, source_node_id=None, source_port_id=None, target_node_id=None, target_port_id=None):
        self.source_node_id = source_node_id
        self.source_port_id = source_port_id
        self.target_node_id = target_node_id
        self.target_port_id = target_port_id
