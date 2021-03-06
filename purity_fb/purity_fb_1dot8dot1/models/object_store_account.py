# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.8.1 Python SDK

    Pure Storage FlashBlade REST 1.8.1 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.8.1
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ObjectStoreAccount(object):
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
        'id': 'str',
        'space': 'Space',
        'object_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'id': 'id',
        'space': 'space',
        'object_count': 'object_count'
    }

    def __init__(self, name=None, created=None, id=None, space=None, object_count=None):
        """
        ObjectStoreAccount - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._id = None
        self._space = None
        self._object_count = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if id is not None:
          self.id = id
        if space is not None:
          self.space = space
        if object_count is not None:
          self.object_count = object_count

    @property
    def name(self):
        """
        Gets the name of this ObjectStoreAccount.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this ObjectStoreAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectStoreAccount.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this ObjectStoreAccount.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this ObjectStoreAccount.
        creation timestamp of the object

        :return: The created of this ObjectStoreAccount.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ObjectStoreAccount.
        creation timestamp of the object

        :param created: The created of this ObjectStoreAccount.
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this ObjectStoreAccount.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this ObjectStoreAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ObjectStoreAccount.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this ObjectStoreAccount.
        :type: str
        """

        self._id = id

    @property
    def space(self):
        """
        Gets the space of this ObjectStoreAccount.
        The space specification of the object store account.

        :return: The space of this ObjectStoreAccount.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this ObjectStoreAccount.
        The space specification of the object store account.

        :param space: The space of this ObjectStoreAccount.
        :type: Space
        """

        self._space = space

    @property
    def object_count(self):
        """
        Gets the object_count of this ObjectStoreAccount.
        The number of object within the account.

        :return: The object_count of this ObjectStoreAccount.
        :rtype: int
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """
        Sets the object_count of this ObjectStoreAccount.
        The number of object within the account.

        :param object_count: The object_count of this ObjectStoreAccount.
        :type: int
        """

        self._object_count = object_count

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
        if not isinstance(other, ObjectStoreAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
