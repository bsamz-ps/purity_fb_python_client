# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.3 Python SDK

    Pure Storage FlashBlade REST 1.3 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.3
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ObjectStoreUser(object):
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
        'account': 'Reference',
        'access_keys': 'list[Reference]'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'account': 'account',
        'access_keys': 'access_keys'
    }

    def __init__(self, name=None, created=None, account=None, access_keys=None):
        """
        ObjectStoreUser - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._account = None
        self._access_keys = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if account is not None:
          self.account = account
        if access_keys is not None:
          self.access_keys = access_keys

    @property
    def name(self):
        """
        Gets the name of this ObjectStoreUser.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this ObjectStoreUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectStoreUser.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this ObjectStoreUser.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this ObjectStoreUser.
        creation timestamp of the object

        :return: The created of this ObjectStoreUser.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ObjectStoreUser.
        creation timestamp of the object

        :param created: The created of this ObjectStoreUser.
        :type: int
        """

        self._created = created

    @property
    def account(self):
        """
        Gets the account of this ObjectStoreUser.
        reference of the associated account

        :return: The account of this ObjectStoreUser.
        :rtype: Reference
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this ObjectStoreUser.
        reference of the associated account

        :param account: The account of this ObjectStoreUser.
        :type: Reference
        """

        self._account = account

    @property
    def access_keys(self):
        """
        Gets the access_keys of this ObjectStoreUser.
        references of the user's access keys

        :return: The access_keys of this ObjectStoreUser.
        :rtype: list[Reference]
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, access_keys):
        """
        Sets the access_keys of this ObjectStoreUser.
        references of the user's access keys

        :param access_keys: The access_keys of this ObjectStoreUser.
        :type: list[Reference]
        """

        self._access_keys = access_keys

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
        if not isinstance(other, ObjectStoreUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
