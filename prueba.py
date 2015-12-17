import jenkins

def main():
    # parse command line options
	#server = jenkins.Jenkins('http://localhost:8080', username='myuser', password='mypassword')
	#version = server.get_version()
	#print(version)

	server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
	jobs = server.get_jobs()
	print(jobs)
	server.build_job('empty')
	server.disable_job('empty')
	server.copy_job('empty', 'empty_copy')
	server.enable_job('empty_copy')
	server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

	server.delete_job('empty')
	server.delete_job('empty_copy')

	# build a parameterized job
	# requires creating and configuring the api-test job to accept 'param1' & 'param2'
	server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
	last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
	build_info = server.get_job_info('api-test', last_build_number)
	print(build_info)

if __name__ == "__main__":
    main()







