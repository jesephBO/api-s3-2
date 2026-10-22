import base64
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directorio']
    nombre_archivo = event['body']['archivo']
    base64_str = event['body']['base64']
    
    if nombre_directorio and not nombre_directorio.endswith('/'):
        nombre_directorio += '/'
        
    ruta_s3 = f"{nombre_directorio}{nombre_archivo}"
    
    s3 = boto3.resource('s3')
    s3.Object(nombre_bucket, ruta_s3).put(Body=base64.b64decode(base64_str))
    
    return {
        'statusCode': 200,
        'mensaje': 'Archivo subido con éxito',
        'bucket': nombre_bucket,
        'ruta_archivo': ruta_s3
    }