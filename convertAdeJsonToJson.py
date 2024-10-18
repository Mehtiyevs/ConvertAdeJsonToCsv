import json
import os

index = 1
            # files total number
while index <= 46:
    try:
                        # if you have more adeJson files, rename all of their name 
                        # to same one and this functioin will directly get all of them
        old_filename = f'yourFileName{index}.json'
        new_filename = f'data{index}.json'

        
        os.rename(old_filename, new_filename)

        data = []
        with open(new_filename, 'r') as file:
            count = 0
            for line in file:
                print(count)
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError:
                    data.append(json.loads(line[:-1]))
                count += 1

      
        corrected_filename = f'data{index}Correct.json'
        with open(corrected_filename, 'w') as file:
            file.write(json.dumps(data, indent=4))
        
        index += 1

    except FileNotFoundError:
        print(f"File {old_filename} not found.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break
