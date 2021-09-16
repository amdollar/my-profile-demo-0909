from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
    aws_s3_deployment as deployment,
    aws_route53 as route53,
    aws_cloudfront_origins as origins,
    aws_cloudfront as cloudfront,
    aws_iam as iam
)
from types import CodeType


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.


[recordName, domainName] = ['www', 'my-profile.com']

class MyProfileApplicationStaticTwoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

         #code for s3 bucket.
        bucket= s3.Bucket(self, id='s3bucket03', bucket_name= 'my-profile.com',
            website_index_document= "index.html",
            #public_read_access= True,
            removal_policy= cdk.RemovalPolicy.DESTROY
        )

        originAccessIdentity = cloudfront.OriginAccessIdentity(self, 'OAI')
        #bucket.grant_read(originAccessIdentity)

        bucket.add_to_resource_policy(iam.PolicyStatement(
            actions=['s3:GetObject'],
            resources=[bucket.arn_for_objects('*')],
            principals= [iam.CanonicalUserPrincipal(originAccessIdentity.cloud_front_origin_access_identity_s3_canonical_user_id)]
        ))

        distribution = cloudfront.CloudFrontWebDistribution(self, 'cloud-front-web-dist',
            origin_configs=[cloudfront.SourceConfiguration(
                s3_origin_source=cloudfront.S3OriginConfig(
                    s3_bucket_source= bucket,
                    origin_access_identity=originAccessIdentity
                ),
                behaviors=[cloudfront.Behavior(is_default_behavior=True)]
            )
            ])

        # s3 bucket deployment Code
        deployment.BucketDeployment(self, 'my-profile-bucket-deployment-py03', sources= [deployment.Source.asset("website")],
        destination_bucket= bucket)

        #OAI
        


        #Code for adding Cloud front on s3 bucket. 

#        cloudfront.Distribution(self, 'my-profile-application-distribution', default_behavior= cloudfront.BehaviorOptions(
 #           origin=origins.S3Origin(bucket, origin_access_identity: )))


    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # lookup the zone based on domain name
        #zone = route53.HostedZone.from_lookup(self, 'HostedZone', domain_name= domainName)

        # adding subdomain to the Route 53.
        

       # cName= route53.ARecord(self, 'AliasRecord', zone= zone, record_name= recordName, 
        #target= route53.RecordTarget.from_alias(alias_target= bucket))
        #AddressRecordTarget(alias_target=ApiGatewayDomain(domain_name=the_lambda_api_gateway.domain_name))


