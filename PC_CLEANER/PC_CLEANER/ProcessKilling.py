from ctypes import *
import subprocess
 
#PSAPI.DLL
psapi = windll.psapi
#Kernel32.DLL
kernel = windll.kernel32
 
def EnumProcesses():
    arr = c_ulong * 256
    lpidProcess= arr()
    cb = sizeof(lpidProcess)
    cbNeeded = c_ulong()
    hModule = c_ulong()
    count = c_ulong()
    modname = c_buffer(30)
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_READ = 0x0010
 
    #Call Enumprocesses to get hold of process id's
    psapi.EnumProcesses(byref(lpidProcess),
                        cb,
                        byref(cbNeeded))
 
    #Number of processes returned
    nReturned = cbNeeded.value/sizeof(c_ulong())
 
    pidProcess = [i for i in lpidProcess][:nReturned]
 
    for pid in pidProcess:
 
        #Get handle to the process based on PID
        hProcess = kernel.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,
                                      False, pid)
        if hProcess:
            psapi.EnumProcessModules(hProcess, byref(hModule), sizeof(hModule), byref(count))
            psapi.GetModuleBaseNameA(hProcess, hModule.value, modname, sizeof(modname))
            print "".join([ i for i in modname if i != '\x00'])
 
            #-- Clean up
            for i in range(modname._length_):
                modname[i]='\x00'
 
            kernel.CloseHandle(hProcess)
 
if __name__ == '__main__':
    EnumProcesses()
    "notepad.exe"
    
    # windows
    import ctypes
    PROCESS_TERMINATE = 1
    handle = ctypes.windll.kernel32.OpenProcess("notepad.exe", False, 11316)
    ctypes.windll.kernel32.TerminateProcess(handle, -1)
    ctypes.windll.kernel32.CloseHandle(handle)

