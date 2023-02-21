Day 42: IAM Programmatic access and AWS CLI 🚀 ☁ 

 

Today is more of a reading exercise and getting some programmatic access for your AWS account 

IAM Programmatic access 

In Order to access your AWS account from a terminal or system, you can use AWS Access keys and AWS Secret Access keys Watch this video for more details. 

AWS CLI 

The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts. 

The AWS CLI v2 offers several new features including improved installers, new configuration options such as AWS IAM Identity Center (successor to AWS SSO), and various interactive features. 

Task-01 

Create AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY from AWS Console. 

Task-02 

Setup and install AWS CLI and configure your account credentials 

 

First Create a User.  

Click on the Add Users Button on the Right Corner. 

 ![sc-4](https://user-images.githubusercontent.com/73602443/220323029-a0cdd499-f233-4877-9a1c-2bee802345e1.JPG)
 
 ![sc-5](https://user-images.githubusercontent.com/73602443/220323083-1fbe0028-1d4b-4ebd-b9f0-dea699a6c2eb.JPG)


Give AWSEC2FullAccess  Permissionto User. 

 ![sc-6](https://user-images.githubusercontent.com/73602443/220323208-9de4e10f-8bf2-4912-bf9a-2adf3c6b793f.JPG) 

User is Created Successfully. 

![sc-7](https://user-images.githubusercontent.com/73602443/220323255-8ac586f2-5306-4ffe-a1e1-cfdaacc09149.JPG)




Click on username and select security credentials Tab. 

Inside click on Access Key Tab. 

Select CLI as an Option. And click the next button. 

![sc-8](https://user-images.githubusercontent.com/73602443/220323329-7eea55a2-dd06-4100-89f0-540209e6c224.JPG)

You have successfully created the Access key and Secret key. 

If you want, then you simply download the Download.csv file. 

This File includes your AccessKey and SecretAccessKey. 

 ![sc-9](https://user-images.githubusercontent.com/73602443/220323387-02bfdba5-6c80-466f-b861-9b7e4fad39a5.JPG)


 

Now install AWS CLI. 

If you are windows User, then you simply  

Download and run the AWS CLI MSI installer for Windows (64-bit) 

All you need to do is install AWS CLI as same as you generally install any software application by accepting the terms, clicking next and then finish to install. 

 ![sc-10](https://user-images.githubusercontent.com/73602443/220323451-ae0a205d-0e1c-4276-acdb-ed835e089c46.JPG)

![sc-11](https://user-images.githubusercontent.com/73602443/220323515-4b5fa5bb-74c6-41ca-8e5d-714a2d71bda8.JPG)

For AWS Configuration, 

We need to run the command  aws configure. 

They will ask your 

1] AWS Access Key ID 

2] AWS Secret Access Key 

3] Default region name 

4] Default output format 


 ![sc-12](https://user-images.githubusercontent.com/73602443/220324877-1a9154b4-22d8-4aa2-a61e-8c150432a0c6.JPG)


Check AWS Version 

		aws --version 

 ![sc-13](https://user-images.githubusercontent.com/73602443/220324923-34fc8c41-c388-40a0-b897-1a06635f4e28.JPG)


Happy Learning :) 

 
