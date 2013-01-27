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

from boto.ec2.connection import EC2Connection

import private

connection = EC2Connection(
    aws_access_key_id=private.MY_AWS_ACCESS_KEY,
    aws_secret_access_key=private.MY_AWS_SECRET_ACCESS_KEY)

NAME = "BayPIGgies_code_demo01"
STOPPED = u'stopped'
RUNNING = u'running'
TERMINATED = u'terminated'

demo_instance = None

for reservation in connection.get_all_instances():
    for instance in reservation.instances:
        name = instance.tags.get('Name', None)
        if instance.state == RUNNING and name == NAME:
            demo_instance = instance
        print(reservation, instance, "{0:25}".format(name),  instance.state)

print("\n\nOur instance")
print("=" * 13)

print(demo_instance)
