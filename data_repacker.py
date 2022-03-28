import os


# TODO: add comments, optimise the code!

def bulk_export_data():
    data_tool = 'C:/Users/Manja/Downloads/Ubisoft_DATA_Tool_By_Delutto/Ubisoft_DATA_Tool.exe'
    data_folder = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC_ACR_Firenze/Giovanni"

    file_list = next(os.walk(data_folder))[2]

    for file in file_list:
        sub_folder = file.replace('.data', '')
        os.system(f'{data_tool} 3 -e "{os.path.join(data_folder, file)}" "{os.path.join(data_folder, sub_folder)}"')


def bulk_import_data():
    data_tool = 'C:/Users/Manja/Downloads/Ubisoft_DATA_Tool_By_Delutto/Ubisoft_DATA_Tool.exe'
    data_folder = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC/Packing"

    folder_list = next(os.walk(data_folder))[1]

    print(next(os.walk(data_folder)))

    for folder_name in folder_list:
        file_name = f'{folder_name}.data'
        # print(os.path.join(data_folder, file_name))
        os.system(f'{data_tool} 3 -i "{os.path.join(data_folder, file_name)}" "{os.path.join(data_folder, folder_name)}"')


def io_forge():
    forge_tool = 'C:/Users/Manja/Downloads/Ubisoft_DATA_Tool_By_Delutto/Ubisoft_Forge_Tool.exe'
    forge_file = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC/DataPC.forge"
    forge_folder = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC/Cook/2"

    os.system(f'{forge_tool} -i "{forge_file}" "{forge_folder}"')    # FORGE


# def io_forge():
#     forge_tool = 'C:/Users/Manja/Downloads/Ubisoft_DATA_Tool_By_Delutto/Ubisoft_Forge_Tool.exe'
#     forge_file = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC.forge"
#     forge_folder = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC_Test"
#
#     os.system(f'{forge_tool} -e "{forge_file}" "{forge_folder}"')    # FORGE
#

# def io_data():
#     data_tool = 'C:/Users/Manja/Downloads/Ubisoft_DATA_Tool_By_Delutto/Ubisoft_DATA_Tool.exe'
#     data_file = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC_ACR_Firenze.data"
#     data_folder = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC_ACR_Firenze"
#
#     os.system(f'{data_tool} 3 -e "{data_file}" "{data_folder}"')  # DATA


def io_data():
    data_tool = 'C:/Users/Manja/Downloads/Ubisoft_DATA_Tool_By_Delutto/Ubisoft_DATA_Tool.exe'
    data_file = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC/97-_Ezio_Florentin.data"
    data_folder = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/games/Assassin's Creed Brotherhood/DataPC/Packing/97-_Ezio_Florentin"

    os.system(f'{data_tool} 3 -i "{data_file}" "{data_folder}"')  # DATA

# io_forge()
# bulk_import_data()
# bulk_export_data()


io_forge()
