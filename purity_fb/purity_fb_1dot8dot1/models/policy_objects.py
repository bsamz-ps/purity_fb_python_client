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


class PolicyObjects(object):
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
        'policy': 'PolicyReferenceWithId',
        'member': 'PolicyReferenceWithId'
    }

    attribute_map = {
        'policy': 'policy',
        'member': 'member'
    }

    def __init__(self, policy=None, member=None):
        """
        PolicyObjects - a model defined in Swagger
        """

        self._policy = None
        self._member = None

        if policy is not None:
          self.policy = policy
        if member is not None:
          self.member = member

    @property
    def policy(self):
        """
        Gets the policy of this PolicyObjects.

        :return: The policy of this PolicyObjects.
        :rtype: PolicyReferenceWithId
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this PolicyObjects.

        :param policy: The policy of this PolicyObjects.
        :type: PolicyReferenceWithId
        """

        self._policy = policy

    @property
    def member(self):
        """
        Gets the member of this PolicyObjects.

        :return: The member of this PolicyObjects.
        :rtype: PolicyReferenceWithId
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this PolicyObjects.

        :param member: The member of this PolicyObjects.
        :type: PolicyReferenceWithId
        """

        self._member = member

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
        if not isinstance(other, PolicyObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
