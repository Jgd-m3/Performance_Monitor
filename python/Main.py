from identificator import User_pers
import utils.Base_monitor as base_script

import threads.Cpu_monitor as cpu_script
import threads.Ram_monitor as ram_script
import threads.Disk_monitor as disc_script
import threads.Network_monitor as net_script



def main():


    user = User_pers.User(r'User.txt').give_me_uid()
    print(user)
    pc = insert_base_data(user)
    
    hiloCpu = cpu_script.Cpu(args=(pc), daemon= True)
    hiloRam = ram_script.Ram(args=(pc), daemon= True)
    hiloDisk = disc_script.Disk(args=(pc), daemon=True)
    hiloNet = net_script.Net(args=(pc), daemon= True)

    hiloCpu.start()
    hiloRam.start()
    hiloDisk.start()
    hiloNet.start()

    hiloCpu.join()
    hiloRam.join()
    hiloDisk.join()
    hiloNet.join()
    
    print('han terminao los daemons')



def insert_base_data(user):
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
