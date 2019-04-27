from fabric.api import local


def prepare_deployment(branch_name):
	''' Run tests and commit your changes, but only if your tests pass '''
    local('python manage.py test django_testing')
    local('git add -p && git commit') # or local('hg add && hg commit')