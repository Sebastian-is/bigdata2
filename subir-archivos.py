import boto3

archivo = 'nwn.txt'

bucket_name = 'bigdatauwu'

s3 = boto3.client('s3')

s3.upload_file(archivo, bucket_name, archivo)

print(f'El archivo {archivo} se ha subido correctamente al bucket {bucket_name}.')
