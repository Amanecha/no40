
## Setup
1. Clone the repository
2. cp .env.sample .env
3. Open the .env file and fill in the required values: AZURE_SUBSCRIPTION_ID: Your Azure Subscription ID
4. pip install -r requirements.txt
5. python azure_resources_cli.py
- az login --scope https://management.azure.com/.default  
- python azure_resources_cli.py --help  
- python azure_resources_cli.py list-resources  
- python azure_resources_cli.py list-resources resource-group  