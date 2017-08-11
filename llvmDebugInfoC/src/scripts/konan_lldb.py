#!/usr/bin/python

#
# (lldb) command script import llvmDebugInfoC/src/scripts/konan_lldb.py
# (lldb) show_variable
#

import lldb
import commands
import optparse
import shlex

def show_variable(debugger, command, result, internal_dict):
    v = lldb.frame.FindVariable(command)
    if not v.IsValid():
        print "Unknown variable %s" % command
    else:
        debugger.GetCommandInterpreter().HandleCommand('expr -- Konan_DebugPrint(%s)' % v.GetName(), result)
    return result

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f konan_lldb.show_variable show_variable')

