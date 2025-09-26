```
Sample data:
students_info = {
    "Alice": {
        "age": 14,
        "class": "9A",
        "father_name": "Mr. Johnson"
    },
    "Bob": {
        "age": 15,
        "class": "9B",
        "father_name": "Mr. Smith"
    },
    "Charlie": {
        "age": 14,
        "class": "9A",
        "father_name": "Mr. Thompson"
    }
}

subject_scores = {
    "Math": {"Alice": 88, "Bob": 76},
    "Science": {"Alice": 91, "Charlie": 85},
    "History": {"Bob": 67, "Charlie": 78}
}

sample output:
{Alice: {age, class, fn, av_m}, bob:{age, class, fn, av_m}, charlie:{age, class, fn, av_m}}

solution::
# Build the final dictionary
final_output = {}

for student, details in students_info.items():
    scores = []
    for subject, marks in subject_scores.items():
        if student in marks:
            scores.append(marks[student])
    avg_score = sum(scores) / len(scores) if scores else 0
    final_output[student] = {
        "age": details["age"],
        "class": details["class"],
        "fn": details["father_name"],
        "av_m": avg_score
    }

print(final_output)

```

S3-Lambda cross account access:

To allow a Lambda function in AWS Account B to access an S3 bucket in Account A, the recommended approach is to use IAM roles and cross-account permissions.

Step-by-Step Setup
1. Create an IAM Role in Account A for S3 access

In Account A, define a role (for example, S3AccessRoleFromAccountB) that has permissions (via a policy) to access the S3 bucket (like s3:GetObject).

Set the "Trust Relationship" so that Account B's Lambda execution role can assume this role.

2. Update the Lambda Execution Role in Account B

Add permissions allowing the Lambda to use AWS STS to AssumeRole for the role you made in Account A.
```
Example policy to attach to Lambda's role in Account B:

json
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam::<AccountA-ID>:role/S3AccessRoleFromAccountB"
}
```

3. Update the S3 Bucket Policy in Account A

Optionally, you can adjust the bucket policy to allow access from the IAM Role if not already included.

4. Use Role Assumption in Lambda Code

In your Lambda, use AWS STS to assume the role from Account A before accessing S3.
```
Example (Python, boto3):

python
import boto3

sts_client = boto3.client('sts')

role_arn = 'arn:aws:iam::<AccountA-ID>:role/S3AccessRoleFromAccountB'
assumed_role = sts_client.assume_role(
    RoleArn=role_arn,
    RoleSessionName='LambdaSession'
)
credentials = assumed_role['Credentials']

s3_client = boto3.client(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)
```

# Now you can use s3_client to access S3 in Account A
5. Security Notes

Follow the principle of least privilege for IAM policies and roles.

Avoid using overly broad permissions or unnecessary wildcards in resource ARNs.

Summary Table
Step	Account A (S3 Owner)	Account B (Lambda Owner)
IAM	Create role with S3 access and trust for Account B	Lambda execution role with sts:AssumeRole
Policy	S3 policy if needed for cross-account	Attach policy for sts:AssumeRole
Lambda	-	Assume role and access S3 via assumed creds
