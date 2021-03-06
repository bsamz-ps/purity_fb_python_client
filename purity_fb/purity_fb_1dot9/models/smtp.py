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


class Smtp(object):
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
        'relay_host': 'str',
        'sender_domain': 'str'
    }

    attribute_map = {
        'name': 'name',
        'relay_host': 'relay_host',
        'sender_domain': 'sender_domain'
    }

    def __init__(self, name=None, relay_host=None, sender_domain=None):
        """
        Smtp - a model defined in Swagger
        """

        self._name = None
        self._relay_host = None
        self._sender_domain = None

        if name is not None:
          self.name = name
        if relay_host is not None:
          self.relay_host = relay_host
        if sender_domain is not None:
          self.sender_domain = sender_domain

    @property
    def name(self):
        """
        Gets the name of this Smtp.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this Smtp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Smtp.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this Smtp.
        :type: str
        """

        self._name = name

    @property
    def relay_host(self):
        """
        Gets the relay_host of this Smtp.
        Relay server used as a forwarding point for email sent from the array

        :return: The relay_host of this Smtp.
        :rtype: str
        """
        return self._relay_host

    @relay_host.setter
    def relay_host(self, relay_host):
        """
        Sets the relay_host of this Smtp.
        Relay server used as a forwarding point for email sent from the array

        :param relay_host: The relay_host of this Smtp.
        :type: str
        """

        self._relay_host = relay_host

    @property
    def sender_domain(self):
        """
        Gets the sender_domain of this Smtp.
        Domain name appended to alert email messages

        :return: The sender_domain of this Smtp.
        :rtype: str
        """
        return self._sender_domain

    @sender_domain.setter
    def sender_domain(self, sender_domain):
        """
        Sets the sender_domain of this Smtp.
        Domain name appended to alert email messages

        :param sender_domain: The sender_domain of this Smtp.
        :type: str
        """

        self._sender_domain = sender_domain

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
        if not isinstance(other, Smtp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
