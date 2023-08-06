from EEETools.Tools.GUIElements.connection_and_block_check import CheckConnectionWidget
from EEETools.Tools.modules_importer import import_excel_input
from tkinter import filedialog
import tkinter as tk
import unittest


class MyTestCase(unittest.TestCase):

    def test_block_connection(self):

        root = tk.Tk()
        root.withdraw()
        excel_path = filedialog.askopenfilename()

        array_handler = import_excel_input(excel_path)
        CheckConnectionWidget.launch(array_handler)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
