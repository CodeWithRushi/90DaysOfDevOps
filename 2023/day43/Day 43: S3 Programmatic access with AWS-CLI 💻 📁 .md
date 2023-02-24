Day 43: S3 Programmatic access with AWS-CLI 💻 📁 

 

Hi,I hope you had a great day yesterday. Today as part of the #90DaysofDevOps Challenge we will be exploring the most	 commonly used service in AWS i.e. S3. 

![sc-32](https://user-images.githubusercontent.com/73602443/221088852-02f241c6-3aa7-4661-8836-1331a492ed11.JPG)


S3(Simple Cloud Storage) 

Amazon Simple Storage Service (Amazon S3) is an object storage service that provides a secure and scalable way to store and access data on the cloud. It is designed for storing any kind of data, such as text files, images, videos, backups, and more. Read more here 

Task-01 

Launch an EC2 instance using the AWS Management Console and connect to it using Secure Shell (SSH). 

 
![sc-13](https://user-images.githubusercontent.com/73602443/221089034-6ddd4ea1-0caa-4e50-8815-d54b1850d486.JPG)

 

We already created an IAM User, Now I am adding only AmazonS3FullAccess Permission to this User 

 ![sc-1](https://user-images.githubusercontent.com/73602443/221089124-499a2281-1b9d-4518-9b3f-a4d80b399024.JPG)


Setting up the AWS Console Login 

 
![sc-2](https://user-images.githubusercontent.com/73602443/221089154-cd0dc9ec-84f8-4476-a29b-98fd4db94738.JPG)

![sc-3](https://user-images.githubusercontent.com/73602443/221089200-1e4e43d1-cf0b-47fa-92ab-fcc49052415a.JPG)

Here we type Custom Password for sign In. 

 ![sc-4](https://user-images.githubusercontent.com/73602443/221089288-4e7d8179-df51-4544-8328-6f743fd20ca6.JPG)



Create an S3 bucket and upload a file to it using the AWS Management Console. 

Go to IAM USER Account, and Search S3. 

![sc-5](https://user-images.githubusercontent.com/73602443/221089327-b3a961bb-f278-473c-9b58-2c480974044d.JPG)


Give Bucket Name 

![sc-6](https://user-images.githubusercontent.com/73602443/221089365-b4300c0b-ede2-495d-8f53-182901972028.JPG)


Enabling versioning for keeping multiple versions of Objects in the same bucket. 

![sc-7](https://user-images.githubusercontent.com/73602443/221089422-bce14c9a-b4bd-4a52-a8ae-dc631618651e.JPG)


![sc-8](https://user-images.githubusercontent.com/73602443/221089435-021a6443-c429-4224-8b2d-fe7f4dedc420.JPG)


Bucket is created Successfully. 

![sc-9](https://user-images.githubusercontent.com/73602443/221089495-a3511997-4a08-4351-8f98-481661c27ca9.JPG)

 

Upload some files in this Bucket. 

 
![sc-10](https://user-images.githubusercontent.com/73602443/221089562-2fc5e7eb-51c0-4d7f-8afb-6f19eb247b4d.JPG)

 
![sc-11](https://user-images.githubusercontent.com/73602443/221089577-f1196967-57b3-49f1-a833-432146e275db.JPG)


 ![sc-12](https://user-images.githubusercontent.com/73602443/221089614-e7334b97-5677-40cd-bc02-d4ec237fe43b.JPG)


In This AWS CLI Demo, I am using Windows CMD. 

Make sure you already install AWS CLI MSI installer for Windows 

Configure the AWS CLI 

![sc-16](https://user-images.githubusercontent.com/73602443/221089674-f623b04b-7a11-49c6-85cf-e948d1aec1fd.JPG)


![sc-17](https://user-images.githubusercontent.com/73602443/221089707-ea74faae-46fe-49fe-8a02-222d682dcc2f.JPG)


Using command Line, see s3 buckets 

![sc-18](https://user-images.githubusercontent.com/73602443/221089758-195089c8-26cc-470d-874a-608883f2301f.JPG)


Access the file from the EC2 instance using the AWS Command Line Interface (AWS CLI). 

![sc-20](https://user-images.githubusercontent.com/73602443/221090001-71b03048-e664-448f-800d-192de423ed0e.JPG)



To View the file Content, in Windows we use more command. 

		more <filename> 

![sc-19](https://user-images.githubusercontent.com/73602443/221089784-d2fdea41-3909-4c39-8033-e587a6091148.JPG) 

 

Note: - 

If you Face this type of error 

Unknown options: ... 

![sc-14](https://user-images.githubusercontent.com/73602443/221090075-91a4f5bb-b2ae-4a43-8b0e-f6169c2c90f8.JPG)

 

The one of Solution of this error is, 

Check there are no spaces in your filename. 

To remove Space, just simply Rename the file Name. 

Click on Actions Tab and Rename the File Name. 

 

![sc-15](https://user-images.githubusercontent.com/73602443/221090127-8fe6efd5-e438-42c1-8c52-2eabfdc40433.JPG)


 

Read more about S3 using aws-cli here 

Task-02 

 

What is Snapshot? 

When you create an AMI of an existing EC2 instance, a snapshot is taken of all the volumes that are attached to the instance. The snapshot includes the device mappings. 

You can’t use snapshots to launch a new instance, but you can use them to replace volumes on an existing instance. If you experience data corruption or a volume failure, you can create a volume from a snapshot that you have taken and replace the old volume. You can also use snapshots to provision new volumes and attach them during a new instance launch. 

 

Create a snapshot of the EC2 instance and use it to launch a new EC2 instance. 

Click on snapshots option present inside EBS. 

![sc-21](https://user-images.githubusercontent.com/73602443/221090201-fda33485-dcbc-4c84-bb95-ed287e9b92f5.JPG


Select Resource Type (Instance). 

![sc-22](https://user-images.githubusercontent.com/73602443/221090249-047d8065-89c9-4679-8513-d6b33d5e7e15.JPG)



The Snapshots is Created Successfully. 

![sc-23](https://user-images.githubusercontent.com/73602443/221090365-fdae6c0d-6e1d-4d70-a2aa-4104ac3b2a78.JPG


Now we need to create an Image from this snapshot. Select this snapshot and click on the action button to select create an image from snapshot 

![sc-24](https://user-images.githubusercontent.com/73602443/221090402-93129a06-b596-4486-983e-e819b4cca51a.JPG

![sc-25](https://user-images.githubusercontent.com/73602443/221090430-bd3bf239-654b-4dba-8c68-f3bdde532053.JPG)

 

Image is created. 

![sc-26](https://user-images.githubusercontent.com/73602443/221090485-4930aac9-f0df-4d7d-a829-fedebd40f22e.JPG)


To see Images, lick on AMI Option. 

![sc-27](https://user-images.githubusercontent.com/73602443/221090508-7417998d-2a63-4e6f-a0db-a3233fff439d.JPG)


Detailed information of AMI’s. 

![sc-28](https://user-images.githubusercontent.com/73602443/221090543-3c607863-e9ab-46b7-a8a9-07bc73a1c86f.JPG)


Create Instance Using this newly created image. 

Select your image and click on Launch Instance. 

![sc-29](https://user-images.githubusercontent.com/73602443/221090604-caadda92-ac50-4d13-bdd6-d8fcf6cb9b62.JPG)


If the instance is connected via ssh, make sure to replace 'root' with 'ubuntu' 

![sc-30](https://user-images.githubusercontent.com/73602443/221090638-105e22d2-742c-4b79-acbd-a5a1a8cdd3df.JPG)


Download a file from the S3 bucket using the AWS CLI. 

Verify that the contents of the file are the same on both EC2 instances. 

![sc-31](https://user-images.githubusercontent.com/73602443/221090667-b4b0759e-81aa-444d-8bc8-06a83e24f731.JPG)


Happy Learning :) 

 
