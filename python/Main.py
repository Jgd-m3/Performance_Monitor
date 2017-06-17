from identificator import User_pers
import utils.Base_monitor as base_script
import threads.Cpu_monitor as cpu_script
import threads.Ram_monitor as ram_script
import threads.Disk_monitor as disk_script
import threads.Network_monitor as net_script
import threads.Process_monitor as proc_script
import os

class Main:
    """
    Class Main to start the program
    """
    def __init__(self):
        """
        constructor of Main's class, that runs the _main() method
        """
        self._main()

    def _main(self):

        """
        Method _main to start the program
        :return: 
        """
        user = None
        looper_corrupt = 0
        while user is None or user < 0:
            user = User_pers.User(r'User.m3').get_uid()
            looper_corrupt += 1
            if looper_corrupt > 10 and (user is None or user < 0):
                os.remove(r'User.m3')
        print(user)

        pc = self._insert_base_data(user)

        hiloCpu = cpu_script.Cpu(args=(pc), name='cpu_monitor', daemon= True)
        hiloRam = ram_script.Ram(args=(pc), name='ram_monitor', daemon= True)
        hiloDisk = disk_script.Disk(args=(pc), name='disk_monitor', daemon=True)
        hiloNet = net_script.Net(args=(pc), name='net_monitor', daemon= True)
        hiloProc = proc_script.Process(args=(pc), name='proc_monitor', daemon= True)

        hiloCpu.start()
        hiloRam.start()
        hiloDisk.start()
        hiloNet.start()
        hiloProc.start()

        hiloCpu.join()
        hiloRam.join()
        hiloDisk.join()
        hiloNet.join()
        hiloProc.join()

        print('han terminao los daemons')


    def _insert_base_data(self, user):
        """
        Method to insert the fixed data of the pc
        :param user: id from the User 
        :return: 
        """
        bs = base_script.Base(user)
        id_pc = bs.get_data_id()

        if id_pc is not None:
            bs.update_pc(id_pc)
        else:
           id_pc = bs.register_pc()

        print('terminó shuprimo')
        return id_pc


if __name__ == '__main__':
    Main()
else:
    print('no me llames desde fuera')
    exit(0)
