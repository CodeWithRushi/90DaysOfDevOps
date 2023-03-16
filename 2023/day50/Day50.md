Day 50: Your CI/CD pipeline on AWS - Part-1 🚀 ☁ 

 

What if I tell you, in the next 4 days, you'll be making a CI/CD pipeline on AWS with these tools. 

CodeCommit 

CodeBuild 

CodeDeploy 

CodePipeline 

S3 

 

What is CodeCommit ? 

 

CodeCommit is a managed source control service by AWS that allows users to store, manage, and version their source code and artifacts securely and at scale. It supports Git, integrates with other AWS services, enables collaboration through branch and merge workflows, and provides audit logs and compliance reports to meet regulatory requirements and track changes. Overall, CodeCommit provides developers with a reliable and efficient way to manage their codebase and set up a CI/CD pipeline for their software development projects. 

Task-01: 

Set up a code repository on CodeCommit and clone it on your local. 

Go to AWS Dashboard, Search CodeCommit and click on Create Repository. 

![1](https://user-images.githubusercontent.com/73602443/225716250-e40a926a-5268-4739-a06b-cee025999aaf.JPG)


Add Repository Name and click on Create. 

![2](https://user-images.githubusercontent.com/73602443/225716317-41efefb0-c4fe-4e26-9a72-acb8a99ce21f.JPG)


See, You Successfully Create a Repository. 

For Setting Up your Connection, you need a one IAM User, Because AWS Not recommends you use Root Account. 

![3](https://user-images.githubusercontent.com/73602443/225716420-8f2b5773-a73a-4b8d-9fbb-30cba8da3563.JPG)


Search IAM in AWS Console and Create a New IAM User. 

![4](https://user-images.githubusercontent.com/73602443/225716481-69f5680e-d3ef-494b-a79b-434bb4eb45fb.JPG

![5](https://user-images.githubusercontent.com/73602443/225716551-4bf2a028-c628-4371-bade-2f1774adb72f.JPG)

 

Attach AWSCodeCommitFullAccess Policy to IAM User. 

![6](https://user-images.githubusercontent.com/73602443/225716616-3511b155-4715-40e2-9f62-5cea8482efe4.JPG


IAM USER is Created Successfully. 

![7](https://user-images.githubusercontent.com/73602443/225716682-08817404-c2c8-43b5-ba37-a5623d278c78.JPG)
 

Click On IAM User, and go to Security credentials Tab. 

![8](https://user-images.githubusercontent.com/73602443/225716815-108c5ee9-6755-46bc-b708-c04f9b72ead7.JPG)

 

You need to setup GitCredentials in your AWS IAM. 

Click on Generate Credentials to generate a username and password so you can use it to authenticate HTTPS connection to AWS CodeCommit repositories. 

![9](https://user-images.githubusercontent.com/73602443/225716889-899fca36-95de-40ef-9e00-9338d461ee32.JPG


Download Credentials. 

![10](https://user-images.githubusercontent.com/73602443/225716970-7afcb2fc-dc47-46dc-8567-2c2f80360f8a.JPG)


Click on Clone HTTPS to copy the Clone URL. 

![11](https://user-images.githubusercontent.com/73602443/225717048-d43a055d-ffe9-48b8-9271-1a74ccf8bf6f.JPG)


Use those credentials in your local and then clone the repository from CodeCommit 

You will be prompted to enter your Git credentials. Enter the username and password that you downloaded earlier. 

![12](https://user-images.githubusercontent.com/73602443/225717117-19b4c237-8786-4879-bd3b-4bbc0036b98a.JPG)


Use dir, to see all available directories in Windows. 

![13](https://user-images.githubusercontent.com/73602443/225717191-dfc33a3f-23b3-4097-8bae-316ec849ce5f.JPG)


Task-02: 

Add a new file from local and commit to your local branch 

![14](https://user-images.githubusercontent.com/73602443/225717267-61592a7b-d4bf-4533-8588-5bdc2918da29.JPG)


![15](https://user-images.githubusercontent.com/73602443/225717319-6033c08b-67ba-4f46-bfb2-8f0fb4c28c5b.JPG)


 

 ![16](https://user-images.githubusercontent.com/73602443/225717350-dc41b7f4-f9fe-4320-957d-3386e27f6e62.JPG)


 

Push the local changes to CodeCommit repository. 

![17](https://user-images.githubusercontent.com/73602443/225717408-9edc1fc6-f614-40f0-b47b-1b84294ea9c8.JPG)


Verify that the changes have been pushed to the CodeCommit repository: 

Go to the code commit repository that you created earlier, you should see the new file listed in the repository's files. 

 
![18](https://user-images.githubusercontent.com/73602443/225717462-b322cee2-2bf5-457c-a3d9-8ead0dd4fdc1.JPG)


 

Happy Learning :) 

 
