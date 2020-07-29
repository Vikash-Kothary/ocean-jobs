import boto3


def get_mock_data():
    try:
        client = boto3.client("lambda")
        response = client.get_account_settings()
    except Exception as e:
        print(e)
    finally:
        response = {"AccountUsage": {"FunctionCount": None}}
    return response["AccountUsage"]
