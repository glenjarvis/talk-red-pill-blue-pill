#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""AWS Specific library for BayPIGgies presentation

13-Dec, 2012

A screencast has been created that walks through this script and
explains how it works:

https://docs.google.com/file/d/0B1tPdExbbaW0dDdUZVUtd3I0aFU/edit

Before you run this script, you will need to get your security
credentials and place them in the private.py file.
"""

from __future__ import print_function
import datetime

from boto import connect_cloudwatch

import private

c = connect_cloudwatch(
    aws_access_key_id=private.MY_AWS_ACCESS_KEY,
    aws_secret_access_key=private.MY_AWS_SECRET_ACCESS_KEY,
    debug=1)


end = datetime.datetime.now()
start = end - datetime.timedelta(hours=7)

for m in c.list_metrics():
    if str(m) == 'Metric:EstimatedCharges':
        service_name = m.dimensions.get(u'ServiceName', None)
        if service_name is not None:
            service_name = service_name[0]
        else:
            service_name = "Total"
        currency = m.dimensions.get(u'Currency', '???')[0]
        datapoints = m.query(
            start, end,
            [u'Maximum', u'Sum', u'Minimum', u'Average', u'SampleCount'])
        for d in datapoints:
            print("{0:25}".format(service_name),
                  d[u'Timestamp'],
                  "{0:8}{1}".format(d[u'Maximum'],
                  currency))
