def slot_btn_chooseMutiFile(self):
    files, filetype = QFileDialog.getOpenFileNames(self,
                                                   "多文件选择",
                                                   self.cwd,  # 起始路径
                                                   "All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")

    if len(files) == 0:
        print("\n取消选择")
        return

    print("\n你选择的文件为:")
    for file in files:
        print(file)
    print("文件筛选器类型: ", filetype)
