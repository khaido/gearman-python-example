from gearman import GearmanClient
import simplejson

# create a client that will connect to the Gearman server running on
# localhost. The array allows you to specify a set of job servers.
client = GearmanClient(['127.0.0.1'])

# Submit a synchronous job request to the job server and store the
print 'Sending job...'
# This runs the "echo" job on the argument "foo"
#request = client.submit_job('reverse', 'hello')

jenkins_data = {'url':"http://localhost:8080",'jobId':'burnit'}
jenkins_burnit_status = {'url':"http://localhost:8080",'jobId':'burnit'}

#info_json = "{'url':'baba','job_id':'didi'}"
#request = client.submit_job('jenkins_invoke_job', simplejson.dumps(jenkins_data))
#request = client.submit_job('org.gearman.example.EchoFunction', "mama", poll_timeout=5)
#request = client.submit_job('org.gearman.example.JenkinsInvokeJob', "burnit", poll_timeout=5)
#request = client.submit_job('org.gearman.example.JenkinsJobStatus', "burnit", poll_timeout=5)
request = client.submit_job('org.gearman.example.JenkinsJobStatus', simplejson.dumps(jenkins_burnit_status), poll_timeout=5)
print request.result
print 'Work complete with state %s' % request.state
#request = client.submit_job('echo', 'foo')
#print request.result
#print 'Work complete with state %s' % request.state