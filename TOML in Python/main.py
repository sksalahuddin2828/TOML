import tomllib
from pprint import pprint

def load_toml() -> dict:
    """Load TOML data from file"""

    # rb = read bytes mode
    # Must change your path or use this --> with open("config.toml", "rb") as f:
    with open("C:/Users/CBZ/Desktop/TOML/config.toml", "rb") as f:
        toml_data: dict = tomllib.load(f)
        return toml_data
    
if __name__ == '__main__':
    data: dict = load_toml()
    pprint(data, sort_dicts=False)



#-----------------------------------------------------------------------------------------------------------


# Answer: {'name': 'My Project',
# 'version': '1.0.1',
# 'website': 'https://www.2nonenone2.com/',
# 'items': {'numbers': [1, 2, 3],
#           'letters': ['a', 'b', 'c'],
#           'details': {'updated': True,
#                       'author': 'Test Name',
#                       'timestamp': datetime.datetime(2023, 6, 6, 0, 0, tzinfo=datetime.timezone.utc)}},
# 'database': {'file': {'type': 'sqlite', 'path': 'data.db'}},
# 'inline_table': {'inline': {'name': 'Test Name', 'age': 30}},
# 'table_group': [{'fruit': 'apple'}, {'fruit': 'orange'}, {'fruit': 'banana'}]}


#-----------------------------------------------------------------------------------------------------------

"""
# Write initial TOML data to the file if needed
with open('config.toml', 'w') as f:


# Rest of the code
with open('/path/to/config.toml', 'rb') as f:

"""
