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


class FileSystemSnapshot(object):
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
        'suffix': 'str',
        'source': 'str',
        'destroyed': 'bool',
        'source_destroyed': 'bool',
        'time_remaining': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'suffix': 'suffix',
        'source': 'source',
        'destroyed': 'destroyed',
        'source_destroyed': 'source_destroyed',
        'time_remaining': 'time_remaining'
    }

    def __init__(self, name=None, created=None, suffix=None, source=None, destroyed=None, source_destroyed=None, time_remaining=None):
        """
        FileSystemSnapshot - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._suffix = None
        self._source = None
        self._destroyed = None
        self._source_destroyed = None
        self._time_remaining = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if suffix is not None:
          self.suffix = suffix
        if source is not None:
          self.source = source
        if destroyed is not None:
          self.destroyed = destroyed
        if source_destroyed is not None:
          self.source_destroyed = source_destroyed
        if time_remaining is not None:
          self.time_remaining = time_remaining

    @property
    def name(self):
        """
        Gets the name of this FileSystemSnapshot.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this FileSystemSnapshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileSystemSnapshot.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this FileSystemSnapshot.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this FileSystemSnapshot.
        creation timestamp of the object

        :return: The created of this FileSystemSnapshot.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this FileSystemSnapshot.
        creation timestamp of the object

        :param created: The created of this FileSystemSnapshot.
        :type: int
        """

        self._created = created

    @property
    def suffix(self):
        """
        Gets the suffix of this FileSystemSnapshot.
        the suffix of the snapshot, e.g., snap1

        :return: The suffix of this FileSystemSnapshot.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this FileSystemSnapshot.
        the suffix of the snapshot, e.g., snap1

        :param suffix: The suffix of this FileSystemSnapshot.
        :type: str
        """

        self._suffix = suffix

    @property
    def source(self):
        """
        Gets the source of this FileSystemSnapshot.
        the name of the source file system

        :return: The source of this FileSystemSnapshot.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this FileSystemSnapshot.
        the name of the source file system

        :param source: The source of this FileSystemSnapshot.
        :type: str
        """

        self._source = source

    @property
    def destroyed(self):
        """
        Gets the destroyed of this FileSystemSnapshot.
        is the file system snapshot destroyed? False by default.

        :return: The destroyed of this FileSystemSnapshot.
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """
        Sets the destroyed of this FileSystemSnapshot.
        is the file system snapshot destroyed? False by default.

        :param destroyed: The destroyed of this FileSystemSnapshot.
        :type: bool
        """

        self._destroyed = destroyed

    @property
    def source_destroyed(self):
        """
        Gets the source_destroyed of this FileSystemSnapshot.
        is the source file system destroyed?

        :return: The source_destroyed of this FileSystemSnapshot.
        :rtype: bool
        """
        return self._source_destroyed

    @source_destroyed.setter
    def source_destroyed(self, source_destroyed):
        """
        Sets the source_destroyed of this FileSystemSnapshot.
        is the source file system destroyed?

        :param source_destroyed: The source_destroyed of this FileSystemSnapshot.
        :type: bool
        """

        self._source_destroyed = source_destroyed

    @property
    def time_remaining(self):
        """
        Gets the time_remaining of this FileSystemSnapshot.
        time in milliseconds before the file system snapshot is eradicated. Null if not destroyed.

        :return: The time_remaining of this FileSystemSnapshot.
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """
        Sets the time_remaining of this FileSystemSnapshot.
        time in milliseconds before the file system snapshot is eradicated. Null if not destroyed.

        :param time_remaining: The time_remaining of this FileSystemSnapshot.
        :type: int
        """

        self._time_remaining = time_remaining

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
        if not isinstance(other, FileSystemSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
