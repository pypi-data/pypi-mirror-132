<br><br>

<img src='.media/logo.png' style='width:400px; float:left'>
<br>

# PYEMR : 
<br><br>

## Python EMR Toolkit

## install 

```
pip install pyemr
```

## init 

You can run 


Specify a target cluster and stage directory,
```
pyemr init \
--project_name=example \
--target_cluster="Cluster Name" \
--s3_stage_dir=s3://some/s3/directory \
--stage=dev \
--region=eu-west-1
```

```
poetry add catboost
```

```
pyemr test src/script.py
```

```
pyemr build
```

```
pyemr submit  src/script.py
```


## logs 

Download master and appllication, and creates a summary,
```
pyemr logs 
```

Specify a specific step
```
pyemr logs --step_id <step_id>
```

Print the last n lines of the last steps stderr,
```
pyemr stderr
```

Print the last n lines of the last steps stdout,
```
pyemr stdout 
```

Print the last n lines of specific step,
```
pyemr stdout --step_id <step_id>
```


## ssm

```
pyemr ssm 
```

```
pyemr ssm --cluster_name <cluster_name>
```

## local 

```
pyemr notebook 
```

```
pyemr python 
```

```
pyemr bash
```

## mock

Downloads the file to the s3 mock directory, 
```
pyemr mock s3://some/s3/path 
```

Downloads part of folder/table to the s3 mock,
```
pyemr mock_part s3://some/s3/path
```

## tools 

list clusters 
```
pyemr clusters
```

list steps ran by the project, 
```
pyemr steps
```

List all steps on a cluster,
```
pyemr steps --all
```

list steps on a specific cluster,
```
pyemr steps --cluster_name
```

Cancel the last step,
```
pyemr cancel 
```

Cancel a specific step, 
```
pyemr steps --step_id <step_id> 
```

Cancel a specific step on a specified cluster,
```
pyemr steps --step_id <step_id> --cluster_name <cluster_name>
```

## export 

Export as an airflow step, 
```
pyemr airflow src/script.py
```

## dev

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
