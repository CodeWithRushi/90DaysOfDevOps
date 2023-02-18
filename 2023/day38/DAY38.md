Day 38 Getting Started with AWS Basics☁ 


Congratulations!!!! you have come so far. Don't let your excuses break your consistency. Let's begin our new Journey with Cloud☁. By this time, you have created multiple EC2 instances, if not let's begin the journey: 

AWS: 

Amazon Web Services is one of the most popular Cloud Provider that has free tier too for students and Cloud enthusiasts for their Handson while learning (Create your free account today to explore more on it). 

Read from here 

IAM:  

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources. Read from here 

Get to know IAM more deeply Click Here!! 

 

Task 1: 

 

Create an IAM user with username of your own wish and grant EC2 Access. Launch your Linux instance through the IAM user that you created now and install Jenkins and docker on your machine via single Shell Script. 

 

In Search bar type IAM, then You will see below IAM Dashboard. 

 

 

This Step1, we have to specify user details. 

Mention Username and check the checkbox of AWS management console access type. 

Set Custome Password. 

 

Set one of the permission options. [Attach policies directly] 

And add AmazonEC2FullAccess policies to a User. 

 

Review and Create the User. 

 

Now, user is created successfully.  

 Download the Download.csv file, because you will need these to authenticate your IAM user when launching instances. 

 

Open Download.csv file. This file contains username, Password and Console sign-in URL. 

 

 

To launch a Linux instance using your IAM user, follow these steps: 

Sign in AWS account as IAM user which we created above. 

 

 

 

Change the Default Password. 

 

Now we successfully logged in as a IAM User, with Username is Avergers1. 

 

First check you have any other permission access? 

When you try to use other service, you will get error. 

 

Go to the EC2 service and click on "Launch instance". 

Choose a Linux AMI. 

 

 

 

Using below script, we will install Jenkins and docker. 

#!/bin/bash 

sudo apt update && sudo apt-get install docker.io -y 

sudo apt install default-jre -y 

sudo apt install default-jdk -y 

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add - 

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' 

 

sudo apt update 

sudo apt install jenkins -y 

sudo systemctl status jenkins 

 

Task2: 

 

In this task you need to prepare a devops team of avengers. Create 3 IAM users of avengers and assign them in devops groups with IAM policy. 

Go To IAM Dashboard 

 

Create a 3 Users and, now we use Copy Permissions Options. 

 

 

 

Create a avengers devops group by clicking on the "User Groups" link in the left-hand menu and clicking on the "Create New Group" button. 

 

Enter the Groupname and add 3 users to a DevOps Group. 

 

Group is created and added 3 users to this group. 

 

 

 

 

 

Thank you for reading! 

 
