from identificator import User_pers
import utils.Base_monitor as base_script
import threads.Cpu_monitor as cpu_script
import threads.Ram_monitor as ram_script
import threads.Disk_monitor as disk_script
import threads.Network_monitor as net_script
import threads.Process as proc_script



def main():

    """Method Main, entry to start program"""

    user = User_pers.User(r'User.txt').get_uid()
    print(user)
    pc = insert_base_data(user)

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



def insert_base_data(user):
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
    main()
else:
    print('no me llames desde fuera')
    exit(0)
