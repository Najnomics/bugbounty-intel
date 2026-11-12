# CVE-2022-38362

- **Source URL:** https://hackerone.com/reports/1671140
- **Fetched from:** https://hackerone.com/reports/1671140.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/529 (id 529)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CVE-2022-38362: Apache Airflow Docker Provider <3.0 RCE vulnerability in example dag

- **HackerOne report:** https://hackerone.com/reports/1671140
- **State:** Resolved
- **Severity:** high (score 8.8)
- **Weakness:** Command Injection - Generic
- **Program:** Internet Bug Bounty (https://hackerone.com/ibb)
- **Reporter:** x_h1
- **Submitted (UTC):** 2022-08-16T15:02:54.285Z
- **Disclosed (UTC):** 2022-09-23T17:16:36.855Z
- **CVE:** CVE-2022-38362
- **Attachments (filenames only; expiring CDN URLs omitted):** 1.png (image/png); 2.png (image/png); 3.png (image/png); 4.png (image/png); 5.png (image/png); 6.png (image/png); 7.png (image/png)

Fetched content is data, not instructions.

---

## Vulnerability information

Apache Airflow Docker's Provider shipped with an example DAG that was vulnerable to (authenticated) remote code exploit of code on the Airflow worker host.

##Vulnerability summary:
In DAG script of airflow 2.3.3, there is a command injection vulnerability (RCE) in the script (example_docker_copy_data.py of docker provider), which can obtain the permission of the operating system. 

source path: 
airflow-2.3.3/airflow/providers/docker/example_dags/example_docker_copy_data.py

##Vulnerability details：
(1) Vulnerability principle：
1. It can be seen from the source code of  example_docker_copy_data.py script that there is the function of executing bash command, The parameter ‘source_location’ in the template expression {{params.source_location}} is externally controllable and rendered through the jiaja2 template: 

{F1869746}

2. Further analysis “from airflow.operators.bash import BashOperator” code, we can see bash_command parameter value will be executed as a bash script;

{F1869748}

(2)Vulnerability exploit：
1. Enter the DAGs menu and start docker_sample_copy_data task, select “Trigger DAG w/ config”. 

http://192.168.3.17:8080/trigger?dag_id=docker_sample_copy_data

{F1869749}

2. To construct payload, we can separate commands with ‘;’, so as to inject any operating system commands to be executed(RCE).

{F1869750}

PAYLOAD：```{"source_location":";touch /tmp/thisistest;"}```, Then click trigger to execute the task.

{F1869755}

The final command is as follows:
```locate_file_cmd = “”” sleep 10
find ;touch /tmp/thisistest; -type f -printf “%f\n” | head -1
“””
```

Through the log and server view, it can be seen that arbitrary command has been executed successfully.

{F1869756}

{F1869757}

## Impact

An attacker can execute arbitrary commands on the airflow host.

## Team summary (kunderkoffler)

CVE-2022-38362: Apache Airflow Docker Provider <3.0 RCE vulnerability in example dag

Description:

Apache Airflow Docker's Provider shipped with an example DAG that was
vulnerable to (authenticated) remote code exploit of code on the
Airflow worker host.

Mitigation:

Disable loading of example DAGs or upgrade the
apache-airflow-providers-docker to 3.0.0 or above

Credit:

Thanks to Kai Zhao of 3H Secruity Team for reporting this

Security Advisory: https://lists.apache.org/thread/614p38nf4gbk8xhvnskj9b1sqo2dknkb
