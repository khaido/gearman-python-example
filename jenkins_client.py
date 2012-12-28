'''
Created on Dec 7, 2012

@author: khaido
'''
from jenkinsapi.api import Jenkins


myj = Jenkins('http://localhost:8080')
jobs_str =  myj.get_jobs()
jobs_list = myj.get_jobs_list()
for job in jobs_list:
    # what labels are jobs associated with?
    print job 
    
node_dict = myj.get_node_dict()
for k, v in sorted(node_dict.items()):
    print k+'='+v

myn = myj.get_node('poppy')
node_data = myn.get_node_data()
node_bla = myn.get_data()
             

#job.invoke(securitytoken=token, block=block)
myjob = myj.get_job('pep')
myjob.invoke(invoke_pre_check_delay=0)


#print j.get_jobs()
#j.create_job('empty', jenkins.EMPTY_CONFIG_XML)
#j.disable_job('empty')
#j.copy_job('empty', 'empty_copy')
#j.enable_job('empty_copy')
#j.reconfig_job('empty_copy', jenkins.RECONFIG_XML)
#
#j.delete_job('empty')
#j.delete_job('empty_copy')

# build a parameterized job
#j.build_job('burnit', {'param1': 'test value 1', 'param2': 'test value 2'})
#j.build_job('burnit')
