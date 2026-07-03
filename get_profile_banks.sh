#!/bin/bash
tail -n 200 src/views/ProfileView.tsx | grep -B 20 -A 20 "Metode Pembayaran"
