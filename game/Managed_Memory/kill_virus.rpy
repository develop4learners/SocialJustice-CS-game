label kill_virus: #kill_virus is now the code that actually contains the bad code, but you have to delete root_virus1 to terminate its while loop I guess

    python:
        renpy.scene()
        renpy.show("desk_standing_behind")

        renpy.show("clara phone",at_list=["lowered_left"])

        import shutil
        from time import sleep
        import glob
        import os

        counter = 0
        while counter != 3: #should eventually be while True
            try: #try to create a clone
                virus_name = "clone_virus" + str(counter) +".txt"
                virus_path = "Users/princesssteffykins/Downloads/RENPY PROJECTS/SocialJustice-CS-game/game/Managed_Memory/" + virus_name
                shutil.copy2("Users/princesssteffykins/Downloads/RENPY PROJECTS/SocialJustice-CS-game/game/Managed_Memory/root_virus1.py", virus_path)
                counter += 1
                sleep(1)
            except: #suddenly root_virus1.py no longer exists
                break
                print("We got into the exception")
