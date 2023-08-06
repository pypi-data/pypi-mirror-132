<br><br>


<img src='.media/logo.png' style='width:400px; float:left'>
<br>

# PYEMR : 
<br><br>

## Python EMR Toolkit

A command line tool for developing, testing and packaging pyspark applications on EMR.

<br> 

Install using
```pip install pyemr ```.

<p align="center">
<img src='.media/code.png' style='width:350px;'>
</p>

### Features: 

- Easily submit Spark scripts along with any dependencies via venv
- Shortcuts for viewing logs, ssm and canceling steps 
- Launch Amazon Linux notebooks/bash locally
- Export spark step as Airflow dag


<br>
<br>


# Quick Start

1. Init the project config [toml](https://python-poetry.org/).  
```
pyemr init 
```
Add python dependency,
```
poetry add <some_package_name>
```
2. Create a script and test it, 
```
pyemr test src/script.py
```
3.  Then build and push the package to s3, 
```
pyemr build 
```
(NOTE: The first time you run this its building the docker image from scratch. This might take > 5 min.)

4. Submit to the cluster, 
```
pyemr submit src/script.py --arg 1
```

5. Create airflow dag, 
```
pyemr airflow src/script.py --arg 1
```


<br>
<br>

# Usage

## 0. install 

Install docker [Docker](https://docs.docker.com/desktop/mac/install/). Install pyemr,

Install pyemr
```
pip install pyemr 
```

## 1. init
Init cretaes a 'pyproject.toml'. It can be run with arguments, 
```
pyemr init \
--project_name=example \
--target_cluster="Cluster Name" \
--s3_stage_dir=s3://some/s3/directory \
--stage=dev \
--region=eu-west-1
```

Or without arguments,
```
pyemr init 
```

## 2. dependencies
Install python dependency,
```
poetry add catboost
```

## 3. test
Test a pyspark script, 
```
pyemr test src/script.py
```
This will run the script locally. Paths on s3 will be downloaded and mocked.


## 4. debug

Download master and appllication, and creates a summary of errors,
```
pyemr logs 
```

Specify a specific step
```
pyemr logs <step_id>
```

Print the last n lines of the last steps stderr,
```
pyemr stderr
```

Print the last n lines of the last steps stdout,
```
pyemr stdout 
```

Alternatively you can specify the spark step id, 
```
pyemr stdout <step_id>
```


## 5. ssm

ssm starts a bash session inside the  cluster master node.  
```
pyemr ssm 
```

Or the master of another cluster, 
```
pyemr ssm <cluster_name>
```

NOTE: This requires your aws account to have the correct permissions. 

## 6. local 

Start a jupyter notebook inside a local aws linux container. This includes s3 mocking, 
```
pyemr notebook 
```

Start an interactive python session with s3 mocking, 
```
pyemr python 
```

Start a bash session inside aws linux container, 
```
pyemr bash
```

## 7. mock

Downloads part of an s3 folder/table into the mock directory,
```
pyemr mock s3://some/s3/path 
```

Downloads all of a folder/file into the mock diectory, 
```
pyemr mock s3://some/s3/path --all
```


## 8. tools 

List emr clusters,
```
pyemr clusters
```

List project steps on default cluster, 
```
pyemr steps
```

List all steps,
```
pyemr steps --all
```

List steps on a given cluster, 
```
pyemr steps <cluster_name>
```

Cancel the latest step, 
```
pyemr cancel 
```

Cancel a specified step, 
```
pyemr cancel --step_id <step_id> --cluster_name <cluster_name>
```

## 9. export 

Exports the spep as an airflow dag, 
```
pyemr airflow src/script.py --arg 1
```

## 10. dev
Format code and remove unused package, 
```
pyemr format 
```

Check for errors,
```
pyemr lint -E
```

Lint and check for style, errors and warnings, 
```
pyemr lint 
```


<br> 
<br> 
<br> 
<br> 

------------------------------------------------------

<br> 
<br> 
<br> 
<br> 
<br> 


## Appendix
<br>

### Dependencies
Requires docker.

### Development 

To reformat the code run 
```
pyemr format
```

Lint code,
```
pyemr lint
```

<br> 

### Troubleshoot

#### 1. 
```
[Errno 28] No space left on device
```

#### Solution: 

```
docker system prune
```

WARNING! This will remove:
- all stopped containers
- all networks not used by at least one container
- all dangling images
- all dangling build cache


<br><br>

####  2.

```
botocore.exceptions.ClientError: An error occurred (InvalidSignatureException) when calling the ListClusters operation: Signature expired: 20211210T145000Z is now earlier than 20211210T145057Z (20211210T145557Z - 5 min.)
```


#### Solution

https://stackoverflow.com/questions/61640295/aws-invalidsignatureexception-signature-expired-when-running-from-docker-contai


#### 3. 

```
Exception: Unable to find py4j, your SPARK_HOME may not be configured correctly
```

#### Solution

Set the SPARK_HOME, 

```
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.2.0/libexec
```


#### 4. 

```
An error occurred while calling o56.load.
: java.lang.reflect.InaccessibleObjectException: Unable to make field private transient java.lang.String java.net.URI.scheme accessible: module java.base does not "opens java.net" to unnamed module @40f9161a
```
#### Solution

switch global java version 
https://github.com/halcyon/asdf-java

```
brew install asdf
```

```
asdf plugin-add java https://github.com/halcyon/asdf-java.git
asdf install java adoptopenjdk-8.0.312+7
asdf global java adoptopenjdk-8.0.312+7
```

Set java home variables in bash/zsh, 
```
. ~/.asdf/plugins/java/set-java-home.bash
. ~/.asdf/plugins/java/set-java-home.zsh
```


## TODO:
- Add other spark versions 
- Support EMR docker 
- 
