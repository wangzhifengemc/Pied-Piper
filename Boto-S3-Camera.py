#!/usr/bin/env python3
import boto

ecs_access_key_id = '131728097553483434@ecstestdrive.emc.com'  
ecs_secret_key = 'jtY64m/sOI7K/XorGUUzv6gchZtmG6fwgMOSvisB'

#### This is the AWS S3 syntax
#session = boto.connect_s3(ecs_access_key_id, ecs_secret_key)

#### This is the ECS syntax. It requires "host" parameter
session = boto.connect_s3(ecs_access_key_id, ecs_secret_key, host='object.ecstestdrive.com')  

bname = 'wzf-bucket'
#### Create a bucket
####b = session.create_bucket(bname, headers=None, location='', policy=None) 

#### Get bucket and display details
print ("ECS connection is: " + str(session))
b = session.get_bucket(bname)
##print ("ECS connection is: " + str(session))
print ("Bucket is: " + str(b))

filename = "foo.mp4"

#### Create new key, define metadata, upload and ACL
k = b.new_key(filename)
k.set_metadata('foo', 'yes')
k.set_contents_from_filename(filename)
k.set_acl('public-read')

#### Get an existing key
#k = b.get_key(filename)

#### Get specific metata for a key
##print (k.get_metadata('vmax'))
####The metadata can be seen in S3 in the "http headers" tab
####It gets stored as "x-amz-meta-vmax"

#### Delete an existing key
##k = b.get_key(filename)
##k.delete()

#### Get all buckets for a given session
##print (session.get_all_buckets())

#### Get all keys for a given bucket
##print (b.get_all_keys())

#### Display all keys in all buckets
#for bucket in session.get_all_buckets():
#    print ("In bucket: " + bucket.name)
#    for object in bucket.list():
#        print(object.key)

#### Display specific metadata for all keys in a bucket
#for k in b.list():
#    print (k.key)
#    key = b.get_key(k)
#    print (key.get_metadata('vmax'))
