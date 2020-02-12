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


class ArrayHttpPerformance(object):
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
        'read_dirs_per_sec': 'int',
        'write_dirs_per_sec': 'int',
        'read_files_per_sec': 'int',
        'write_files_per_sec': 'int',
        'others_per_sec': 'int',
        'usec_per_read_dir_op': 'int',
        'usec_per_write_dir_op': 'int',
        'usec_per_read_file_op': 'int',
        'usec_per_write_file_op': 'int',
        'usec_per_other_op': 'int',
        'time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'read_dirs_per_sec': 'read_dirs_per_sec',
        'write_dirs_per_sec': 'write_dirs_per_sec',
        'read_files_per_sec': 'read_files_per_sec',
        'write_files_per_sec': 'write_files_per_sec',
        'others_per_sec': 'others_per_sec',
        'usec_per_read_dir_op': 'usec_per_read_dir_op',
        'usec_per_write_dir_op': 'usec_per_write_dir_op',
        'usec_per_read_file_op': 'usec_per_read_file_op',
        'usec_per_write_file_op': 'usec_per_write_file_op',
        'usec_per_other_op': 'usec_per_other_op',
        'time': 'time'
    }

    def __init__(self, name=None, read_dirs_per_sec=None, write_dirs_per_sec=None, read_files_per_sec=None, write_files_per_sec=None, others_per_sec=None, usec_per_read_dir_op=None, usec_per_write_dir_op=None, usec_per_read_file_op=None, usec_per_write_file_op=None, usec_per_other_op=None, time=None):
        """
        ArrayHttpPerformance - a model defined in Swagger
        """

        self._name = None
        self._read_dirs_per_sec = None
        self._write_dirs_per_sec = None
        self._read_files_per_sec = None
        self._write_files_per_sec = None
        self._others_per_sec = None
        self._usec_per_read_dir_op = None
        self._usec_per_write_dir_op = None
        self._usec_per_read_file_op = None
        self._usec_per_write_file_op = None
        self._usec_per_other_op = None
        self._time = None

        if name is not None:
          self.name = name
        if read_dirs_per_sec is not None:
          self.read_dirs_per_sec = read_dirs_per_sec
        if write_dirs_per_sec is not None:
          self.write_dirs_per_sec = write_dirs_per_sec
        if read_files_per_sec is not None:
          self.read_files_per_sec = read_files_per_sec
        if write_files_per_sec is not None:
          self.write_files_per_sec = write_files_per_sec
        if others_per_sec is not None:
          self.others_per_sec = others_per_sec
        if usec_per_read_dir_op is not None:
          self.usec_per_read_dir_op = usec_per_read_dir_op
        if usec_per_write_dir_op is not None:
          self.usec_per_write_dir_op = usec_per_write_dir_op
        if usec_per_read_file_op is not None:
          self.usec_per_read_file_op = usec_per_read_file_op
        if usec_per_write_file_op is not None:
          self.usec_per_write_file_op = usec_per_write_file_op
        if usec_per_other_op is not None:
          self.usec_per_other_op = usec_per_other_op
        if time is not None:
          self.time = time

    @property
    def name(self):
        """
        Gets the name of this ArrayHttpPerformance.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this ArrayHttpPerformance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ArrayHttpPerformance.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this ArrayHttpPerformance.
        :type: str
        """

        self._name = name

    @property
    def read_dirs_per_sec(self):
        """
        Gets the read_dirs_per_sec of this ArrayHttpPerformance.
        Read directories requests processed per second

        :return: The read_dirs_per_sec of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._read_dirs_per_sec

    @read_dirs_per_sec.setter
    def read_dirs_per_sec(self, read_dirs_per_sec):
        """
        Sets the read_dirs_per_sec of this ArrayHttpPerformance.
        Read directories requests processed per second

        :param read_dirs_per_sec: The read_dirs_per_sec of this ArrayHttpPerformance.
        :type: int
        """
        if read_dirs_per_sec is not None and read_dirs_per_sec < 0:
            raise ValueError("Invalid value for `read_dirs_per_sec`, must be a value greater than or equal to `0`")

        self._read_dirs_per_sec = read_dirs_per_sec

    @property
    def write_dirs_per_sec(self):
        """
        Gets the write_dirs_per_sec of this ArrayHttpPerformance.
        Write directories requests processed per second

        :return: The write_dirs_per_sec of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._write_dirs_per_sec

    @write_dirs_per_sec.setter
    def write_dirs_per_sec(self, write_dirs_per_sec):
        """
        Sets the write_dirs_per_sec of this ArrayHttpPerformance.
        Write directories requests processed per second

        :param write_dirs_per_sec: The write_dirs_per_sec of this ArrayHttpPerformance.
        :type: int
        """
        if write_dirs_per_sec is not None and write_dirs_per_sec < 0:
            raise ValueError("Invalid value for `write_dirs_per_sec`, must be a value greater than or equal to `0`")

        self._write_dirs_per_sec = write_dirs_per_sec

    @property
    def read_files_per_sec(self):
        """
        Gets the read_files_per_sec of this ArrayHttpPerformance.
        Read files requests processed per second

        :return: The read_files_per_sec of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._read_files_per_sec

    @read_files_per_sec.setter
    def read_files_per_sec(self, read_files_per_sec):
        """
        Sets the read_files_per_sec of this ArrayHttpPerformance.
        Read files requests processed per second

        :param read_files_per_sec: The read_files_per_sec of this ArrayHttpPerformance.
        :type: int
        """
        if read_files_per_sec is not None and read_files_per_sec < 0:
            raise ValueError("Invalid value for `read_files_per_sec`, must be a value greater than or equal to `0`")

        self._read_files_per_sec = read_files_per_sec

    @property
    def write_files_per_sec(self):
        """
        Gets the write_files_per_sec of this ArrayHttpPerformance.
        Write files requests processed per second

        :return: The write_files_per_sec of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._write_files_per_sec

    @write_files_per_sec.setter
    def write_files_per_sec(self, write_files_per_sec):
        """
        Sets the write_files_per_sec of this ArrayHttpPerformance.
        Write files requests processed per second

        :param write_files_per_sec: The write_files_per_sec of this ArrayHttpPerformance.
        :type: int
        """
        if write_files_per_sec is not None and write_files_per_sec < 0:
            raise ValueError("Invalid value for `write_files_per_sec`, must be a value greater than or equal to `0`")

        self._write_files_per_sec = write_files_per_sec

    @property
    def others_per_sec(self):
        """
        Gets the others_per_sec of this ArrayHttpPerformance.
        Other operations processed per second

        :return: The others_per_sec of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._others_per_sec

    @others_per_sec.setter
    def others_per_sec(self, others_per_sec):
        """
        Sets the others_per_sec of this ArrayHttpPerformance.
        Other operations processed per second

        :param others_per_sec: The others_per_sec of this ArrayHttpPerformance.
        :type: int
        """
        if others_per_sec is not None and others_per_sec < 0:
            raise ValueError("Invalid value for `others_per_sec`, must be a value greater than or equal to `0`")

        self._others_per_sec = others_per_sec

    @property
    def usec_per_read_dir_op(self):
        """
        Gets the usec_per_read_dir_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a read directory request

        :return: The usec_per_read_dir_op of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._usec_per_read_dir_op

    @usec_per_read_dir_op.setter
    def usec_per_read_dir_op(self, usec_per_read_dir_op):
        """
        Sets the usec_per_read_dir_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a read directory request

        :param usec_per_read_dir_op: The usec_per_read_dir_op of this ArrayHttpPerformance.
        :type: int
        """
        if usec_per_read_dir_op is not None and usec_per_read_dir_op < 0:
            raise ValueError("Invalid value for `usec_per_read_dir_op`, must be a value greater than or equal to `0`")

        self._usec_per_read_dir_op = usec_per_read_dir_op

    @property
    def usec_per_write_dir_op(self):
        """
        Gets the usec_per_write_dir_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a write directory request

        :return: The usec_per_write_dir_op of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._usec_per_write_dir_op

    @usec_per_write_dir_op.setter
    def usec_per_write_dir_op(self, usec_per_write_dir_op):
        """
        Sets the usec_per_write_dir_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a write directory request

        :param usec_per_write_dir_op: The usec_per_write_dir_op of this ArrayHttpPerformance.
        :type: int
        """
        if usec_per_write_dir_op is not None and usec_per_write_dir_op < 0:
            raise ValueError("Invalid value for `usec_per_write_dir_op`, must be a value greater than or equal to `0`")

        self._usec_per_write_dir_op = usec_per_write_dir_op

    @property
    def usec_per_read_file_op(self):
        """
        Gets the usec_per_read_file_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a read file request

        :return: The usec_per_read_file_op of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._usec_per_read_file_op

    @usec_per_read_file_op.setter
    def usec_per_read_file_op(self, usec_per_read_file_op):
        """
        Sets the usec_per_read_file_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a read file request

        :param usec_per_read_file_op: The usec_per_read_file_op of this ArrayHttpPerformance.
        :type: int
        """
        if usec_per_read_file_op is not None and usec_per_read_file_op < 0:
            raise ValueError("Invalid value for `usec_per_read_file_op`, must be a value greater than or equal to `0`")

        self._usec_per_read_file_op = usec_per_read_file_op

    @property
    def usec_per_write_file_op(self):
        """
        Gets the usec_per_write_file_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a write file request

        :return: The usec_per_write_file_op of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._usec_per_write_file_op

    @usec_per_write_file_op.setter
    def usec_per_write_file_op(self, usec_per_write_file_op):
        """
        Sets the usec_per_write_file_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process a write file request

        :param usec_per_write_file_op: The usec_per_write_file_op of this ArrayHttpPerformance.
        :type: int
        """
        if usec_per_write_file_op is not None and usec_per_write_file_op < 0:
            raise ValueError("Invalid value for `usec_per_write_file_op`, must be a value greater than or equal to `0`")

        self._usec_per_write_file_op = usec_per_write_file_op

    @property
    def usec_per_other_op(self):
        """
        Gets the usec_per_other_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process other operations

        :return: The usec_per_other_op of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._usec_per_other_op

    @usec_per_other_op.setter
    def usec_per_other_op(self, usec_per_other_op):
        """
        Sets the usec_per_other_op of this ArrayHttpPerformance.
        Average time, measured in microseconds, that the array takes to process other operations

        :param usec_per_other_op: The usec_per_other_op of this ArrayHttpPerformance.
        :type: int
        """
        if usec_per_other_op is not None and usec_per_other_op < 0:
            raise ValueError("Invalid value for `usec_per_other_op`, must be a value greater than or equal to `0`")

        self._usec_per_other_op = usec_per_other_op

    @property
    def time(self):
        """
        Gets the time of this ArrayHttpPerformance.
        Sample time in milliseconds since UNIX epoch

        :return: The time of this ArrayHttpPerformance.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this ArrayHttpPerformance.
        Sample time in milliseconds since UNIX epoch

        :param time: The time of this ArrayHttpPerformance.
        :type: int
        """

        self._time = time

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
        if not isinstance(other, ArrayHttpPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
