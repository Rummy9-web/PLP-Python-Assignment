try:
    filename = input("Enter the file name: ")
    with open(filename, "r") as f:
        content = f.read()

    # Simple modification: make content uppercase
    modified = content.upper()

    new_file = "modified_" + filename
    with open(new_file, "w") as f:
        f.write(modified)

    print(f"Modified file saved as {new_file}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Error: {e}")
