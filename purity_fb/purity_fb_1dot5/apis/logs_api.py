# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.5 Python SDK

    Pure Storage FlashBlade REST 1.5 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.5
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class LogsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list_logs(self, **kwargs):
        """
        Download logs
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_logs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int start_time: Time to start sample in milliseconds since epoch.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_logs_with_http_info(**kwargs)
        else:
            (data) = self.list_logs_with_http_info(**kwargs)
            return data

    def list_logs_with_http_info(self, **kwargs):
        """
        Download logs
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_logs_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int start_time: Time to start sample in milliseconds since epoch.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_time', 'start_time']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_logs" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.5/logs', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
