import jsonpickle
from aws_xray_sdk.core import xray_recorder
from ocean_jobs.lambda_function import lambda_handler as handler


def test_function():
    xray_recorder.begin_segment("test_function")
    with open("tests/event.json", "rb") as file:
        ba = bytearray(file.read())
        event = jsonpickle.decode(ba)
        print("## EVENT")
        print(jsonpickle.encode(event))
        context = {"requestid": "1234"}
        result = handler(event, context)
        print(str(result))
        assert "FunctionCount" in str(result), "Should match"
    xray_recorder.end_segment()
