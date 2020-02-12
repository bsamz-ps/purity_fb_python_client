# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.5 Python SDK

    Pure Storage FlashBlade REST 1.5 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.5
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Bucket(object):
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
        'space': 'Space',
        'account': 'Reference',
        'destroyed': 'bool',
        'time_remaining': 'int',
        'object_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'space': 'space',
        'account': 'account',
        'destroyed': 'destroyed',
        'time_remaining': 'time_remaining',
        'object_count': 'object_count'
    }

    def __init__(self, name=None, created=None, space=None, account=None, destroyed=None, time_remaining=None, object_count=None):
        """
        Bucket - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._space = None
        self._account = None
        self._destroyed = None
        self._time_remaining = None
        self._object_count = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if space is not None:
          self.space = space
        if account is not None:
          self.account = account
        if destroyed is not None:
          self.destroyed = destroyed
        if time_remaining is not None:
          self.time_remaining = time_remaining
        if object_count is not None:
          self.object_count = object_count

    @property
    def name(self):
        """
        Gets the name of this Bucket.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this Bucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Bucket.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this Bucket.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this Bucket.
        creation timestamp of the object

        :return: The created of this Bucket.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Bucket.
        creation timestamp of the object

        :param created: The created of this Bucket.
        :type: int
        """

        self._created = created

    @property
    def space(self):
        """
        Gets the space of this Bucket.
        the space specification of the bucket

        :return: The space of this Bucket.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this Bucket.
        the space specification of the bucket

        :param space: The space of this Bucket.
        :type: Space
        """

        self._space = space

    @property
    def account(self):
        """
        Gets the account of this Bucket.
        the account of the bucket

        :return: The account of this Bucket.
        :rtype: Reference
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Bucket.
        the account of the bucket

        :param account: The account of this Bucket.
        :type: Reference
        """

        self._account = account

    @property
    def destroyed(self):
        """
        Gets the destroyed of this Bucket.
        is the bucket destroyed? False by default. Modifiable.

        :return: The destroyed of this Bucket.
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """
        Sets the destroyed of this Bucket.
        is the bucket destroyed? False by default. Modifiable.

        :param destroyed: The destroyed of this Bucket.
        :type: bool
        """

        self._destroyed = destroyed

    @property
    def time_remaining(self):
        """
        Gets the time_remaining of this Bucket.
        time in milliseconds before the bucket is eradicated. Null if not destroyed.

        :return: The time_remaining of this Bucket.
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """
        Sets the time_remaining of this Bucket.
        time in milliseconds before the bucket is eradicated. Null if not destroyed.

        :param time_remaining: The time_remaining of this Bucket.
        :type: int
        """

        self._time_remaining = time_remaining

    @property
    def object_count(self):
        """
        Gets the object_count of this Bucket.
        the number of object within the bucket.

        :return: The object_count of this Bucket.
        :rtype: int
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """
        Sets the object_count of this Bucket.
        the number of object within the bucket.

        :param object_count: The object_count of this Bucket.
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
        if not isinstance(other, Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
