import os
import pdb
import sys
import json
import time
import boto3

# ARGS:
#     - bucket
#     - key
#     - object
#     - ACL

if len(sys.argv) != 4:
    print("Usage: python replace.py <bucket> <key> <file path> <ACL (default to public)>")
    sys.exit()

bucket = sys.argv[1]
key = sys.argv[2]
file_path = sys.argv[3]

if len(sys.argv) == 5:
    # TODO
    acl = sys.argv[4]
else:
    acl = "public-read"

# boto3.set_stream_logger('')
s3 = boto3.client("s3")

print("Replacing object: {}".format(file_path))
response = s3.delete_object(
                            Bucket=bucket,
                            Key=key
                            )
print(json.dumps(response, indent=4))

time.sleep(0.5)
response = s3.put_object(
                            ACL=acl,
                            Body=file_path,
                            Bucket=bucket,
                            Key=key
                        )

print(json.dumps(response, indent=4))
print("\n")

time.sleep(0.5)
