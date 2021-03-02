import pymem
import pymem.process
import keyboard
import os
import time
 
dwEntityList = (0x4DA2F34)
dwGlowObjectManager = (0x52EB550)
m_iGlowIndex = (0xA438)
m_iTeamNum = (0xF4)
 
 
 
def Glow():
    isActive = False
    os.system("color 6")
    os.system("cls")
    print("...made by pero...")
    time.sleep(3)
    os.system("cls")
    
    os.system("color 4")
    os.system("cls")
    
    print("Glow Hack has launched.")
   
    print("\n\nHacks Is |Deactivated|")
 
    print("press N for Toggle ON\npress H for Toggle OFF.")
 
    pm = pymem.Pymem("csgo.exe") # Getting Procces by client name.
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll # Config. for  "client".
 
    while True:
        if keyboard.is_pressed("N") == True:
            isActive = True
            os.system("cls")
            os.system("color a")
            print("\n\nHacks Is |Activated|")
 
        if keyboard.is_pressed("H") == True:
            isActive = False
            os.system("cls")
            os.system("color 4")
            print("\n\nHacks Is |Deactive|")
 
        if isActive == True:
            glow_manager = pm.read_int(client + dwGlowObjectManager)
 
            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)
 
                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_glow = pm.read_int(entity + m_iGlowIndex)
 
                    if entity_team_id == 2:  # Terrorist
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))   
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)          
 
                    elif entity_team_id == 3:  # Counter-terrorist
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))   
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)          
 
def NoFlash():
    pass
 
if __name__ == '__main__':
    Glow()
