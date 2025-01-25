## Feature
'no40' will aims to complete resource operations in Azure using the command line. In other words, no40 will provide multiple commands and options to apply resource settings as a cli.

## Setup
1. git clone https://github.com/Amanecha/no40.git
2. cd no40
3. cp env.sample .env
4. Open the .env file and fill in the required values: AZURE_SUBSCRIPTION_ID: Your Azure Subscription ID
5. python3 -m venv .venv
6. source venv/bin/activate
7. pip install -r requirements.txt
8. pip install -e .
9. az login --scope https://management.azure.com/.default  
- no40 --help
- no40 list-resources  
- no40 list-resources resource-group  

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Dependencies
This project relies on the following libraries:
- numpy (BSD License)
- requests (Apache 2.0 License)
- PyTorch (BSD License)
Please refer to the respective licenses of these libraries for more details.