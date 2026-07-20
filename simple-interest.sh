#!/bin/bash

# Simple Interest Calculator (Bash)
# Formula: SI = (P * R * T) / 100

echo "=== Simple Interest Calculator ==="

read -p "Enter principal amount: " principal
read -p "Enter annual interest rate (%): " rate
read -p "Enter time period (years): " time

# Calculate simple interest using bc for decimal support
interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
total=$(echo "scale=2; $principal + $interest" | bc)

echo ""
echo "Simple Interest: $interest"
echo "Total Amount (Principal + Interest): $total"
