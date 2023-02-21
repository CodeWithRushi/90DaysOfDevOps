Day 41: Setting up an Application Load Balancer with AWS EC2 🚀 ☁ 

 

 ![Attachment-1](https://user-images.githubusercontent.com/73602443/220233745-307d9c8e-f4d9-4f30-ae9f-675064b06d30.JPG)


LB2 

Hi, I hope you had a great day yesterday learning about the launch template and instances in EC2. Today, we are going to dive into one of the most important concepts in  

EC2: Load Balancing. 

 

What is Load Balancing? 

Load balancing is the distribution of workloads across multiple servers to ensure consistent and optimal resource utilization. It is an essential aspect of any large-scale and scalable computing system, as it helps you to improve the reliability and performance of your applications. 

Elastic Load Balancing: 

Elastic Load Balancing (ELB) is a service provided by Amazon Web Services (AWS) that automatically distributes incoming traffic across multiple EC2 instances. ELB provides three types of load balancers: 

Read more from here 

Application Load Balancer (ALB) - operates at layer 7 of the OSI model and is ideal for applications that require advanced routing and microservices. 

Read more from here 

Network Load Balancer (NLB) - operates at layer 4 of the OSI model and is ideal for applications that require high throughput and low latency. 

Read more from here 

Classic Load Balancer (CLB) - operates at layer 4 of the OSI model and is ideal for applications that require basic load balancing features. 

Read more here 

 

🎯 Today's Tasks: 

 

Task 1: 

launch 2 EC2 instances with an Ubuntu AMI and use User Data to install the Apache Web Server. 

Login to your EC2 Dashboard and click on Launch Template. 

 ![sc-1](https://user-images.githubusercontent.com/73602443/220233821-9b7ae444-32f0-4543-bac2-bd0e0fb6860e.JPG)


Select Ubuntu as an AMI with t2. micro as an Instance Type. 

 ![sc-2](https://user-images.githubusercontent.com/73602443/220233850-782cf595-2e64-4647-b8ef-8e2d715d2623.JPG)


Add Apache server installing script inside User Data Block. 

 ![sc-3](https://user-images.githubusercontent.com/73602443/220233870-bf506edd-4195-4c65-b60c-26ddd9b7b850.JPG)


Template Is Created. 

 ![sc-4](https://user-images.githubusercontent.com/73602443/220233887-f3792561-191c-4d24-8e9c-63397b3f67c9.JPG)


Select Template and click on Launch Instance. 

 ![sc-5](https://user-images.githubusercontent.com/73602443/220233902-aa5d60b3-2772-4820-bf7f-452c3ea0efd3.JPG)


Here, we specify No.of Instances we want to create. 

 ![sc-6](https://user-images.githubusercontent.com/73602443/220233925-d20e101a-7764-4b13-8ce1-fa84c73ede6f.JPG)


Allow Port 80 in SG (Security Group) to run an app on the internet. 

 ![sc-7](https://user-images.githubusercontent.com/73602443/220233935-4cb14232-a385-40dd-89f9-0922231e20a9.JPG)


Paste EC2 Public Ip address:<port no> to browser 

Hey, our Apache Server is Running. 

 ![sc-8](https://user-images.githubusercontent.com/73602443/220233977-cca87244-bcde-4fe6-8ff7-a34f9592b2b7.JPG)


Modify the index.html file to include your name so that when your Apache server is hosted, it will display your name also do it for 2nd instance which include " TrainWithShubham Community is Super Awesome :) ". 

Copy the public IP address of your EC2 instances. 

Open a web browser and paste the public IP address into the address bar. 

You should see a webpage displaying information about your PHP installation. 

 

If you are not able to write custom content inside var/www/html/index.html. 

Then simply you change the permission using chmod command. 

		sudo chmod 477 index.html 

 
![sc-9 1](https://user-images.githubusercontent.com/73602443/220234045-cf72e1b6-4c48-4ba1-a373-6da24cf86e54.JPG)

First Instance Running after adding some Custome content inside index.html. 

 ![sc-9](https://user-images.githubusercontent.com/73602443/220234057-1c5f979d-6e1e-4e74-9d39-990d8f0278f9.JPG)


Second Instance Running after adding some Custome content inside index.html. 

 
![sc-10](https://user-images.githubusercontent.com/73602443/220234065-366939b1-d4b0-4887-afa9-352c46b419e1.JPG)

 

Task 2: 

Create an Application Load Balancer (ALB) in EC2 using the AWS Management Console. 

Click on Load Balancer option on the left side and create a Load Balancer. 

 
![sc-11](https://user-images.githubusercontent.com/73602443/220234087-552486c8-cdc6-407d-889a-f17521e492e0.JPG)

Add EC2 instances which you launch in task-1 to the ALB as target groups. 

 ![sc-12](https://user-images.githubusercontent.com/73602443/220234110-cd66abd3-d150-4ef4-99b7-ef6667c5b6c7.JPG)


Add ALB Name and add some AZ. 

 ![sc-13 1](https://user-images.githubusercontent.com/73602443/220234126-d76df56a-6ef4-439b-97a2-04d3ff338c35.JPG)


 ![sc-13 2](https://user-images.githubusercontent.com/73602443/220234157-7eaf88bc-de0b-4edd-96c9-09305e56422e.JPG)


Configure Security Groups. Add HTTP type and Port Range is 80. 

 ![sc-14](https://user-images.githubusercontent.com/73602443/220234169-1d5db843-59a9-46ad-896f-f06adf87634b.JPG)


Add TargetGroupName and Target Type is Instance. 

 ![sc-15](https://user-images.githubusercontent.com/73602443/220234184-31e98e95-11ed-4538-a8b5-56e7ad4366ba.JPG)

![sc-16](https://user-images.githubusercontent.com/73602443/220234219-9ef16e71-93ab-4350-b768-6d420d7c0234.JPG)
 

Select all Available EC2 Instances and click on Add to Registered Targets option to register all instances. 

 ![sc-17](https://user-images.githubusercontent.com/73602443/220234501-b01de252-537a-4bba-a6e9-ab863568ce1f.JPG)



Review the All Configurations. 

 ![sc-18](https://user-images.githubusercontent.com/73602443/220234503-e4905ec6-9bf0-4fd5-8bd2-7e8b66f12410.JPG)


Load Balancer is Created Successfully. 

 ![sc-19](https://user-images.githubusercontent.com/73602443/220234525-1a3de68a-ae15-4fc8-b570-1fdc541470a9.JPG)


Check the Instances Health inside Target Tabs. The Status is Healthy. 

 ![sc-20](https://user-images.githubusercontent.com/73602443/220234536-b498ccd6-8abd-4466-ac64-57f46cabf85e.JPG)


Verify that the ALB is working properly by checking the health status of the target instances and testing the load balancing capabilities. 

LoadBalancer 

Copy The Load Balancer DNS Name and Paste it on your Browser. 

 ![sc-21](https://user-images.githubusercontent.com/73602443/220234606-feab5d12-8bc9-45b3-b3a5-fe032e91ffac.JPG)


See, first time we redirect to second instance webpage using same DNS name. 

 ![sc-22](https://user-images.githubusercontent.com/73602443/220234635-5391d685-dfe7-4b0f-a266-2980726b420d.JPG)


See, second time we redirect to first instance webpage using same DNS name. 

 
![sc-23](https://user-images.githubusercontent.com/73602443/220234646-842b313b-8e65-442c-a0d3-af2c94d6b754.JPG)

 

 

Happy Learning! 😃 

 
