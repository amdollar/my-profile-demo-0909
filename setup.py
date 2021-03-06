import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="my_profile_application_static_two",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "my_profile_application_static_two"},
    packages=setuptools.find_packages(where="my_profile_application_static_two"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws_s3",
        "aws-cdk.aws_s3_deployment",
        "aws-cdk.aws_cloudfront",
        "aws_cdk.aws_cloudfront_origins",
        "aws-cdk.aws_iam"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
