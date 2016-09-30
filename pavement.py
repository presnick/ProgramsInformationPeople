import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()


######## CHANGE THIS ##########
project_name = "pip2"
###############################

master_url = 'http://127.0.0.1:8000'
master_url = 'https://www.programsinformationpeople.org'
master_app = 'runestone'
serving_dir = "./build/" + project_name
dest = "../../static"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/"+project_name,
        sourcedir="./_sources/",
        outdir="./build/"+project_name,
        confdir=".",
        project_name = project_name,
        template_args = {
            'course_id':project_name,
            'login_required':'true',
            'appname':master_app,
            'loglevel':10,
            'course_url':master_url,
            'use_services': 'true',
            'python3': 'false',
            'basecourse':'pip2'
        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.