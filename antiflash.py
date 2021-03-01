#if you have problems read readme file with link to my discord server  
import pymem
import pymem.process
import time
#update offsets
dwLocalPlayer = (0xD8B2CC)
m_flFlashMaxAlpha = (0xA41C)


def main():
    print('made by pero')
    print(' anti flash has launched')
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(0))
        time.sleep(1)


if __name__ == '__main__':
    main()
