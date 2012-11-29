from gearman import GearmanWorker
from jenkinsapi.api import Jenkins
import simplejson

# The function that will do the work
def task_listener_echo(worker, job):
    return job.data

def task_listener_reverse(worker, job):
	rev = job.data[::-1]
	return rev

def task_listener_jenkins_invoke_job(worker, job):
    
    rev = "happy!!"
    
    jenkins_data = simplejson.loads(job.data)
    try:
        myj = Jenkins(jenkins_data['url'])
        job = myj.get_job(jenkins_data['job_id'])
        #job.invoke(securitytoken=token, block=block)
        job.invoke(invoke_pre_check_delay=0)
    except:
        rev="Not Happy!!!" 
    
    return rev

	
# Establish a connection with the job server on localhost--like the client,
# multiple job servers can be used.
worker = GearmanWorker(['127.0.0.1'])

# register_task will tell the job server that this worker handles the "echo"
# task
worker.set_client_id('your_worker_client_id_name')
worker.register_task('echo', task_listener_echo)
worker.register_task('reverse', task_listener_reverse)
worker.register_task('jenkins_invoke_job', task_listener_jenkins_invoke_job)

# Once setup is complete, begin working by consuming any tasks available
# from the job server
print 'working...'
worker.work()

# The worker will continue to run (waiting for new work) until exited by
# code or an external signal is caught