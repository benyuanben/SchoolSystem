from Address import Address

class Person:
    def __init__(self, first, last, dob, phone, address):
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone_number = phone
        #the address parameter can either be a list of addresses or a single instance of address
        self.addresses = []
        # check that the address argument is a single instance of Address
        if isinstance(address, Address):
            self.addresses.append(address)
        #else if: check that the address argument is an instance of list
        elif isinstance(address, list):
            #for each entry in the list, check that they are instances of Address
            for entry in address:
                # another option:
                # assert isinstance(entry, Address), "Invalid Address...\n"
                if not isinstance(entry, Address):
                    raise ValueError("Invalid Address...\n")

            self.addresses = address
        else:
            #if address is not in the prev two forms, then it is invalid input
            raise ValueError("Invalid Address Input...\n")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise ValueError("Invalid Address Input...\n")

        self.addresses.append(address)

