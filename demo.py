import boto3
aws_mg_con=boto3.session.Session(profile_name='cc_user')


iam_con=aws_mg_con.client(service_name='iam',region_name='us-east-1')
for each_user in iam_con.list_users()["User"]:
    print(each_user['UserName'])
#print(dir(aws_mg_con))
#print(aws_mg_con.get_available_resources())