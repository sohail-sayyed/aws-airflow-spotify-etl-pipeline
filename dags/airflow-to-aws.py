from airflow import DAG
from datetime import datetime
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator
from airflow.providers.amazon.aws.operators.s3 import S3DeleteBucketOperator
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator
from airflow.providers.amazon.aws.operators.lambda_function import LambdaCreateFunctionOperator
import spotipy
from airflow.operators.python_operator import PythonOperator
from spotipy.oauth2 import SpotifyClientCredentials
import json
from airflow.models import Variable
import pandas as pd
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def _fetch_spotify_data(**kwargs):
    auth_manager = SpotifyClientCredentials(client_id=Variable.get('spotify_client_id'), client_secret=Variable.get('spotify_client_secret'))
    sp = spotipy.Spotify(auth_manager=auth_manager)
    data=sp.new_releases(country='IN', limit=50)

    kwargs['ti'].xcom_push(key='spotify_data', value=json.dumps(data))


def _transform_data(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='fetching_spotify_data', key='spotify_data')
    var = json.loads(data)
    s3_hook=S3Hook(aws_conn_id='aws_s3_airbnb')
    bucket_name= 'airflow-bucket'
    prefix=f"spotify-data/processed_data/"
    artists_details=[]
    for i in var['albums']['items']:   
         looping= i['artists']
         for j in looping:
             artist_url = j['external_urls']['spotify']
             artist_name = j['name']
             artist_id = j['id']
             artists_details.append({'artist_url': artist_url, 'artist_name': artist_name, 'artist_id': artist_id})

    artists_df = pd.DataFrame(artists_details, index=range(1, len(album_details)+1))
    artists_df.to_csv('artists_details.csv', index=False)

    s3_hook.load_file(filename='artists_details.csv', key=prefix + f"album_details{datetime.now().strftime('%Y%m%d, %H:%M:%S')}.csv", bucket_name=bucket_name, replace=True)

dag=DAG(
    dag_id='spotify_etl_pipeline',
    start_date=datetime(2024, 12, 1),
    schedule_interval='@daily',
    description='An airflow pipeline which fetch data from spotify API. transform it and then load it to s3 bucket',
)

create_bucket=S3CreateBucketOperator(
    task_id='creating_bucket',
    bucket_name='airflow-bucket',
    aws_conn_id='aws_s3_airbnb',
    region_name = 'ap-south-1',
    dag=dag
)

fetch_spotify_data=PythonOperator(
    task_id = 'fetching_spotify_data',
    python_callable=_fetch_spotify_data,
    dag=dag,
)

create_object_raw=S3CreateObjectOperator(
    task_id="creating_object_raw",
    aws_conn_id='aws_s3_airbnb',
    s3_bucket='airflow-bucket',
    s3_key=f"spotify-data/raw_data/spotify_raw_{datetime.now().strftime('%Y%m%d, %H:%M:%S')}.json",
    data="{{ task_instance.xcom_pull(task_ids='fetching_spotify_data', key='spotify_data') }}",
    replace=True,
    dag=dag
)

transform_data=PythonOperator(
    task_id = 'transforming_data',
    python_callable=_transform_data,
    dag=dag
)

create_bucket >> fetch_spotify_data >> create_object_raw >> transform_data
