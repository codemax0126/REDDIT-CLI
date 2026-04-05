banner = """

    ██████╗ ███████╗██████╗ ██████╗ ██╗████████╗     ██████╗██╗     ██╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝    ██╔════╝██║     ██║
    ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║       ██║     ██║     ██║
    ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║       ██║     ██║     ██║
    ██║  ██║███████╗██████╔╝██████╔╝██║   ██║       ╚██████╗███████╗██║
    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝        ╚═════╝╚══════╝╚═╝

                REDDIT CLI — (prototype)
"""

print(banner)

countinue = input("Do you want you continue? Y/n: ")

if countinue == "Y":
    Ask = input("What question would you like to search? ")
    print(f"Answers for {Ask}")
elif countinue == "n":
    print("It's ok")
else:
    quit()
