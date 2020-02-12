# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK. Compatible with REST API versions 1.0 - 1.9. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Resource(object):
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
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, name=None, id=None):
        """
        Resource - a model defined in Swagger
        """

        self._name = None
        self._id = None

        if name is not None:
          self.name = name
        if id is not None:
          self.id = id

    @property
    def name(self):
        """
        Gets the name of this Resource.
        name of the object

        :return: The name of this Resource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Resource.
        name of the object

        :param name: The name of this Resource.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this Resource.
        A unique ID chosen by the system. Cannot change.

        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Resource.
        A unique ID chosen by the system. Cannot change.

        :param id: The id of this Resource.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
