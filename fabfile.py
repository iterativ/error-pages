import os
from fabric.api import *
from fabric.contrib.project import *


def _local_path(*args):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *args)


# environments
env.use_ssh_config = True
# Warning:
# env.hosts = ['cloudsigma.iterativ.ch'] don't specify hard code hosts
# use fab deploy -Hcloudsigma.iterativ.ch
env.rsync_exclude = ['.settings/',
                     '.project',
                     '.pydevproject',
                     '.git/',
                     '.idea/',
                     '*.py',
                     '*.pyc',
                     '.keep']
env.remote_app = '/srv/www/error-pages'
env.local_app = _local_path() + '/'


def deploy():
    sudo('mkdir -p %(remote_app)s' % env)
    # sources & templates
    rsync_project(
        remote_dir = env.remote_app,
        local_dir = env.local_app,
        exclude = env.rsync_exclude,
        extra_opts='--rsync-path="sudo rsync"',
    )    

    # don't restart on error pages update
    #run('/etc/init.d/nginx restart')
