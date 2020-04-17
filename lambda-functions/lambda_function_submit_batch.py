#!/usr/bin/env python

import boto3
import os
import random 
import string

'''
This lambda handler submits a job to a AWS Batch queue.
JobQueue, and JobDefinition environment variables must be set. 
These environment variables are intended to be set to the Name, not the Arn. 
'''
def lambda_handler(event,context):
    # Grab data from environment
    jobqueue = os.environ['JOB_QUEUE']
    jobdef = os.environ['JOB_DEFINITION']
    job1Name = os.environ['JOB_NAME']
    print("jobqueue: {}, jobdef: {}, job1Name: {}".format(jobqueue,jobdef,job1Name))
    # Set up a batch client 
    session = boto3.session.Session()
    client = session.client('batch')

    # Submit the job
    job1 = client.submit_job(
        jobName=job1Name,
        jobQueue=jobqueue,
        jobDefinition=jobdef
    )
    print("Started Job: {}".format(job1['jobName']))
    
"""
JOB_DEFINITION  : arn:aws:batch:YOUR REGION:ACCOUNT ID:job-definition/1234 ...
JOB_NAME        : job name
JOB_QUEUE       : arn:aws:batch:YOUR REGION:ACCOUNT ID:job-queue/1234 ...
"""
