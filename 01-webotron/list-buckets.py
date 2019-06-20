# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
    
if __name__ == '__main__':
    print('List of all the buckets..\n')
    for bucket in s3.buckets.all():
        print(bucket)
 
