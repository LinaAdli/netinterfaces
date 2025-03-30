# netinterfaces

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight and cross-platform Python library to retrieve network interface names with a simple API.

Find on PyPI -  https://pypi.org/project/netinterfaces/

## Features
- **Single-function API** – Quickly retrieve network interface names with minimal effort.
- **Cross-platform support** – Works on Windows, Linux, and macOS.
- **No external dependencies** – Pure Python implementation with no additional requirements.
- **Consistent output format** – Provides a uniform list output across different operating systems.
- **Handles errors gracefully** – Returns an empty list in case of errors instead of crashing.

## Installation

Install `netinterfaces` using `pip`:

```bash
pip install netinterfaces
```

## Usage

Import and use `get_interfaces` to retrieve network interface names:

```python
from netinterfaces import get_interfaces

interfaces = get_interfaces()
print(interfaces)  # Example output: ['eth0', 'wlan0', 'lo']
```

## Platform-Specific Examples

The library adapts to different platforms and returns interface names accordingly:

- **Linux**: `['lo', 'eth0', 'wlan0']`
- **Windows**: `['Ethernet', 'Wi-Fi', 'Loopback Pseudo-Interface']`
- **macOS**: `['lo0', 'en0', 'en1']`

## API Documentation

### `get_interfaces()`
```python
def get_interfaces() -> list:
    """
    Retrieves a list of network interface names available on the system.
    
    Returns:
        list: A list of network interface names (e.g., ['eth0', 'wlan0', 'lo']).
        If an error occurs, an empty list is returned.
    """
```
#### Returns
- **List of strings**: Each string represents a network interface name.
- **Empty list**: Returned in case of an error (e.g., lack of permissions, unexpected system behavior).

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Implement your changes and write tests if necessary.
4. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Deadpool2000/netinterfaces/blob/main/LICENSE) file for details.

## Support

If you encounter any issues or have feature requests, please open an [issue](https://github.com/Deadpool2000/netinterfaces/issues) on the GitHub repository.
