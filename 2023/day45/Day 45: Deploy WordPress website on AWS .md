Day 45: Deploy WordPress website on AWS 

 

Over 30% of all websites on the internet use WordPress as their content management system (CMS). It is most often used to run blogs, but it can also be used to run e-commerce sites, message boards, and many other popular things. This guide will show you how to set up a WordPress blog site. 

Task-01 

 

As WordPress requires a MySQL database to store its data, create an RDS as you did in Day 44 

To configure this WordPress site, you will create the following resources in AWS: 

An Amazon EC2 instance to install and host the WordPress application. 

An Amazon RDS for MySQL database to store your WordPress data. 

Set up the server and post your new WordPress app. 

 

For setting up the DB, search RDS. 

You can see the RDS Dashboard. 

![1](https://user-images.githubusercontent.com/73602443/221396568-232f0012-9910-48a8-b121-81766198ab72.JPG)

	 

Click on Create Database. 

Select Database creation method I.e. (Standard create), also choose engine as MySQL. 

![2](https://user-images.githubusercontent.com/73602443/221396581-335c9ad9-6540-4b2c-8887-4cc699f1841b.JPG)


Before choosing MySQL version, first check the current WordPress version compatibility. 

	 
![3](https://user-images.githubusercontent.com/73602443/221396588-b30e47f6-de3c-4ace-b086-652e4e6c26f1.JPG)

Select the MySQL version. 

	 
![4](https://user-images.githubusercontent.com/73602443/221396596-b74ee521-52ac-4a22-a745-c83718b11d21.JPG)

Give username and set the password. 

![5](https://user-images.githubusercontent.com/73602443/221396608-ce1d8398-3b10-4b96-9026-15da66c1bb86.JPG)


For Setting up a connection to an EC2 instance, Select Connect to an EC2 compute resource option 

![6](https://user-images.githubusercontent.com/73602443/221396627-84d84ffa-a054-4244-b1c1-1699f1655550.JPG)


	Launch an EC2 Instance. 

	 
![7](https://user-images.githubusercontent.com/73602443/221396648-2aff95f5-fb9c-481e-9a7d-0f137640d27c.JPG)

![8](https://user-images.githubusercontent.com/73602443/221396667-b510aa46-da05-46d0-b839-975effb99e26.JPG)
![9](https://user-images.githubusercontent.com/73602443/221396677-75115007-20bf-4998-a20e-d7f628793462.JPG)


	Use User Data Option to install Apache Web Server. 

![10](https://user-images.githubusercontent.com/73602443/221396686-36bb6819-5b64-4b45-99be-f6fdc5b8f956.JPG)


	Your Instance is Running. 

![11](https://user-images.githubusercontent.com/73602443/221396691-4794f787-7151-4238-924a-ac7e01a9e57f.JPG)


	Add Your EC2 Instance as the compute resource for this Database.  

![12](https://user-images.githubusercontent.com/73602443/221396695-1c34ddbe-df06-4bc9-b341-7390b18d0361.JPG)


	Select SG (Security Group). Recommendation is chosen same as EC2 used. 

![13](https://user-images.githubusercontent.com/73602443/221396705-1e0e35e3-619a-479f-bb95-d5877f283743.JPG)


	Click on the Create Database Button. 

![14](https://user-images.githubusercontent.com/73602443/221396721-45fda5ac-eb9c-49ab-852a-1d68052c7663.JPG


	Copy the Public address and hit on the browser. Your Web server is Running. 

![15](https://user-images.githubusercontent.com/73602443/221396730-70557d80-2c49-467e-8498-d692c469b477.JPG)


	Make a WordPress Directory and download all WordPress files from Remote to local, using wget 	command. 

![16](https://user-images.githubusercontent.com/73602443/221396748-47082c0f-104a-456d-9c3e-74dc65af5d16.JPG)


	After Downloading these files, using ls command see all new files are available. 

![17](https://user-images.githubusercontent.com/73602443/221396756-b44103c5-fc36-483c-a7b6-18b898f8e809.JP


	Move WordPress folder to Webserver Default Location I.e., /var/www/html/ 

![18](https://user-images.githubusercontent.com/73602443/221396764-01abc6cd-8cf7-4548-a937-cfc7c4602968.JPG)


	Install MySQL client command to interact with MySQL server. 

![19](https://user-images.githubusercontent.com/73602443/221396777-7bf68ed0-3a3c-44f2-8e83-02cb4d2ce070.JPG)


	Below is shown as RDS host address. 

	Click on Database instance name. Inside Connectivity & security tab, you can find this 	address. 

![20](https://user-images.githubusercontent.com/73602443/221396797-06c056c9-413e-4985-ad59-431e817a5ba2.JPG)


	Using the command below to connect with MySQL Server. 

	mysql -h <Host Address> -P <DB Port No.> -u <Username> -p 

![21](https://user-images.githubusercontent.com/73602443/221396808-aea7805b-9123-4b9e-8845-638f5dcd6d98.JPG)


	Go to EC2 instance and allow port 3306 to Anywhere. 

![22](https://user-images.githubusercontent.com/73602443/221396819-0a6945b6-c93c-4f46-83e2-f85f1d22db74.JPG


	Install Php because WordPress is working on Php. 

![23](https://user-images.githubusercontent.com/73602443/221396831-a4c8ece0-d7ea-4dda-a97e-125c6f363c89.JPG)


	Copy the Public Address and hit on browser.  

Public Address /WordPress (Folder Name) 

	Your WordPress Setup is started. 
  
![24](https://user-images.githubusercontent.com/73602443/221396850-427e8006-e28f-43a7-abb1-9bbbd08c08d1.JPG)

 

	For the next step you need DB Name, go to RDS Dashboard, go to configuration Tab and 	see DB Name. 

![25](https://user-images.githubusercontent.com/73602443/221396861-3a5bbcfb-435a-44bd-a842-3dd7bf5d2eb7.JPG


	If DB Name is not there, create a DB, using Below Command. 

![26](https://user-images.githubusercontent.com/73602443/221396903-496b0a08-17cc-4c71-9caa-104febbaf897.JPG)

Add necessary information and click on the submit button. 

	
![28](https://user-images.githubusercontent.com/73602443/221396941-36e5b6de-c49a-4722-a1f3-edde9caf7455.JPG)

	It shows some errors. 

	Copy all content and create a wp-config.php file inside WordPress folder. 

	

![29](https://user-images.githubusercontent.com/73602443/221396973-8fa8ae00-51dc-474c-82b0-d0243600014b.JPG


	Add Above file content into wp-config.php file. 



![30](https://user-images.githubusercontent.com/73602443/221397023-46c583a1-eb1f-4072-b27a-0ff6cb74a76b.JPG)

![31](https://user-images.githubusercontent.com/73602443/221397016-125c7dd0-015e-4598-9792-c8b09b4ce1cb.JPG


	Hey!!!  Your WordPress has been Installed. 

	 
![32](https://user-images.githubusercontent.com/73602443/221397010-cc05befa-3660-472c-8b80-1f5dfeac02c5.JPG)

	 
![33](https://user-images.githubusercontent.com/73602443/221397008-d04ea4ec-cdad-4f44-9c52-26a794e67ca2.JPG)

 

 
