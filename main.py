import os, glob, subprocess


def make_plural(condition):
    return 's' if condition else ''


def main():
    # obtaining directory of desired exe
    while True:
        directory = input("Please paste the path of the directory that contains the desired exe: ")

        # checks if directory exists
        print("Confirming directory... ")
        if not os.path.isdir(directory):
            print("Please enter a valid directory. ")
            continue

        # checks if any executables are present
        print("Checking for executables... ")
        os.chdir(directory)
        executables = glob.glob("*.exe")
        if not executables:
            print("The directory you entered does not contain any executables.")
            continue

        break  # basically replicates a do/while loop in py

    # prints array of .exe files
    print(f"\nFound {len(executables)} executable{make_plural(len(executables) > 1)} in {directory}:")
    print("\n".join("- " + i for i in executables) + "\n")

    # requests user selection of exe
    if len(executables) > 1:
        while True:
            executable = input("Select an executable from the list above: ")
            if not executable.endswith(".exe"):
                executable += ".exe"

            if executable in executables:
                break

            print("Please enter a valid executable.")
    else:
        executable = executables[0]  # automatically selects the only executable if only one is present

    # creates temporary batch file
    with open(f"bypass.bat", "w") as f:
        f.write(
            f"""
        set __COMPAT_LAYER=RunAsInvoker
        start {executable[:-4]}
        """)

    # executes and deletes aforementioned batch file
    subprocess.call(["bypass.bat"])
    os.remove("bypass.bat")


if __name__ == "__main__":
    main()
