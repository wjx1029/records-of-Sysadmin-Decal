#!/bin/bash

ip link show eth0 | head -n 2 | tail -n 1 | cut -c 16-32