import tomllib
from pprint import pprint

def load_toml() -> dict:
    """Load TOML data from file"""

    # rb = read bytes mode
    # with open("config.toml", "rb") as f:
    with open("C:/Users/CBZ/Desktop/TOML/config.toml", "rb") as f:
        toml_data: dict = tomllib.load(f)
        return toml_data
    
if __name__ == '__main__':
    data: dict = load_toml()
    pprint(data, sort_dicts=False)


"""
# Write initial TOML data to the file if needed
with open('config.toml', 'w') as f:


# Rest of the code
with open('/path/to/config.toml', 'rb') as f:

"""