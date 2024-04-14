# Initial command to create structured_responses1.txt
jq '.' response.txt > structured_responses1.txt

# Set to store unique lines
seen_lines=()
counter=0

while true; do
    # Process the structured_responses1.txt file
    while IFS= read -r line; do
        # Check if the line contains "full_text"
        if [[ $line == *"full_text"* ]]; then
            # Check if the line is already in the set
            if ! [[ " ${seen_lines[@]} " =~ " ${line} " ]]; then
                # Prepend the username to the line
                line="name: @UserHere, $line"
                # Append the line to output.txt
                echo "$line" >> output.txt
                # Add the line to the set
                seen_lines+=("$line")
                # Increment the counter
                ((counter++))
                # Check if we have found the first 3 occurrences
                if [ $counter -eq 3 ]; then
                    break  # Exit the inner loop
                fi
            fi
        fi
    done < structured_responses1.txt

    # Sleep for 45 seconds
    sleep 45

    # Update structured_responses1.txt with latest data
    jq '.' response.txt > structured_responses1.txt
done
