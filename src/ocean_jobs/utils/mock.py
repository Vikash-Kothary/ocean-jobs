
import boto3

def get_mock_data():
	client = boto3.client('lambda')
	response = client.get_account_settings()
	return response['AccountUsage']