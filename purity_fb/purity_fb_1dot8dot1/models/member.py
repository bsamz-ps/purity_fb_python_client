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


class Member(object):
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
        'member': 'Reference',
        'group': 'Reference'
    }

    attribute_map = {
        'member': 'member',
        'group': 'group'
    }

    def __init__(self, member=None, group=None):
        """
        Member - a model defined in Swagger
        """

        self._member = None
        self._group = None

        if member is not None:
          self.member = member
        if group is not None:
          self.group = group

    @property
    def member(self):
        """
        Gets the member of this Member.
        A reference to an object that is a member of the referenced group.

        :return: The member of this Member.
        :rtype: Reference
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this Member.
        A reference to an object that is a member of the referenced group.

        :param member: The member of this Member.
        :type: Reference
        """

        self._member = member

    @property
    def group(self):
        """
        Gets the group of this Member.
        A reference to a group object that has the referenced member object as a member.

        :return: The group of this Member.
        :rtype: Reference
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this Member.
        A reference to a group object that has the referenced member object as a member.

        :param group: The group of this Member.
        :type: Reference
        """

        self._group = group

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
