from Shared.Command.Command import Command
from Shared.Save.Classes.DataSaver import DataSaver


class SaveTxtCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: DataSaver, text_data: str):
        self.__executor = executor
        self.__text_data = text_data

    def execute(self) -> None:
        self.__executor.save_txt(self.__text_data)
