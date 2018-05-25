import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()


######## CHANGE THIS ##########
project_name = "UMSI106"
###############################

#master_url = 'http://127.0.0.1:8000'
master_url = 'https://106w18.learningpython.today'
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
            'login_required':'false',
            'appname':master_app,
            'loglevel':10,
            'course_url':master_url,
            'use_services': 'true',
            'python3': 'true',
            'basecourse':'pip2',
            # 'enable_chatcodes': 'true'
        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.
