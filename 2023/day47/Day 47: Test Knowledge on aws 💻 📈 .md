Day 47: Test Knowledge on aws 💻 📈 

 

Today, we will be testing the aws knowledge on services in AWS, as part of the 90 Days of DevOps Challenge. 

Task-01 

Launch an EC2 instance using the AWS Management Console and connect to it using SSH. 

	 
![1](https://user-images.githubusercontent.com/73602443/222602048-d7a362df-a8e0-41ff-a1c5-a8003d898d0d.JPG)

Install a web server on the EC2 instance and deploy a simple web application. 

	Add below script in User Data, to install Apache server. 

![2](https://user-images.githubusercontent.com/73602443/222602014-43ca991b-2bb6-4611-b562-133ab702d865.JPG)


	Click on Connect Button to connect the instance. 

	 
![3](https://user-images.githubusercontent.com/73602443/222601974-b4be343e-ba55-4144-ac0a-4a32f25be752.JPG)

	Copy the ssh Address to connect with local cmd. 

	 
![4](https://user-images.githubusercontent.com/73602443/222601926-b947421d-b693-4c1c-9cc1-dc7152da08ac.JPG)


	Go to private key-value file location, and paste the address. 

![5](https://user-images.githubusercontent.com/73602443/222601863-916b3abe-6e99-4c96-94bf-b52cf26c99ee.JPG)


	Go to /var/www/html path and change the Apache Default index.html page. 

![6](https://user-images.githubusercontent.com/73602443/222601749-23136d58-e496-4888-8191-1e7032326d7d.JPG)


	Paste the Public Ip address on Browser and hit enter, your web app is Running. 

![7](https://user-images.githubusercontent.com/73602443/222601587-bd00a6c8-8206-4bce-913f-505dfd7a09ff.JPG)


Monitor the EC2 instance using Amazon CloudWatch and troubleshoot any issues that arise. 

	In AWS, for Monitoring Purpose, we use AWS CloudWatch. 

	Click on create alarm. 

![8](https://user-images.githubusercontent.com/73602443/222601471-c88456fc-6e25-4a04-a1db-db3d4f0e402b.JPG)


	Click on select metrics. 

![9](https://user-images.githubusercontent.com/73602443/222601374-e079c27c-ffb2-4067-89f3-9fd374064c1b.JPG)


	Click on EC2 metrics. 

![10](https://user-images.githubusercontent.com/73602443/222601323-5d193b3c-400f-48fc-b00a-e7a60185319c.JPG)


	Click on Pre-instance Metrics and Select any metrics like CPUUtilization ,  

Disk Space,etc. 

![11](https://user-images.githubusercontent.com/73602443/222601199-5574d84b-f042-45c8-9f08-97fa3dc0fdef.JPG)


![12](https://user-images.githubusercontent.com/73602443/222601225-3c970e22-2b25-418f-b216-eb17e5bc10df.JPG)


	Specify the Threshold Value, when CPU Utilization reaches a threshold value number, it gives 	alarm .	 

![13](https://user-images.githubusercontent.com/73602443/222601117-11b096ba-f7dd-4b39-8d48-8ac171edaf90.JPG)


	Review and Create an Alarm. 

	 
![14](https://user-images.githubusercontent.com/73602443/222600985-40977ccf-3e23-468f-854a-62d5d2bfac49.JPG)

![30](https://user-images.githubusercontent.com/73602443/222600860-d15c7750-ef32-43fd-aa76-acc57656174e.JPG)

 

Task-02 

Create an Auto Scaling group using the AWS Management Console and configure it to launch EC2 instances in response to changes in demand. 

	Auto-Scaling Needs Template, so we create our first Temple. 

	Click on Actions Tab and click on Image and Template and select Create Template from 	Instance.  

![16](https://user-images.githubusercontent.com/73602443/222600705-3d1d5db0-5d1a-4c1e-945d-568e7b07b497.JPG)
	 

	Add Template Name and fill in all necessary Info and click Create Launch Template. 

![17](https://user-images.githubusercontent.com/73602443/222600646-0d6dbeb9-7c3c-4987-b8aa-b857e8720200.JPG)


![18](https://user-images.githubusercontent.com/73602443/222600576-6ca6034f-4c85-4ae4-8b62-7065abe96446.JPG)


	Template is created. 

![19](https://user-images.githubusercontent.com/73602443/222600431-f505482d-47cd-4ef5-a9b2-a2ff74327285.JPG)


	Click on below Auto-Scaling Option 

![20](https://user-images.githubusercontent.com/73602443/222600267-839e0633-f07d-42d8-8fbb-3ad2a3dec768.JPG)


	Add Auto-scaling name and select Template name. 

![21](https://user-images.githubusercontent.com/73602443/222600161-23db57ce-f696-415a-a69f-73621746de78.JPG)

![22](https://user-images.githubusercontent.com/73602443/222600016-fb1f94e7-5115-41d3-9da4-ad7613442934.JPG)


	Set the Desired, minimum and Maximum Capacity. 

![23](https://user-images.githubusercontent.com/73602443/222599942-da04ae58-6772-4db9-b743-4a6bae015f32.JPG)
 

	For changing on demand purpose, we use Scaling Policies Option. 

	Select Metric type. 

![24](https://user-images.githubusercontent.com/73602443/222599862-9cd5db49-2638-4bf0-9253-4eae1e906d4f.JPG)


![25](https://user-images.githubusercontent.com/73602443/222599808-777ba88a-32eb-4a66-bd74-7dcda9e587f2.JPG)


	The instances are Running. 

![26](https://user-images.githubusercontent.com/73602443/222599757-1373f54a-499c-42fc-a917-968018adac22.JPG)
 

Use Amazon CloudWatch to monitor the performance of the Auto Scaling group and the EC2 instances and troubleshoot any issues that arise. 

	For Using CloudWatch to monitor, we have two ways to enable auto-scaling monitor. 

	1] click on autoscaling name and enable auto-scaling group metrics option. 

![32](https://user-images.githubusercontent.com/73602443/222599670-0c76929a-9795-4966-b3d7-d8c9829a0dbc.JPG)


	2] Goto CloudWatch and create alarm. 

![33](https://user-images.githubusercontent.com/73602443/222599605-0605e18d-bf06-484d-9a64-f11d4e7cde80.JPG)


	Select By Auto-Scaling Group Metrics. 

![34](https://user-images.githubusercontent.com/73602443/222599522-922451b3-3b12-4f37-9ff4-ad6217dcc96f.JPG)


	Specify the threshold type and value.  

![35](https://user-images.githubusercontent.com/73602443/222599444-44504787-64a4-4045-bc46-32921cf0c37c.JPG


	See, when our condition is satisfied, it shows alarm in state. 

	 
![36](https://user-images.githubusercontent.com/73602443/222599355-038ff151-94bb-4740-8d98-75c7734e3cf1.JPG)

![31](https://user-images.githubusercontent.com/73602443/222599180-b8959987-8826-4555-8076-d55b69a6607a.JPG)

 

Use the AWS CLI to view the state of the Auto Scaling group and the EC2 instances and verify that the correct number of instances are running. 

	For AWS CLI, in Windows you need to install AWS-CLI package, after that check 	AWS-CLI version. 

![42](https://user-images.githubusercontent.com/73602443/222598870-0a7b4010-4c7d-4b38-8770-22f860c17201.JPG)


	First Create Access key for Root User. 

	Click on the Manage Access Key, to create the Access key. 

![39 1](https://user-images.githubusercontent.com/73602443/222598476-c45384c8-2725-45cc-8e99-117a9c9b2282.JPG

![39](https://user-images.githubusercontent.com/73602443/222598380-56ceade2-3dce-401a-b6c0-b790cfa9cdaa.JPG)

	 
![40](https://user-images.githubusercontent.com/73602443/222598326-f1ecbfb5-8c53-4287-ab52-81d1a43fdbbe.JPG)

	 

	Use this region us-east-1 

 ![41](https://user-images.githubusercontent.com/73602443/222598267-c5ec436d-ee0d-405b-9b06-6c6354ee0a96.JPG)


	Use aws –configure command to configure AWS-CLI, 

	It is asking Authentication password, secret password,region,etc. 

 
![43](https://user-images.githubusercontent.com/73602443/222597894-d3c78cec-07e4-4fa5-835c-e17572a7835f.JPG)

	 

	Check Auto-scaling state 

	aws autoscaling describe-auto-scaling-groups 


![44](https://user-images.githubusercontent.com/73602443/222597831-af58909b-e119-47f0-b5ec-3ad458edeff4.JPG)

	Check EC2 Instance state 

	aws ec2 describe-instances 

	 

	 
![45](https://user-images.githubusercontent.com/73602443/222597729-0d9a3e30-a18f-41d8-988e-3513c93607b5.JPG)

	 

We hope that these tasks will give you hands-on experience with aws services and help you understand how these services work together. If you have any questions or face any issues while doing the tasks, please let us know. 

Happy Learning 😊 

 

 

 
