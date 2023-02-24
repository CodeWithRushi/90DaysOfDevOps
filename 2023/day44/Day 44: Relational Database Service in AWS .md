Day 44: Relational Database Service in AWS 

 

Amazon Relational Database Service (Amazon RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. 

 ![1](https://user-images.githubusercontent.com/73602443/221086772-a97e6b89-895a-4788-ac85-5e4531b9dc6a.png)


Task-01 

 

Create a Free tier RDS instance of MySQL 

![2](https://user-images.githubusercontent.com/73602443/221086806-62f6a40e-0347-416d-bc9e-b1234858728d.JPG)

Choose a Database creation method I.e., Standard Create. 

![3](https://user-images.githubusercontent.com/73602443/221086833-06afdd5a-f925-4ae6-8170-707eb861f35e.JPG)


	Select Free Tier Template 

	 
![4](https://user-images.githubusercontent.com/73602443/221086857-45acfa41-987b-4337-b910-47cdd9e17adb.JPG)

	Setting Up the Master Username and Password 
![5](https://user-images.githubusercontent.com/73602443/221086881-0bb74169-d00b-4cb5-a5c6-f4a81cf81854.JPG)

Choose Connectivity Option. 
![6](https://user-images.githubusercontent.com/73602443/221086901-02421108-9b77-4d7f-94a7-331a3e3e5d5e.JPG)


	Leave Other Option as it is. 

	 
![7](https://user-images.githubusercontent.com/73602443/221086980-24667366-a377-43a5-8890-ab84586459bd.JPG)

![8](https://user-images.githubusercontent.com/73602443/221087019-75f6dfa1-27b5-4920-b4da-d5557a8671d7.JPG)


Create an EC2 instance 

	 
![9](https://user-images.githubusercontent.com/73602443/221087051-57a1e74a-a3c4-4b62-b2c2-f6fff776f57b.JPG)



![10](https://user-images.githubusercontent.com/73602443/221087119-c87914ac-a2a5-4c1b-8f07-4a780ed7773f.JPG)

	Instance is Created Successfully. 
  
![11](https://user-images.githubusercontent.com/73602443/221087134-5d41dbee-7414-4079-b38d-9180936c1c36.JPG)

	Add MYSQL Port No 3306 into SG (Security Group) 

![12](https://user-images.githubusercontent.com/73602443/221087166-ce5b5b03-b6f2-42e0-9f1d-d55d381a6442.JPG)


Create an IAM role with RDS access 

	See the IAM Dashboard, I have Already 4 Roles Available. 

![13](https://user-images.githubusercontent.com/73602443/221087203-9aec333d-6127-485b-b93b-9ffb7ac4a27a.JPG)

	Adding a New Role 

![14](https://user-images.githubusercontent.com/73602443/221087215-321a0e95-faf0-4647-b8bb-efcbcfaf6eec.JPG)

	Add AWSRDSFullAccess Permission to this Role. 


![15](https://user-images.githubusercontent.com/73602443/221088237-ca11e88b-cb50-4506-837b-349587d8fafb.JPG)


	Give Role Name. 

![16](https://user-images.githubusercontent.com/73602443/221087281-67885888-832e-426d-b70c-5245a483f8ed.JPG)


![17](https://user-images.githubusercontent.com/73602443/221087313-8d6a9125-28e9-492f-bed0-3e0c47e56bb6.JPG)

Assign the role to EC2 so that your EC2 Instance can connect with RDS 

	Goto Actions Tab, select Security and click on Modify IAM Role. 

![18](https://user-images.githubusercontent.com/73602443/221087343-00df5c82-ad30-4034-ac96-12afd3a65243.JPG)

	Select Role Name. 

![19](https://user-images.githubusercontent.com/73602443/221087368-3f95ba55-fd0b-4ac1-92aa-a8bbe1ec8c82.JPG)

  	 

Once the RDS instance is up and running, get the credentials and connect your EC2 instance using a MySQL client. 


![20](https://user-images.githubusercontent.com/73602443/221087413-2cbc3b7e-dbdc-4e5f-ba2f-5211d1bd128e.JPG)

	For connecting MySQL, you need host name. 

	Goto RDS Page, in Connectivity & Security Tab, You Found Endpoint address I.e., host 	address. 

![21](https://user-images.githubusercontent.com/73602443/221088411-6f5c5582-fc73-4d0c-95ba-f14a338d096a.JPG)


	Successfully Connected to MYSQL SERVER. 

![22](https://user-images.githubusercontent.com/73602443/221088435-16a97d05-e272-438c-99d8-38e9255db82e.JPG)


Happy Learning:) 

 

 

 
