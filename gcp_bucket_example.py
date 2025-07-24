import json
import os
from google.cloud import storage

# create files
def create_files():
    dic = {'name':'Bob',
           'accident details': 'car crash',
           'accident place': 'Terre Haute',
           'accident date': '23rd July'}
    for i in range(1,20):
        folder_name = 'json_files'
        file_name = "details_"+str(i)+".json"
        full_path = os.path.join(folder_name, file_name)
        with open(full_path, 'w') as file:
            json.dump(dic, file)
        upload_files('bucket_23_july', full_path, 'claims_23_july/'+ file_name) 
    return "Sucess"

# upload files to GCP
def upload_files(bucket_name, source_file_path, destination_blob_name):
    client = storage.Client.from_service_account_json('proud-coral-466820-c9-d928beb1fbfe.json')
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(source_file_path)
    print(f"File {source_file_path} uploaded to {destination_blob_name}.")

    return "sucess"

# download a file from GCP
def download_files(bucket_name, source_blob_name, destination_file_path):
    client = storage.Client.from_service_account_json('proud-coral-466820-c9-d928beb1fbfe.json')
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    
    blob.download_to_filename(destination_file_path)
    print(f"Blob {source_blob_name} downloaded to {destination_file_path}.")
    return "download sucess"

# delete a file from GCP
def delete_files(bucket_name, blob_name):
    client = storage.Client.from_service_account_json('proud-coral-466820-c9-d928beb1fbfe.json')
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    blob.delete()
    print(f"Blob {blob_name} deleted.")

    return "delete sucess"


def main():
    print(create_files())
    bucket_name = 'bucket_23_july'
    source_blob_name = 'claims_23_july/details_1.json'
    destination_file_path = os.path.join('cloud_files','details_1.json')
    print(download_files(bucket_name, source_blob_name, destination_file_path))
    blob_name = 'claims_23_july/details_2.json'
    print(delete_files(bucket_name, blob_name))
    
    

if __name__ == "__main__":
    main()