import os, glob, subprocess


def make_plural(condition):
    return 's' if condition else ''


def main():
    # obtaining directory of desired exe
    while True:
        directory = input("Please paste the path of the directory that contains the desired exe: ")

        print("Confirming directory... ")
        if not os.path.isdir(directory):
            print("Please enter a valid directory. ")
            continue

        print("Checking for executables... ")
        os.chdir(directory)
        executables = glob.glob("*.exe")
        if not executables:
            print("The directory you entered does not contain any executables.")
            continue

        break

    print(f"\nFound {len(executables)} executable{make_plural(len(executables) != 1)} in {directory}:")
    print("\n".join("- " + i for i in executables) + "\n")
    if len(executables) > 1:
        while True:
            executable = input("Select an executable from the list above: ")
            if not executable.endswith(".exe"):
                executable += ".exe"

            if executable in executables:
                break

            print("Please enter a valid executable.")
    else:
        executable = executables[0]

    with open(f"bypass.bat", "w") as f:
        f.write(
            f"""
        set __COMPAT_LAYER=RunAsInvoker
        start {executable[:-4]}
        """)

    subprocess.call(["bypass.bat"])
    os.remove("bypass.bat")

if __name__ == "__main__":
    main()
