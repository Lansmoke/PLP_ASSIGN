def modify_content(content):
    """
    A simple function that modifies file content.
    Here, we convert text to uppercase.
    You can replace this logic with any modification you want.
    """
    return content.upper()


def main():
    try:
        # Ask user for input filename
        input_file = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify content
        modified_content = modify_content(content)

        # Ask for output file name
        output_file = input("Enter the name of the new file to write to: ")

        # Write modified content to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ Modified content successfully written to '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
