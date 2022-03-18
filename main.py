import PySimpleGUI as sg
import requests

from input_log_window import InputLog

sg.theme('LightGrey4')
layout = [[sg.Text('アプリケーション説明')],
                       [sg.Text('WebApi を投げてどのようなレスポンスデータが表示されるか確認する為のツール')],
                       [sg.Text('実行回数:0', key="play_count")],
                       [sg.Text('WebApi URL https://', key="key_https"), sg.InputText()],
                       [sg.Text('リクエストデータ:', key="key_request")],
                       [sg.Button('送信'), sg.Button('閉じる'), sg.Button('ログ確認')],
                       [sg.Text('レスポンスデータ:', key="key_response")]]

window_name = "TestWebAPIPyResponseViewer -MainWindow"
window = sg.Window(window_name, layout)

is_loop = True
play_count = 0
inputLogWindow = InputLog()

while is_loop:
    event, values = window.read()
    inputLogWindow.close()

    print(event)

    if event == sg.WIN_CLOSED or event == '閉じる':
        is_loop = False
        print("閉じるボタンが押されました")

    elif event == '送信':
        play_count += 1
        update_text = "実行回数:" + str(play_count)
        window['play_count'].update(update_text)

        # リクエストデータの表示内容を更新
        window['key_request'].update("リクエストデータ:" + str(values[0]))

        # リクエスト処理
        requestData = 'https://' + str(values[0])
        inputLogWindow.add_log(requestData)
        try:
            response = requests.get(requestData)
            update_response_text = "リクエストに成功しました \n レスポンスデータ:" + response.text
        except:
            update_response_text = "レスポンスデータ:" + "失敗"

        # レスポンスデータの更新
        window['key_response'].update(update_response_text)
    elif event == "ログ確認":
        inputLogWindow.open()
        print("ログ確認ウィンドウの表示")

window.close()