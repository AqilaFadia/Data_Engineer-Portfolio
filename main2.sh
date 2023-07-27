#!/bin/bash

# Variables
filename_excel=daily_market_price.xlsx
source_dir=/local/data/market
target_dir=/path/to/target/directory

# Check if target directory exists
if [ -d "$target_dir" ]; then
    # Copy file from source directory to target directory
    cp "$source_dir/$filename_excel" "$target_dir/"

    # Check if copy was successful
    if [ $? -eq 0 ]; then
        # Create log file with success message
        echo "File Moved Successfully" > "$target_dir/log.txt"
    else
        echo "Failed to move file"
    fi
else
    echo "Target directory does not exist"
fi



