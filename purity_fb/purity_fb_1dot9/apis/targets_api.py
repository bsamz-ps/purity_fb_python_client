# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK. Compatible with REST API versions 1.0 - 1.9. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
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


class TargetsApi(object):
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

    def create_targets(self, target, **kwargs):
        """
        Create a new target.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_targets(target, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TargetPost target: The attribute map used to create the target. (required)
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_targets_with_http_info(target, **kwargs)
        else:
            (data) = self.create_targets_with_http_info(target, **kwargs)
            return data

    def create_targets_with_http_info(self, target, **kwargs):
        """
        Create a new target.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_targets_with_http_info(target, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TargetPost target: The attribute map used to create the target. (required)
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['target', 'names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'target' is set
        if ('target' not in params) or (params['target'] is None):
            raise ValueError("Missing the required parameter `target` when calling `create_targets`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'target' in params:
            body_params = params['target']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/targets', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TargetResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_targets(self, **kwargs):
        """
        Delete a target.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_targets(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_targets_with_http_info(**kwargs)
        else:
            (data) = self.delete_targets_with_http_info(**kwargs)
            return data

    def delete_targets_with_http_info(self, **kwargs):
        """
        Delete a target.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_targets_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_targets" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/targets', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_targets(self, **kwargs):
        """
        List targets.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_targets(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param int limit: limit, should be >= 0
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :param str sort: The way to order the results.
        :param int start: start
        :param str token: token
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_targets_with_http_info(**kwargs)
        else:
            (data) = self.list_targets_with_http_info(**kwargs)
            return data

    def list_targets_with_http_info(self, **kwargs):
        """
        List targets.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_targets_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param int limit: limit, should be >= 0
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :param str sort: The way to order the results.
        :param int start: start
        :param str token: token
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'ids', 'limit', 'names', 'sort', 'start', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_targets" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/targets', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TargetResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_targets_performance_replication(self, **kwargs):
        """
        List instant or historical target replication performance.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_targets_performance_replication(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param str filter: The filter to be used for query.
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param int limit: limit, should be >= 0
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :param int resolution: sample frequency in milliseconds
        :param str sort: The way to order the results.
        :param int start: start
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param str token: token
        :param bool total_only: Return only the total object.
        :param str type: to sample space of either file systems, object store, or all
        :return: PerformanceReplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_targets_performance_replication_with_http_info(**kwargs)
        else:
            (data) = self.list_targets_performance_replication_with_http_info(**kwargs)
            return data

    def list_targets_performance_replication_with_http_info(self, **kwargs):
        """
        List instant or historical target replication performance.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_targets_performance_replication_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param str filter: The filter to be used for query.
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param int limit: limit, should be >= 0
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :param int resolution: sample frequency in milliseconds
        :param str sort: The way to order the results.
        :param int start: start
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param str token: token
        :param bool total_only: Return only the total object.
        :param str type: to sample space of either file systems, object store, or all
        :return: PerformanceReplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_time', 'filter', 'ids', 'limit', 'names', 'resolution', 'sort', 'start', 'start_time', 'token', 'total_only', 'type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_targets_performance_replication" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'total_only' in params:
            query_params.append(('total_only', params['total_only']))
        if 'type' in params:
            query_params.append(('type', params['type']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/targets/performance/replication', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PerformanceReplicationResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_targets(self, target, **kwargs):
        """
        Update an existing target.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_targets(target, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Target target: The attribute map used to update the target. (required)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_targets_with_http_info(target, **kwargs)
        else:
            (data) = self.update_targets_with_http_info(target, **kwargs)
            return data

    def update_targets_with_http_info(self, target, **kwargs):
        """
        Update an existing target.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_targets_with_http_info(target, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Target target: The attribute map used to update the target. (required)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['target', 'ids', 'names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'target' is set
        if ('target' not in params) or (params['target'] is None):
            raise ValueError("Missing the required parameter `target` when calling `update_targets`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'target' in params:
            body_params = params['target']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/targets', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TargetResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)