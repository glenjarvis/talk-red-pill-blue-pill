#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""BayPIGgies/MeetUp presentation: Starting an instance via a script

13-Dec, 2012

This script is a bare-bones script that demonstrates how to start an AWS
instance. Be warned that each time you run this script, an instance will
be created (if things go well).

A screencast has been created that walks through this script and
explains how it works:

https://docs.google.com/file/d/0B1tPdExbbaW0dDdUZVUtd3I0aFU/edit

Before you run this script, you will need to get your security
credentials and place them in the private.py file.
"""

from boto.ec2.connection import EC2Connection
import time

import private

NAME = "BayPIGgies_code_demo01"
AMI = 'ami-1624987f'
SIZE = 't1.micro'
KEY_NAME = "aws_baypiggies_demo"
FIREWALL = "baypiggies_demo"

connection = EC2Connection(
    aws_access_key_id=private.MY_AWS_ACCESS_KEY,
    aws_secret_access_key=private.MY_AWS_SECRET_ACCESS_KEY)

reservation = connection.run_instances(
    AMI,
    min_count=1,
    max_count=1,
    key_name=KEY_NAME,
    security_groups=[FIREWALL]
)

# Let's add a variable to the reservation
while not len(reservation.instances):
    print("Waiting for instance")
    time.sleep(1)

our_instance = reservation.instances[0]
our_instance.add_tag('Name', NAME)

while our_instance.state != 'running':
    print("State of our instance: {0}".format(our_instance.state))
    our_instance.update()
