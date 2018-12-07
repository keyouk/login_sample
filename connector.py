import boto
import boto.s3.connection
import os

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')


# conn = boto.connect_s3(
#         aws_access_key_id = AWS_ACCESS_KEY,
#         aws_secret_access_key = AWS_SECRET_KEY,
#         calling_format = boto.s3.connection.OrdinaryCallingFormat(),
#     	)


# def getAllBuckets():
# 	for bucket in conn.get_all_buckets():
# 		print "{name}\t{created}".format(
#                 name = bucket.name,
#                 created = bucket.creation_date,
#         )

if __name__ == '__main__':
	print AWS_SECRET_KEY
	print AWS_ACCESS_KEY