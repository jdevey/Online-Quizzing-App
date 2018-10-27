# bob-ross-fan-club


INSTALL

Install Python 3.6.3

Verify pip3 was installed with python

a. run cmd: pip3 --version

b. expected output: pip version 10.0.1

Install virtualenv

a. cmd: python3 -m venv virtenv

b. sudo pip install vitualenv

Clone Project

cd to project root directory

Instruct Virtualenv which version of python to use with the following command

a. cmd: venv -p python3 virtenv

b. cmd: source bin/activate

From the project directory run the following command

a. cmd: pip install -Ur local.txt
      
      1.If running for testing or production run the corresponding .txt file

b. Expected output dependencies will be installed.

VIRTUAL ENVIORNMENT To disable the virtual environement

  a. cmd: deactivate
To renable virtual enviornemnt

  a. cmd: source bin/activate
