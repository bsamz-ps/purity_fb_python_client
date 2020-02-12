# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.6 Python SDK

    Pure Storage FlashBlade REST 1.X Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Linkaggregationgroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ports': 'list[Reference]',
        'add_ports': 'list[Reference]',
        'remove_ports': 'list[Reference]'
    }

    attribute_map = {
        'ports': 'ports',
        'add_ports': 'add_ports',
        'remove_ports': 'remove_ports'
    }

    def __init__(self, ports=None, add_ports=None, remove_ports=None):
        """
        Linkaggregationgroup - a model defined in Swagger
        """

        self._ports = None
        self._add_ports = None
        self._remove_ports = None

        if ports is not None:
          self.ports = ports
        if add_ports is not None:
          self.add_ports = add_ports
        if remove_ports is not None:
          self.remove_ports = remove_ports

    @property
    def ports(self):
        """
        Gets the ports of this Linkaggregationgroup.

        :return: The ports of this Linkaggregationgroup.
        :rtype: list[Reference]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this Linkaggregationgroup.

        :param ports: The ports of this Linkaggregationgroup.
        :type: list[Reference]
        """

        self._ports = ports

    @property
    def add_ports(self):
        """
        Gets the add_ports of this Linkaggregationgroup.

        :return: The add_ports of this Linkaggregationgroup.
        :rtype: list[Reference]
        """
        return self._add_ports

    @add_ports.setter
    def add_ports(self, add_ports):
        """
        Sets the add_ports of this Linkaggregationgroup.

        :param add_ports: The add_ports of this Linkaggregationgroup.
        :type: list[Reference]
        """

        self._add_ports = add_ports

    @property
    def remove_ports(self):
        """
        Gets the remove_ports of this Linkaggregationgroup.

        :return: The remove_ports of this Linkaggregationgroup.
        :rtype: list[Reference]
        """
        return self._remove_ports

    @remove_ports.setter
    def remove_ports(self, remove_ports):
        """
        Sets the remove_ports of this Linkaggregationgroup.

        :param remove_ports: The remove_ports of this Linkaggregationgroup.
        :type: list[Reference]
        """

        self._remove_ports = remove_ports

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Linkaggregationgroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
