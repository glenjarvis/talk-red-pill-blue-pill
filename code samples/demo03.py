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

from boto.ec2.connection import EC2Connection

import private

connection = EC2Connection(
    aws_access_key_id=private.MY_AWS_ACCESS_KEY,
    aws_secret_access_key=private.MY_AWS_SECRET_ACCESS_KEY)

NAME = "BayPIGgies_code_demo01"
STOPPED = u'stopped'
RUNNING = u'running'
TERMINATED = u'terminated'


def get_our_instance():
    """Modifying the previous demonstration to be a function"""
    this_demo_instance = None
    for reservation in connection.get_all_instances():
        for instance in reservation.instances:
            name = instance.tags.get('Name', None)
            if instance.state == RUNNING and name == NAME:
                this_demo_instance = instance
    return this_demo_instance


def loop_until(instance, state):

    """From demo01"""

    while instance.state != state:
        print("State of our instance: {0}/{1}".format(
            instance.state, datetime.datetime.now()))
        instance.update()


demo_instance = get_our_instance()

print("\n\nOur instance")
print("=" * 13)

print(demo_instance)
if demo_instance is None:
    print("We're not running")
else:
    demo_instance.stop()
    loop_until(demo_instance, STOPPED)
