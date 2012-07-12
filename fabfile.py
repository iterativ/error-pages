import os
from fabric.api import *
from fabric.contrib.project import *

def _local_path(*args):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *args)

# environments
env.user = 'root'
env.rsync_exclude = ['.settings/',
                     '.project',
                     '.pydevproject',
                     '.git/',
                     '*.py',
                     '*.pyc',
                     '.keep']
env.remote_app = '/srv/www/error-pages'
env.local_app = _local_path() + '/'

def deploy():

    run('mkdir -p %(remote_app)s' % env) 
    
    # sources & templates
    rsync_project(
        remote_dir = env.remote_app,
        local_dir = env.local_app,
        exclude = env.rsync_exclude,
    )    
    
    run('/etc/init.d/nginx restart')
    

