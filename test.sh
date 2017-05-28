#!/bin/bash

while read LINE; do
  python consumer.py $LINE
done < /dev/stdin
