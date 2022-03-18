import PySimpleGUI as sg

class InputLog:
    """入力ログ管理クラス"""
    window = None
    layout = None
    log_text = []
    def __init__(self):
        print("InputLogクラスの生成")

    def __del__(self):
        print("InputLogクラスの破棄")

    def open(self):
        print("window open")
        sg.theme('LightGrey4')
        window_name = "SubWindow"
        self.layout = [[sg.Text('RequestLog確認用ウィンドウです\n'
                                '※MainWindow の操作に戻る場合はSubWindowを閉じてください', size=(64, 5))],
                       [sg.Button('閉じる')],
                       [sg.Text('[ 履歴 ]')],
                       [[sg.Text(f"{log}")]for log in self.log_text]]

        self.window = sg.Window(window_name, self.layout,finalize=True)

        event, values = self.window.read()

        if event == sg.WIN_CLOSED or event == '閉じる':
            print("閉じるボタンが押されました")
            self.close()

    def close(self):
        if self.window == None:
            return
        self.window.close()

    def add_log(self, log):
        self.log_text.append(log)

