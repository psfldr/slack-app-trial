import boto3

ssm = boto3.client('ssm', 'ap-northeast-1', endpoint_url='http://localstack:4566')
# response = ssm.put_parameter(
#     Name='test_param_name',
#     Value='test_param_value'
# )
# print(response)

response = ssm.get_parameter(
    Name='test_param_name'
)
print(response)