# Copyright (c) 2014 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from kmip.core.enums import KeyFormatType
from kmip.core.enums import ObjectType
from kmip.core.enums import Operation
from kmip.core.enums import ResultStatus

from kmip.core.objects import TemplateAttribute

from kmip.demos import utils

from kmip.services.kmip_client import KMIPProxy

import logging
import sys


if __name__ == '__main__':
    logger = utils.build_console_logger(logging.INFO)

    parser = utils.build_cli_parser(Operation.REGISTER)
    opts, args = parser.parse_args(sys.argv[1:])

    username = opts.username
    password = opts.password
    config = opts.config
    object_type = opts.type
    format_type = opts.format

    # Exit early if the arguments are not specified
    object_type = getattr(ObjectType, object_type, None)
    if object_type is None:
        logger.error("Invalid object type specified; exiting early from demo")
        sys.exit()

    key_format_type = getattr(KeyFormatType, format_type, None)
    if key_format_type is None:
        logger.error(
            "Invalid key format type specified; exiting early from demo")

    # Create the template attribute for the secret and then build the secret
    usage_mask = utils.build_cryptographic_usage_mask(logger, object_type)
    attributes = [usage_mask]
    template_attribute = TemplateAttribute(attributes=attributes)

    secret = utils.build_object(logger, object_type, key_format_type)

    # Build the client, connect to the server, register the secret, and
    # disconnect from the server
    client = KMIPProxy(
        host='172.21.0.1',
        port=5696,
        certfile='/etc/pykmip/certs/server.crt',
        keyfile='/etc/pykmip/certs/server.key',
        cert_reqs='CERT_REQUIRED',
        ssl_version='PROTOCOL_SSLv23',
        username='user',
        password='password',
        config='client'
    )
    print (client.host_list)
    #client.open()
    #result = client.register(object_type, template_attribute, secret)
    #print (result)
    """
    client.close()

    # Display operation results
    logger.info('register() result status: {0}'.format(
        result.result_status.value))

    if result.result_status.value == ResultStatus.SUCCESS:
        logger.info('registered UUID: {0}'.format(result.uuid.value))
        logger.info('registered template attribute: {0}'.
                    format(result.template_attribute))
    else:
        logger.info('register() result reason: {0}'.format(
            result.result_reason.value))
        logger.info('register() result message: {0}'.format(
            result.result_message.value))
    """
