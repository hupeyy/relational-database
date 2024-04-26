class inMemoryDB:
    def __init__(self):
        self.db = {}
        self.key = None
        self.value = None
        self.transaction = False

    def put(self, key, value):
        try:
            value = int(value)
            if self.transaction:
                self.key = key
                self.value = value
            else:
                print("Error: no transaction in progress")
        except ValueError:
            print("Error: value must be an integer")
            return
    
    def get(self, key):
        if key in self.db:
            return self.db[key]
        else:
            return None

    def begin_transaction(self):
        self.transaction = True

    def commit(self):
        if self.transaction:
            self.transaction = False
            self.db[self.key] = self.value
        else:
            print("Error: no transaction in progress")
        
    def rollback(self):
        if self.transaction:
            self.transaction = False
            self.key = None
            self.value = None
        else:
            print("Error: no transaction in progress")

def main():
    db = inMemoryDB()
    
    command_list = """Commands:
    GET key
    PUT key value
    BEGIN
    COMMIT
    ROLLBACK
    END
    """
    while True:
        print(command_list)
        command = input("Enter command: ")
        command = command.upper()
        command = command.split()

        if command[0] == "END":
            break
        elif command[0] == "BEGIN":
            db.begin_transaction()
        elif command[0] == "ROLLBACK":
            db.rollback()
        elif command[0] == "COMMIT":
            db.commit()
        elif command[0] == "GET":
            print("THE VALUE OF " + command[1] + " is:", db.get(command[1]))
        elif command[0] == "PUT":
            db.put(command[1], command[2])
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()