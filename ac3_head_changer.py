import sys
import os
import errno
from enum import Enum


class FileKind(Enum):
    diffuse = 'Diffuse'
    normal = 'Normal'
    mesh = 'Mesh'
    h_2050484285 = '2050484285'


class HexFile:
    kind: str
    hex_id: bytearray
    hex_content: bytearray
    file_path: str
    file_name: str


class Head:
    folder_path: str
    file_list: list

    diffuse: HexFile
    normal: HexFile

    mesh: HexFile

    h_2050484285: HexFile

    def __init__(self, folder):
        self.folder_path = folder
        self.file_list = next(os.walk(self.folder_path))[2]

        self.diffuse = HexFile()
        self.diffuse.kind = FileKind.diffuse.value

        self.normal = HexFile()
        self.normal.kind = FileKind.normal.value

        self.mesh = HexFile()
        self.mesh.kind = FileKind.mesh.value

        self.h_2050484285 = HexFile()
        self.h_2050484285.kind = FileKind.h_2050484285.value

        self.load_file_info(hex_file=self.diffuse)
        self.load_file_info(hex_file=self.normal)
        self.load_file_info(hex_file=self.mesh)
        self.load_file_info(hex_file=self.h_2050484285)

    def load_file_info(self, hex_file: HexFile) -> None:
        hex_file.hex_content, hex_file.file_path, hex_file.file_name = self.get_hex_content_and_paths(file_kind=hex_file.kind)
        hex_file.hex_id = self.get_hex_id(hex_content=hex_file.hex_content)

    @staticmethod
    def get_hex_id(hex_content: bytearray) -> bytearray:
        return hex_content[1:5]

    def get_hex_content_and_paths(self, file_kind: str) -> tuple:
        for file_name in self.file_list:
            if file_kind in file_name:
                file_path = f'{self.folder_path}\\{file_name}'
                return self.load_hex_content(file_path=file_path), file_path, file_name

    @staticmethod
    def load_hex_content(file_path) -> bytearray:
        with open(file_path, 'rb') as f:
            return bytearray(f.read())

    @staticmethod
    def print_file_info(hex_file: HexFile) -> None:
        print(f'Kind: {hex_file.kind}\n'
              f'ID: {("".join([hex(byte).replace("0x", "").upper() for byte in hex_file.hex_id]))}\n'
              f'FileName: {hex_file.file_name}\n')

    def print_diff_info(self):
        self.print_file_info(self.diffuse)


class HeadChanger:
    head1: Head
    head2: Head

    def __init__(self, args):
        self.head1 = Head(args[0])
        self.head2 = Head(args[1])

    def report_ids(self):
        self.report_id('1', self.head1)
        self.report_id('2', self.head2)

    @staticmethod
    def report_id(head_number: str, head_obj: Head):
        print('\n')
        print(f'Head {head_number}: \n')

        print(f'Diffuse: {head_obj.diffuse.hex_id}')
        print(f'Normal: {head_obj.normal.hex_id}')
        print(f'Mesh: {head_obj.mesh.hex_id}')
        print(f'2050484285: {head_obj.h_2050484285.hex_id}')

    def change_ids(self):
        self.change_id(original_hex_file=self.head2.diffuse, new_hex_file=self.head1.diffuse)
        self.change_id(original_hex_file=self.head2.normal, new_hex_file=self.head1.normal)
        self.change_id(original_hex_file=self.head2.mesh, new_hex_file=self.head1.mesh)

    def change_id(self, original_hex_file: HexFile, new_hex_file: HexFile):
        new_file_path = os.path.join(f'{str(self.head1.folder_path)}_NEW/', new_hex_file.file_name)
        if not os.path.exists(os.path.dirname(new_file_path)):
            try:
                os.makedirs(os.path.dirname(new_file_path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        edited_hex_content = self.get_original_hex_content_with_new_id(original_hex_file.hex_content, new_hex_file.hex_id)

        if original_hex_file.kind in FileKind.mesh.value:
            edited_hex_content = self.get_changed_references(original_hex_content=edited_hex_content)

        self.save_file(file_path=new_file_path, hex_content=edited_hex_content)

    @staticmethod
    def get_original_hex_content_with_new_id(original_hex_content: bytearray, new_id: bytearray) -> bytearray:
        return original_hex_content[:1] + new_id + original_hex_content[5:]

    def get_changed_references(self, original_hex_content: bytearray) -> bytearray:
        original_205_id = self.head2.h_2050484285.hex_id
        new_205_id = self.head1.h_2050484285.hex_id

        updated_hex_content = original_hex_content.replace(original_205_id, new_205_id)
        return updated_hex_content

    @staticmethod
    def save_file(file_path, hex_content: bytearray):
        with open(file_path, 'wb+') as f:
            f.write(hex_content)
            f.close()
            print(f'File created: {file_path}')


heads = HeadChanger(sys.argv[1:])
heads.change_ids()

# ezio = Head(sys.argv[1:][0])
# frederico = Head(sys.argv[1:][1])
# ezio.print_diff_info()
# frederico.print_diff_info()
