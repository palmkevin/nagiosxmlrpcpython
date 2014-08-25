#!/usr/bin/python

# CAUTION: This script should be Python 2 and 3 compatible
import sys
<<<<<<< HEAD
import ssl
import socket

if sys.version_info >= (3, 0):
    # Python 3
    from xmlrpc.client import ServerProxy, Fault as xmlrpcFault
else:
    from xmlrpclib import ServerProxy, Fault as xmlrpcFault
=======
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6

NAGIOS_OK = 0
NAGIOS_WARN = 1
NAGIOS_CRIT = 2
NAGIOS_UNKNOWN = 3

<<<<<<< HEAD
def abort(msg):
    print(msg)
    exit(NAGIOS_UNKNOWN)

def main(argv):
    if len(argv) > 0 and argv[0] in ('--help', '-h'):
        abort("Usage: nagiosclient.py url_of_xmlrpc_server remote_method_to_be_called [arg1] [arg2] [arg3] [arg4]...")
    if len(argv) < 2:
        abort("Invalid arguments provided. Try `nagiosclient.py --help` for more information")
=======
if sys.version_info >= (3, 0):
    # Python 3
    from xmlrpc.client import ServerProxy, Fault as xmlrpcFault
else:
    from xmlrpclib import ServerProxy, Fault as xmlrpcFault

def main(argv):
    if len(argv) < 2:
        raise Exception('Wrong arguments provided: At least the URL of the xmlrpc-server and the method should be passed')
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6
    
    url = argv[0]
    methodName = argv[1]
    methodArgs = argv[2:]
<<<<<<< HEAD
        
    try:
        try:
            proxy = ServerProxy(url)
        except Exception as ex:
            abort("Invalid URL for XMLRPC-server passed: %s" % ex)
        
=======
    try:
        proxy = ServerProxy(url)
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6
        try:
            ret = getattr(proxy, methodName)(*methodArgs)
        except xmlrpcFault as xf:
            fctNotSupMsg = 'method "%s" is not supported' % methodName
            if fctNotSupMsg in str(xf):
<<<<<<< HEAD
                abort("The remote method '%s' is unknown" % methodName)
            abort(xf.faultString)
        except socket.error as sockerr:
            abort("Socket error (%s): %s" % (type(sockerr).__name__, sockerr.args[1]))
=======
                print("The remote method '%s' is unknown" % methodName)
                exit(NAGIOS_UNKNOWN)
            raise Exception(xf.faultString)
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6
        
        if not isinstance(ret, list):
            ret = [ret]

        if len(ret) > 2:
<<<<<<< HEAD
            abort("The remote method '%s' returned %s arguments. This is not supported (maximum 2 are allowed)" % (methodName, len(ret)))
=======
            raise Exception("The remote method '%s' returned %s arguments. This is not supported" % (methodName, len(ret)))
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6
        if len(ret) > 1:
            status, message = ret
        else:
            # one returned arg
            if isinstance(ret[0], int): # if numeric
                status = ret[0]
                message = '#NO INFO#'
            else:
                if not ret[0]:  # if empty
                    status = NAGIOS_UNKNOWN
                    message = "The remote method '%s' returned an empty answer" % methodName
                else:
<<<<<<< HEAD
                    status = NAGIOS_OK # if only a message is returned we suppose that everythis is ok
=======
                    status = NAGIOS_OK # We suppose that the client would raise an exception in all other cases
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6
                    message = ret[0]

        if status in (NAGIOS_OK, NAGIOS_WARN, NAGIOS_CRIT, NAGIOS_UNKNOWN):
            print(message)
            exit(status)
        else:
<<<<<<< HEAD
            abort("XMLRPC-server returned invalid status: %s" % status)
    except Exception as ex:
        abort(str(ex))

if __name__ == "__main__":
  main(sys.argv[1:])
=======
            print("XMLRPC-server returned invalid status: %s" % status)
            exit(NAGIOS_UNKNOWN)
    except Exception as ex:
        print(str(ex))
        exit(NAGIOS_UNKNOWN)


if __name__ == "__main__":
  main(sys.argv[1:])
>>>>>>> a0fd2e24bfc415a1f15f95ec6f496c0c3dfbbdb6
