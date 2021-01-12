#!/bin/bash

for n in $(seq 0 20); do
size=$((2**n))
echo $size $(likwid-bench -t clcopy -w S0:${size}kB:1 2>/dev/null | grep MByte/s | cut -f 3)
done; 