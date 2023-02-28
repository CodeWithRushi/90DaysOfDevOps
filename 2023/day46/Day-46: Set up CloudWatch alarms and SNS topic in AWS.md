Day-46: Set up CloudWatch alarms and SNS topic in AWS 

 

Hey learners, you have been using aws services atleast for last 45 days. Have you ever wondered what happen if for any service is charging you bill continously and you don't know till you loose all your pocket money ? 

Hahahaha😁, Well! we, as a responsible community ,always try to make it under free tier , but it's good to know and setup something , which will inform you whenever bill touches a Threshold. 

What is Amazon CloudWatch? 

Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. 

![1](https://user-images.githubusercontent.com/73602443/221724420-72639695-4d5e-45dc-9382-7e088761a523.JPG)
 

Read more about cloudwatch from the official documentation here 

What is Amazon SNS? 

Amazon Simple Notification Service is a notification service provided as part of Amazon Web Services since 2010. It provides a low-cost infrastructure for mass delivery of messages, predominantly to mobile users. 

Read more about it here 

Why we need Cloud Based Monitoring? 

Cloud monitoring is the practice of measuring workloads inside cloud tenancies against specific metrics and thresholds. 

Cloud monitoring allows you to find out if your cloud-hosted applications are performing within their Service-Level Agreement (SLA), discover any potential security risks, identify any capacity issues, and analyze costs. 

Cost optimization 

By monitoring cloud, we can track resource utilization and, from there, optimize cost. 

Performance 

Discovering the  cloud-based applications running status. 

Security 

Cloud monitoring can help you with security. By examining the application, server, API gateway, or firewall logs, a monitoring solution can alert you of anomalies 

 

Amazon CloudWatch Events: 

Amazon CloudWatch Events is a part of Amazon CloudWatch which delivers “a real time stream of system events” that allows you to monitor and respond to the changes in your AWS Resources. 

Amazon CloudWatch Logs: 

Amazon CloudWatch Logs is used to monitor, store and access log files from AWS resources like Amazon EC2 instances, and Others. 

 

 

Task: 

Create a CloudWatch alarm that monitors your billing and sends an email to you when it reaches $2. 

(You can keep it for your future use) 

	For Starting CloudWatch Alarm, search CloudWatch. 

	You Will redirect to CloudWatch Dashboard 

![2](https://user-images.githubusercontent.com/73602443/221724484-71df4306-5778-450d-b0f8-dbbff6bb47ab.JPG)
![3](https://user-images.githubusercontent.com/73602443/221724554-0dbb2704-b525-4642-a627-7b95ee66098e.JPG)

	Click on Create Alarm. 


![4](https://user-images.githubusercontent.com/73602443/221724594-4d60f87a-392c-44a9-9547-45f5e04062e6.JPG)

	Click on Select metric. 


![5](https://user-images.githubusercontent.com/73602443/221724615-3ae00ae9-8351-4028-a422-dffd1747ebfa.JPG)

	See, you are not able to find the Billing option. 


![6](https://user-images.githubusercontent.com/73602443/221724661-bfcfb5c2-1082-450a-a4a2-8fda99e7f496.JPG)

	Goto Dashboard, search Billing. 

	Inside Billing Dashboard, click on Billing Preferences option 

	Check the checkbox Receive Billing Alerts. 


![7](https://user-images.githubusercontent.com/73602443/221724685-c7b66672-86ef-42cb-a179-e159074b5be7.JPG)

	Again,come back to CloudWatch Dashboard, Inside Metrics now you will find the 	Billing Option. 



![8](https://user-images.githubusercontent.com/73602443/221724722-bb3f6ffb-f5d3-4cfb-82d9-af62a0a77b8b.JPG)

	Click on Total Estimated Charge 
  

![9](https://user-images.githubusercontent.com/73602443/221724754-4060c446-f515-4f34-9574-7429611362c1.JPG)


	Check the checkbox and click on select metrics. 

![10](https://user-images.githubusercontent.com/73602443/221724825-e9a9717a-bd70-44d4-a824-ab9469700332.JPG)

	Here we set the Threshold value. 



![11](https://user-images.githubusercontent.com/73602443/221724851-353f05e4-5883-49e5-a679-677d258a8633.JPG)

	Set Threshold Type and value. 


![12](https://user-images.githubusercontent.com/73602443/221724883-df18d6e1-b060-42b5-a32b-dd8d2b00aff8.JPG)

	For Notification, click on Add Notification. 

	 
![13](https://user-images.githubusercontent.com/73602443/221724968-79c5aa1e-2d7c-4e45-9890-313579c59e78.JPG)


	Currently we don’t have any topic, so click on create new topic. 

	Add Topic name and Endpoint Email Address. 


	 
![14](https://user-images.githubusercontent.com/73602443/221724983-8f19e32d-84a1-4f75-a9dd-8aa15d28ade8.JPG)

![15](https://user-images.githubusercontent.com/73602443/221725007-c4263516-e875-4703-9719-10e137b6c31d.JPG) 

	Set AlertName and click on Next Button. 

![16](https://user-images.githubusercontent.com/73602443/221725036-2657d39c-bc3a-4fa5-bf34-8d0477a5623c.JPG)

	See, our Threshold value is set.  


![17](https://user-images.githubusercontent.com/73602443/221725101-dea76e2f-36cd-4775-b2d5-c911c375c6af.JPG)


![18](https://user-images.githubusercontent.com/73602443/221725173-2cc7311b-7062-4198-bd17-72cc623c7a7d.JPG)
	Click on Create Alarm. 




![19](https://user-images.githubusercontent.com/73602443/221725222-9847e2f0-8e5e-4c4b-b9fe-1a0a3f11c278.JPG)

	See our Alarm is set, but we got one warning. 

	I.e. SNS Subscription is Pending. 

	So let’s go ahead and complete the Procedure. 

	 

	 
![20](https://user-images.githubusercontent.com/73602443/221725236-c4712f6a-a74a-46a9-965c-c2ace61cf0c2.JPG)


![21](https://user-images.githubusercontent.com/73602443/221725282-bdb0c075-b793-4a92-af9c-8625f653280a.JPG) 

	Go to Gmail, in the spam section you will find this Confirmation mail. 

	Confirm subscription. 



![22](https://user-images.githubusercontent.com/73602443/221725313-60dda718-94cc-4d12-a124-be8200c94b6f.JPG)

![23](https://user-images.githubusercontent.com/73602443/221725484-e8669e56-594a-4cf0-8197-d1da78224306.JPG)

	 

	Refresh the page, see Your subscriptions is confirmed. 

![24](https://user-images.githubusercontent.com/73602443/221725377-e3fab599-ce71-4d29-861d-8bd16ea72c30.JPG)

	 

Delete your billing Alarm that you created now. 

	 
![25](https://user-images.githubusercontent.com/73602443/221725412-489a681a-69a5-44bf-9a3f-3e8e30e875f6.JPG)

![26](https://user-images.githubusercontent.com/73602443/221725428-82a06a11-fe41-4b6e-af13-1d32fcfc3614.JPG)


(Now you also know how to delete as well. ) 

Need help with Cloudwatch? Check out this official documentation for assistance. 

Keep growing your AWS knowledge💥🙌 

Happy Learning! :) 

 
