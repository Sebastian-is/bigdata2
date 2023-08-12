import boto3

bucket_name = 'bigdatauwu'

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    print(f'Archivos en el bucket {bucket_name}:')
    for obj in response['Contents']:
        print(f'  {obj["Key"]}')
else:
    print(f'El bucket {bucket_name} no contiene objetos.')
