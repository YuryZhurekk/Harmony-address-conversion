from pyhmy import util

def convert_addresses(filename):
    with open(filename, 'r') as file:
        addresses = file.readlines()

    for i, address in enumerate(addresses):
        address = address.strip()
        one_address = util.convert_hex_to_one(address)
        print(f"{i+1}. {one_address}")

if __name__ == "__main__":
    convert_addresses('wallets.txt')