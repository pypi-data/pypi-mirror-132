# pyshell
A Linux subprocess module, An easier way to interact with the Linux shell

# Installation

You can install using the Volian repo

    echo "deb http://deb.volian.org/volian/ scar main" | sudo tee /etc/apt/sources.list.d/volian-archive-scar-unstable.list
    wget -qO - https://deb.volian.org/volian/scar.key | sudo tee /etc/apt/trusted.gpg.d/volian-archive-scar-unstable.gpg > /dev/null
    sudo apt update && sudo apt install python3-pyshell

You can also install using pip

`pip install pyshell`

# Usage

    from pyshell import pyshell
    shell = pyshell()
    shell.echo('Hello', "GitLab!")
    
# Docs

Check out the Official [Documentation](https://volitank.com/pyshell/index.html) for help with syntax and different arguments

# TODO
- Update docs to include new expect and popen functionality.
- Update docs with new basic `import shell`
- Update docs with `DEFAULT, DEVNULL, PIPE, STDOUT` moving to `shell.`