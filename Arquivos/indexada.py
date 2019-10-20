from helpers.so import OS


if __name__ == '__main__':

    info = "\nuser@os:~"
    text = info + "r/$ "
    command = ""
    opsystem = OS(memory_size=512)

    while command != "exit":
        command = input(text)

        inputs = command.split(" ")

        if len(inputs) == 1 and inputs[0] != "ls":
            print("Comando executado de forma incompleta.")
            continue

        if inputs[0] == "cd":
            text = info + opsystem.cd(inputs[1]) + "$ "
        elif inputs[0] == "ls":
            opsystem.ls()
        elif inputs[0] == "mkdir":
            print("mkdir")
            opsystem.mkdir(inputs[1])
        elif inputs[0] == "rm":
            opsystem.rm(inputs[1])
        else:
            print("Informe um comando válido.")

        print(opsystem.info())
