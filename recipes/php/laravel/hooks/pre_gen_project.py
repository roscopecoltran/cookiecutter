import cookiecutter
import mkdocs
import honcho

from subprocess import call

def install_laravel_installer():
    return call(["composer", "global", "require" "laravel/installer"])

def install_laravel_via_laravel_installer():
    return call(["laravel", "new", "--prefer-dist", "laravel/laravel"])

def install_laravel_via_composer():
    return call(["composer", "create-project", "--prefer-dist", "laravel/laravel", "."])



assert cookiecutter.__version__ > '1.3.0', 'Please upgrade your Cookiecutter installation'

assert mkdocs.__version__ > '0.10.0', 'Please upgrade your MkDocs installation'

assert honcho.__version__ > '0.6.0', 'Please upgrade your Honcho installation'

install_laravel_via_composer()
