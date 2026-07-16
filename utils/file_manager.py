class FileManager:
    
    @staticmethod
    def write_file(filename, data):

        with open(filename, "w") as file:
            file.write(data)

        print("Data Written Successfully.")


    @staticmethod
    def append_file(filename, data):

        with open(filename, "a") as file:
            file.write(data + "\n")

        print("Data Appended Successfully.")


    @staticmethod
    def read_file(filename):

        with open(filename, "r") as file:
            return file.read()


    @staticmethod
    def clear_file(filename):

        with open(filename, "w") as file:
            file.write("")

        print("File Cleared Successfully.")