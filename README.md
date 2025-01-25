## Feature
&nbsp;'no40' will aims to complete resource operations in Azure using the command line. In other words, no40 will provide multiple commands and options to apply resource settings as a cli.

### usage example
---
```no40 crg sampleRG ```  
>Resource group sampleRG created in japaneast  

&nbsp;Create a resource group named sampleRG. no40 works as cli and crg as subcommand. This command requires the resource group name to be specified.  

```no40 crg sampleRG --dry-run -v```  
>Simulating resource group creation:  
Name: sampleRG  
Location: japaneast  
tag: {}

&nbsp;This simulates the creation of a resource group and prints the results in detail to the terminal.  


## background
&nbsp;Why did this project start? That is learning cli and github.  
Azure resource operations as a value-add I wanted to add.  
&nbsp;Therefore, the vision for this cli is to add commands, and to accept the addition of functionality on a command-by-command basis as open source.

## Setup
1. git clone https://github.com/Amanecha/no40.git
2. cd no40
3. cp env.sample .env
4. Open the .env file and fill in the required values: AZURE_SUBSCRIPTION_ID: Your Azure Subscription ID
5. python3 -m venv .venv
6. source .venv/bin/activate
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