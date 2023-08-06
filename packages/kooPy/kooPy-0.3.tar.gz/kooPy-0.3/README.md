# KooPy: Koo for Python!

KooPy is a Python library for [KooApp](https://www.kooapp.com/feed).

This is a very basic version with only the most basic functions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install KooPy.

```bash
pip install kooPy
pip install kooPy --upgrade
```

## Usage

```python
from kooPy import Koo

# Initialize
ku = Koo()

# Get User Profile
profile = ku.getUserProfile('virat.kohli', format='dict', method='filter')

# Get User Koos
user_koos = ku.getUserKoos('virat.kohli', format='dict', method='filter', limit=10)

# Get Trending Koos
trending = ku.getTrendingKoos(format='dict', method='filter', limit=5)
```

## Contributing

Pull requests are welcome. For major changes, you can also open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
