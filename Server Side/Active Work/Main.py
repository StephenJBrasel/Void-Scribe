import threading
import queue
import time
import Terminal_Controller
import FireStore_Monitor
import Algorithm_Processor
import FireStore_Uploader


main_processings = queue.Queue()
shut_down_processes = queue.Queue()
master_thread_list = []


def SpinUpThread(target, name, daemon=False):
    thread = threading.Thread(target=target, name=name)
    thread.setDaemon(daemon)
    thread.start()
    master_thread_list.append(thread)

def AddShutDownProcess(procces):
    shut_down_processes.put(procces)
    

def MainEntryPoint():
    
    shut_down = False
    #Terminal Command Definitions
    #Exit Command
    def command_exit(arguments=None):
        nonlocal shut_down
        shut_down = True
    help_tip_exit = "Triggers the gracefull termination of the server."
    def post_report_exit():
        return None

    #Start-Up Procedure
    SpinUpThread(Terminal_Controller.InputEntryPoint, "Terminal Controller", True)
    SpinUpThread(Terminal_Controller.ExecutionerEntryPoint, "Terminal Exeutioner")
    SpinUpThread(FireStore_Monitor.FireStoreMonitorEntryPoint, "Firestore Monitor", True)
    SpinUpThread(FireStore_Uploader.FireStoreUploaderEntryPoint, "Firestore Uploader")
    SpinUpThread(Algorithm_Processor.AlgorithmProcessorEntryPoint, "Algorithm Processor")

    Terminal_Controller.AddTerminalCommand("exit", command_exit, help_tip_exit, post_report_exit)

    #Run-Time Procedure
    while True:
        if shut_down:
            break

        try:
            process = main_processings.get_nowait()
        except:
            time.sleep(1/10)
            continue

        process()
    
    #Exit Proceedure
    while True:
        try:
            exit_process = shut_down_processes.get_nowait()
        except:
            break
    
        exit_process()

    for thread in master_thread_list:
        if thread.is_alive() and not thread.isDaemon():
            thread.join()

    print("Gracefully Terminated")