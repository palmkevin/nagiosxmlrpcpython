#!/usr/bin/python

# CAUTION: This script should be Python 2 and 3 compatible
import sys

NAGIOS_OK = 0
NAGIOS_WARN = 1
NAGIOS_CRIT = 2
NAGIOS_UNKNOWN = 3

if sys.version_info >= (3, 0):
    # Python 3
    from xmlrpc.client import ServerProxy, Fault as xmlrpcFault
else:
    from xmlrpclib import ServerProxy, Fault as xmlrpcFault

def main(argv):
    if len(argv) < 2:
        raise Exception('Wrong arguments provided: At least the URL of the xmlrpc-server and the method should be passed')
    
    url = argv[0]
    methodName = argv[1]
    methodArgs = argv[2:]
    try:
        proxy = ServerProxy(url)
        try:
            ret = getattr(proxy, methodName)(*methodArgs)
        except xmlrpcFault as xf:
            fctNotSupMsg = 'method "%s" is not supported' % methodName
            if fctNotSupMsg in str(xf):
                print("The remote method '%s' is unknown" % methodName)
                exit(NAGIOS_UNKNOWN)
            raise Exception(xf.faultString)
        
        if not isinstance(ret, list):
            ret = [ret]

        if len(ret) > 2:
            raise Exception("The remote method '%s' returned %s arguments. This is not supported" % (methodName, len(ret)))
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
                    status = NAGIOS_OK # We suppose that the client would raise an exception in all other cases
                    message = ret[0]

        if status in (NAGIOS_OK, NAGIOS_WARN, NAGIOS_CRIT, NAGIOS_UNKNOWN):
            print(message)
            exit(status)
        else:
            print("XMLRPC-server returned invalid status: %s" % status)
            exit(NAGIOS_UNKNOWN)
    except Exception as ex:
        print(str(ex))
        exit(NAGIOS_UNKNOWN)


if __name__ == "__main__":
  main(sys.argv[1:])
