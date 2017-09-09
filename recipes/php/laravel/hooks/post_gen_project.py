from __future__ import print_function
import cookiecutter
from subprocess import call
import os
import random
import shutil

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_mkdocs(project_directory):
    """Removes the mkdocs files and directory"""

    mkdocs_config_location = os.path.join(
        PROJECT_DIRECTORY,
        'mkdocs.yml'
    )
    shutil.rmtree(mkdocs_config_location)

    mkdocs_docs_location = os.path.join(
        PROJECT_DIRECTORY,
        '{{ cookiecutter.repo_name }}/docs'
    )
    shutil.rmtree(mkdocs_docs_location)




if '{{ cookiecutter.use_mkdocs }}'.lower() == 'n':
    remove_mkdocs(PROJECT_DIRECTORY)
