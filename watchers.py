#!/Users/wooseongjin/.pyenv/shims/python
from optparse import OptionParser
import subprocess

# Alias of argrument
nginx = "/var/log/nginx/access.log"
tomcat = "/var/lib/tomcat/logs/catalina.out"

def main():
    usage = "usage: %prog -s arg1 -l arg2"
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option('-s', '--server', dest='servername', type='string', help='target server host')
    parser.add_option('-l', '--log', dest='logfile', type='string', help='logfile full path')
    parser.set_defaults(verbose=True)

    (options, args) = parser.parse_args()

    if options.servername and options.logfile and options.logfile in nginx and len(args) == 0:
        command = "ssh root@" + options.servername + " tail -f " + nginx
        # print(command)
        # print(len(args))
        subprocess.call(command, shell=True)
    elif options.servername and options.logfile and options.logfile in tomcat and len(args) == 0:
        command = "ssh root@" + options.servername + " tail -f " + tomcat
        # print(command)
        # print(len(args))
        subprocess.call(command, shell=True)      
    elif options.servername and options.logfile and len(args) != 0:
        parser.error("Too many arguments")
    else:
        parser.error("Wrong number of arguments")


if __name__ == "__main__":
    main()