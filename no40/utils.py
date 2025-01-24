from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os

load_dotenv()

# Azureリソースの認証とクライアント作成
def get_client():
    """Azure のクライアントを作成する"""
    credential = DefaultAzureCredential() # az loginでログイン済みのアカウントを使用
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")  # load_dotenv()で読み込んだ環境変数にアクセスして取得
    return ResourceManagementClient(credential, subscription_id) # Azureのリソース管理APIにアクセスするためのクライアント