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


class ObjectStoreAccessKey(object):
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
        'created': 'int',
        'user': 'Reference',
        'enabled': 'bool',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'user': 'user',
        'enabled': 'enabled',
        'secret_access_key': 'secret_access_key'
    }

    def __init__(self, name=None, created=None, user=None, enabled=None, secret_access_key=None):
        """
        ObjectStoreAccessKey - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._user = None
        self._enabled = None
        self._secret_access_key = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if user is not None:
          self.user = user
        if enabled is not None:
          self.enabled = enabled
        if secret_access_key is not None:
          self.secret_access_key = secret_access_key

    @property
    def name(self):
        """
        Gets the name of this ObjectStoreAccessKey.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this ObjectStoreAccessKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectStoreAccessKey.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this ObjectStoreAccessKey.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this ObjectStoreAccessKey.
        creation timestamp of the object

        :return: The created of this ObjectStoreAccessKey.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ObjectStoreAccessKey.
        creation timestamp of the object

        :param created: The created of this ObjectStoreAccessKey.
        :type: int
        """

        self._created = created

    @property
    def user(self):
        """
        Gets the user of this ObjectStoreAccessKey.
        reference of the associated user

        :return: The user of this ObjectStoreAccessKey.
        :rtype: Reference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this ObjectStoreAccessKey.
        reference of the associated user

        :param user: The user of this ObjectStoreAccessKey.
        :type: Reference
        """

        self._user = user

    @property
    def enabled(self):
        """
        Gets the enabled of this ObjectStoreAccessKey.
        is the access key enabled? Default is true

        :return: The enabled of this ObjectStoreAccessKey.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ObjectStoreAccessKey.
        is the access key enabled? Default is true

        :param enabled: The enabled of this ObjectStoreAccessKey.
        :type: bool
        """

        self._enabled = enabled

    @property
    def secret_access_key(self):
        """
        Gets the secret_access_key of this ObjectStoreAccessKey.
        the secret access key, only populated on creation

        :return: The secret_access_key of this ObjectStoreAccessKey.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """
        Sets the secret_access_key of this ObjectStoreAccessKey.
        the secret access key, only populated on creation

        :param secret_access_key: The secret_access_key of this ObjectStoreAccessKey.
        :type: str
        """

        self._secret_access_key = secret_access_key

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
        if not isinstance(other, ObjectStoreAccessKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
