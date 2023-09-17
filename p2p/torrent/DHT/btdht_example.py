#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import btdht
import binascii
import utils

dht = btdht.DHT()
dht.start()  # now wait at least 15s for the dht to boostrap
#init socket for 4c323257aa6c4c5c6ccae118db93ccce5bb05d92
#Bootstraping
dht.get_peers(binascii.a2b_hex("0403fb4728bd788fbcb67e87d6feb241ef38c75a"))
"""
[
    ('81.171.107.75', 17744),
    ('94.242.250.86', 3813),
    ('88.175.164.228', 32428),
    ('82.224.107.213', 61667),
    ('85.56.118.178', 6881),
    ('78.196.28.4', 38379),
    ('82.251.140.70', 32529),
    ('78.198.108.3', 10088),
    ('78.235.153.136', 10619),
    ('88.189.113.32', 33192),
    ('81.57.9.183', 5514),
    ('82.251.17.155', 14721),
    ('88.168.207.178', 31466),
    ('82.238.89.236', 32970),
    ('78.226.209.88', 2881),
    ('5.164.219.48', 6881),
    ('78.225.252.39', 31002)
]
"""