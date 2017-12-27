import os
import pdb
import sys
import json
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

f = open(file_path, "r")

s3 = boto3.client("s3")
response = s3.put_object(
                            ACL=acl,
                            Body=f,
                            Bucket=bucket,
                            Key=key
                        )

f.close()

print(json.dumps(response))
