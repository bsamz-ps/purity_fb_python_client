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


class SnmpAgent(object):
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
        'id': 'str',
        'name': 'str',
        'engine_id': 'str',
        'version': 'str',
        'v2c': 'SnmpV2c',
        'v3': 'SnmpV3'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'engine_id': 'engine_id',
        'version': 'version',
        'v2c': 'v2c',
        'v3': 'v3'
    }

    def __init__(self, id=None, name=None, engine_id=None, version=None, v2c=None, v3=None):
        """
        SnmpAgent - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._engine_id = None
        self._version = None
        self._v2c = None
        self._v3 = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if engine_id is not None:
          self.engine_id = engine_id
        if version is not None:
          self.version = version
        if v2c is not None:
          self.v2c = v2c
        if v3 is not None:
          self.v3 = v3

    @property
    def id(self):
        """
        Gets the id of this SnmpAgent.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this SnmpAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SnmpAgent.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this SnmpAgent.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SnmpAgent.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this SnmpAgent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnmpAgent.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this SnmpAgent.
        :type: str
        """

        self._name = name

    @property
    def engine_id(self):
        """
        Gets the engine_id of this SnmpAgent.
        An SNMP engine's administratively-unique identifier.

        :return: The engine_id of this SnmpAgent.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """
        Sets the engine_id of this SnmpAgent.
        An SNMP engine's administratively-unique identifier.

        :param engine_id: The engine_id of this SnmpAgent.
        :type: str
        """
        if engine_id is not None and len(engine_id) > 32:
            raise ValueError("Invalid value for `engine_id`, length must be less than or equal to `32`")

        self._engine_id = engine_id

    @property
    def version(self):
        """
        Gets the version of this SnmpAgent.
        Version of the SNMP protocol to be used by an SNMP manager in communications with Purity's SNMP agent. Valid values are `v2c` and `v3`.

        :return: The version of this SnmpAgent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SnmpAgent.
        Version of the SNMP protocol to be used by an SNMP manager in communications with Purity's SNMP agent. Valid values are `v2c` and `v3`.

        :param version: The version of this SnmpAgent.
        :type: str
        """

        self._version = version

    @property
    def v2c(self):
        """
        Gets the v2c of this SnmpAgent.

        :return: The v2c of this SnmpAgent.
        :rtype: SnmpV2c
        """
        return self._v2c

    @v2c.setter
    def v2c(self, v2c):
        """
        Sets the v2c of this SnmpAgent.

        :param v2c: The v2c of this SnmpAgent.
        :type: SnmpV2c
        """

        self._v2c = v2c

    @property
    def v3(self):
        """
        Gets the v3 of this SnmpAgent.

        :return: The v3 of this SnmpAgent.
        :rtype: SnmpV3
        """
        return self._v3

    @v3.setter
    def v3(self, v3):
        """
        Sets the v3 of this SnmpAgent.

        :param v3: The v3 of this SnmpAgent.
        :type: SnmpV3
        """

        self._v3 = v3

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
        if not isinstance(other, SnmpAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
