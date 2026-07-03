#!/bin/bash
sleep 5
tail -n 20 npm-debug.log || echo "No debug log"
