**Day 28 Task: Jenkins Agents** 

Jenkins uses a Master-Slave architecture to manage distributed builds. In this architecture, Master and Slave communicate through TCP/IP protocol. 

To run heavy projects which gets build on a regular basis is not a good option. 

In such a scenario, need to off load, load from Master by configuring more slaves. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.001.png)

Distributed builds are used to absorb extra load or to run specialized build jobs in a specific operating system or environments. 

Jenkins slaves are generally required to provide the desired environment. They work on the basis of requests received from Jenkins master. 

**Jenkins Master (Server): -** 

Jenkins’s server or master node holds all key configurations. Jenkins master server is like a control server that orchestrates all the workflow defined in the pipelines. For example,  

- Scheduling build jobs. 
- Dispatching builds to the slaves for the actual execution. 
- Monitor the slaves (possibly taking them online and offline as required). 
- Recording and presenting the build results. 
- A Master instance of Jenkins can also execute build jobs directly. 

**Jenkins Agent(slave): -** 

An agent is typically a machine or container that connects to a Jenkins master and this agent that actually execute all the steps mentioned in a Job. When you create a Jenkins job, you have to assign an agent to it. Every agent has a label as a unique identifier. 

When you trigger a Jenkins job from the master, the actual execution happens on the agent node that is configured in the job. 

A single, monolithic Jenkins installation can work great for a small team with a relatively small number of projects. As your needs grow, however, it often becomes necessary to scale up. Jenkins provides a way to do this called “master to agent connection.” Instead of serving the Jenkins UI and running build jobs all on a single system, you can provide Jenkins with agents to handle the execution of jobs while the master serves the Jenkins UI and acts as a control node. 

Full Jenkins installation on a slave is not required. 

**Follow below steps to run a project using Jenkins Agent: -** 

1. before starting connecting Jenkins agent to Jenkins master, first create a new EC2 Instance, same .as you create master one. 

Note: - [ Make sure Your Jenkins master **SubnetID and Availability** one is same as Jenkins slave.]   

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.002.png)

This SubnetID and Availability zone ,you can find in networking TAB. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.003.jpeg)

2. After Creating an agent EC2 instance, you can make a connection between master and slave. 
1. Go to master command prompt and type  

**ssh-keygen** 

After that **.ssh** folder is created, this folder contains your public and private key 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.004.jpeg)

id\_rsa ----------------> private key id\_rsa.pub ----------> public key 

2. Copy this master public key and paste into agent authorized key. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.005.jpeg)

3. After that go to **Manage Jenkins** and click on **Manage nodes and clouds** 

Click on New Node and type mode name 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.006.jpeg)

Also add the Labels and inside Launch method select Launch agents via ssh.

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.007.jpeg)

Inside Launch Method, put Host Ip address and Jenkins master Private key Using** 

` `**SSH username and private key** 

It looks like below image. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.008.jpeg)

4. After that you install java on Jenkins Agent and the java version is same as Jenkins master java version.  

Also, for this project needs docker, so install docker and docker-compose on Jenkins  agent. 

Give the docker permission to current user. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.009.png)

5. check the Jenkins agent log, your agent is successfully connected to master or not?

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.010.jpeg)

3. After Agent connecting to Master, add the label to Declarative pipeline. 

This is the syntax to add label in Declarative pipeline. You can add label in Jenkinsfile. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.011.jpeg)

And do the commit. Using webhooks it’s automatically starting the build on Jenkins UI. 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.012.jpeg)

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.013.jpeg)

4. After Successfully Run the pipeline, check the logs and full view of pipeline 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.014.jpeg)

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.015.jpeg)

5. Add your Project Port no into your Jenkins agent security Group. Copy the public Ip address 

and put the port no. 

Your application is running 

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.016.jpeg)

![](Aspose.Words.e39b7f80-17d6-4665-9b63-ea43cfb04f24.017.jpeg)
