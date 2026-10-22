import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directorio']
    
    if not nombre_directorio.endswith('/'):
        nombre_directorio += '/'
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=nombre_directorio)
    
    return {
        'statusCode': 200,
        'mensaje': f'Directorio {nombre_directorio} creado correctamente',
        'bucket': nombre_bucket,
        'directorio': nombre_directorio
    }