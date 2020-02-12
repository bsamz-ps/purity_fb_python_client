# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.8 Python SDK

    Pure Storage FlashBlade REST 1.8 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.8
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TestResult(object):
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
        'component_address': 'str',
        'component_name': 'str',
        'description': 'str',
        'destination': 'str',
        'enabled': 'bool',
        'resource': 'str',
        'result_details': 'str',
        'success': 'bool',
        'test_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'component_address': 'component_address',
        'component_name': 'component_name',
        'description': 'description',
        'destination': 'destination',
        'enabled': 'enabled',
        'resource': 'resource',
        'result_details': 'result_details',
        'success': 'success',
        'test_type': 'test_type'
    }

    def __init__(self, name=None, component_address=None, component_name=None, description=None, destination=None, enabled=None, resource=None, result_details=None, success=None, test_type=None):
        """
        TestResult - a model defined in Swagger
        """

        self._name = None
        self._component_address = None
        self._component_name = None
        self._description = None
        self._destination = None
        self._enabled = None
        self._resource = None
        self._result_details = None
        self._success = None
        self._test_type = None

        if name is not None:
          self.name = name
        if component_address is not None:
          self.component_address = component_address
        if component_name is not None:
          self.component_name = component_name
        if description is not None:
          self.description = description
        if destination is not None:
          self.destination = destination
        if enabled is not None:
          self.enabled = enabled
        if resource is not None:
          self.resource = resource
        if result_details is not None:
          self.result_details = result_details
        if success is not None:
          self.success = success
        if test_type is not None:
          self.test_type = test_type

    @property
    def name(self):
        """
        Gets the name of this TestResult.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this TestResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TestResult.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this TestResult.
        :type: str
        """

        self._name = name

    @property
    def component_address(self):
        """
        Gets the component_address of this TestResult.
        Address of the component running the test

        :return: The component_address of this TestResult.
        :rtype: str
        """
        return self._component_address

    @component_address.setter
    def component_address(self, component_address):
        """
        Sets the component_address of this TestResult.
        Address of the component running the test

        :param component_address: The component_address of this TestResult.
        :type: str
        """

        self._component_address = component_address

    @property
    def component_name(self):
        """
        Gets the component_name of this TestResult.
        Name of the component running the test

        :return: The component_name of this TestResult.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this TestResult.
        Name of the component running the test

        :param component_name: The component_name of this TestResult.
        :type: str
        """

        self._component_name = component_name

    @property
    def description(self):
        """
        Gets the description of this TestResult.
        What the test is doing

        :return: The description of this TestResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TestResult.
        What the test is doing

        :param description: The description of this TestResult.
        :type: str
        """

        self._description = description

    @property
    def destination(self):
        """
        Gets the destination of this TestResult.
        The URI of the target server being tested

        :return: The destination of this TestResult.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this TestResult.
        The URI of the target server being tested

        :param destination: The destination of this TestResult.
        :type: str
        """

        self._destination = destination

    @property
    def enabled(self):
        """
        Gets the enabled of this TestResult.
        Is the service enabled?

        :return: The enabled of this TestResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this TestResult.
        Is the service enabled?

        :param enabled: The enabled of this TestResult.
        :type: bool
        """

        self._enabled = enabled

    @property
    def resource(self):
        """
        Gets the resource of this TestResult.
        A reference to the object being tested

        :return: The resource of this TestResult.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this TestResult.
        A reference to the object being tested

        :param resource: The resource of this TestResult.
        :type: str
        """

        self._resource = resource

    @property
    def result_details(self):
        """
        Gets the result_details of this TestResult.
        Reason of test failure, if any

        :return: The result_details of this TestResult.
        :rtype: str
        """
        return self._result_details

    @result_details.setter
    def result_details(self, result_details):
        """
        Sets the result_details of this TestResult.
        Reason of test failure, if any

        :param result_details: The result_details of this TestResult.
        :type: str
        """

        self._result_details = result_details

    @property
    def success(self):
        """
        Gets the success of this TestResult.
        Did the test succeed?

        :return: The success of this TestResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this TestResult.
        Did the test succeed?

        :param success: The success of this TestResult.
        :type: bool
        """

        self._success = success

    @property
    def test_type(self):
        """
        Gets the test_type of this TestResult.
        The type of the test. Possible values are phonehome, phonehome-ping, remote-assist, directory-service, directory-service-connecting, directory-service-binding, directory-service-group-searching, and directory-service-uri-searching.

        :return: The test_type of this TestResult.
        :rtype: str
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """
        Sets the test_type of this TestResult.
        The type of the test. Possible values are phonehome, phonehome-ping, remote-assist, directory-service, directory-service-connecting, directory-service-binding, directory-service-group-searching, and directory-service-uri-searching.

        :param test_type: The test_type of this TestResult.
        :type: str
        """

        self._test_type = test_type

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
        if not isinstance(other, TestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
