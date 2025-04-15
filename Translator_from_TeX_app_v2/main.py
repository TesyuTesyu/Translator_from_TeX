import TkEasyGUI as eg
import TeX_bug_fixer
import TeX_Encode
import TeX_Translation
import TeX_Decode
import TeX_replace
from pathlib import Path

#v1 : 2024/05/12 Nagata Ryouta
def main():
    # define layout
    layout = [[eg.Text("TeX Translator v2, 2024/06/02 Nagata Ryouta mf23a006@oecu.jp")],
            [eg.Button("select folder")],
            [eg.Text("", key='text1')],
            [eg.Text("Input file:          "),eg.InputText("English_origin.tex", key='text2')],
            [eg.Text("Output file:      "),eg.InputText("Japanese.tex", key='text3')],
            [eg.Text("DeepL API key: "),eg.InputText("", key='text4'),eg.Button("input", key='input')],
            [eg.Button("1st execute", key='ex11'),eg.Text("bug fix of TeX file"),eg.Button("help", key='ex12')],
            [eg.Button("2nd execute", key='ex21'),eg.Text("Separate equation and text (Eng) from TeX"),eg.Button("help", key='ex22'),eg.Checkbox("Translate footnotetext", key="footnotetextflag")],
            [eg.Button("3rd execute", key='ex31'),eg.Text("Translate to Japanese by DeepL"),eg.Button("help", key='ex32')],
            [eg.Button("4th execute", key='ex41'),eg.Text("Combining equation and text (JP)"),eg.Button("help", key='ex42')],
            [eg.Button("5th execute", key='ex51'),eg.Text("Fix TeX"),eg.Button("help", key='ex52')]
            ]
    window = eg.Window('TeX Transrator', layout, size=(500, 500) )
    API_key="a"
    # GUI表示実行
    while True:
        # ウィンドウ表示
        event, values = window.read( timeout=1000 )
        if event != "__TIMEOUT__" and event != "-TIMEOUT-":
            if event == eg.WIN_CLOSED:
                break
        if event in ["select folder", eg.WINDOW_CLOSED]:
            selected_dir = eg.popup_get_folder("select folder.")
            window['text1'].update(selected_dir)
        if event in ["input", eg.WINDOW_CLOSED]:
            API_key:str=window["text4"].get_text()
            window['text4'].update("done")
        if event in ["ex11", eg.WINDOW_CLOSED]:
            folder_pass=window["text1"].get_text()
            input_file=window["text2"].get_text()
            ans=TeX_bug_fixer.TeX_bug_fixer(folder_pass,input_file)
            if ans==-1:
                eg.popup(f"No such file.")
            else:
                eg.popup(f"Replaced has been done.")
        if event in ["ex21", eg.WINDOW_CLOSED]:
            folder_pass=window["text1"].get_text()
            ans=TeX_Encode.TeX_Encode(folder_pass,values["footnotetextflag"])
            if ans==-1:
                eg.popup(f"No such file.")
            else:
                eg.popup(f"Encoded has been done.")
        if event in ["ex31", eg.WINDOW_CLOSED]:
            folder_pass=window["text1"].get_text()
            path_eng_main = folder_pass+r'\English_main.log'
            path_eng_sentence = folder_pass+r'\English_sentence.log'
            file_path_obj = Path(path_eng_main)
            if not file_path_obj.exists():
                return -1
            file_path_obj = Path(path_eng_sentence)
            if not file_path_obj.exists():
                return -1
            with open(path_eng_main,'r',encoding="utf-8") as f:
                txt_main = f.read()
            with open(path_eng_main,'r',encoding="utf-8") as f:
                txt_sentence = f.read()
            Word_length=len(txt_main)+len(txt_sentence)
            Select_ans = eg.popup_buttons(
                "Do you really want to translate "+str(Word_length)+" words of text?",
                buttons=["Cancel", "continue"])
            if Select_ans=="continue":
                ans=TeX_Translation.TeX_Translation(folder_pass,API_key)
                if ans==200:
                    eg.popup(f"Translation has been done.")
                elif ans==-1:
                    eg.popup(f"No such file.")
                else:
                    eg.popup(f"ERROR from DeepL : "+str(ans))
            elif Select_ans=="Cancel":
                print("Cancel")
        if event in ["ex41", eg.WINDOW_CLOSED]:
            folder_pass=window["text1"].get_text()
            ans=TeX_Decode.TeX_Decode(folder_pass)
            if ans==-1:
                eg.popup(f"No such file.")
            else:
                eg.popup(f"Decoded has been done.")
        if event in ["ex51", eg.WINDOW_CLOSED]:
            folder_pass=window["text1"].get_text()
            ansfile=folder_pass+'\\'+window["text3"].get_text()
            ans=TeX_replace.TeX_replace(folder_pass,ansfile)
            if ans==-1:
                eg.popup(f"No such file.")
            else:
                eg.popup(f"Final processing. Replaced has been done.")
            
        if event in ["ex12", eg.WINDOW_CLOSED]:#help
            eg.popup(f"align 環境に\\tagがあって動かないので、分割してそれぞれの式として独立させる。\n必ず生成されたファイル(English_2.tex)がコンパイルできるかを確かめてから次に進む。(コンパイラはpdfLaTeX)")
        if event in ["ex22", eg.WINDOW_CLOSED]:#help
            eg.popup(f"式と文章を分離して、English_SWT.logとEnglish_main.logを生成する。\nさらにEnglish_SWT.logに残っている文章を抽出し、English_sentence.logを生成する。")
        if event in ["ex32", eg.WINDOW_CLOSED]:#help
            eg.popup(f"DeepLでEnglish_main.logとEnglish_sentence.logを翻訳し、Japanese_main.logとJapanese_sentence.logを生成する。\nDeepLの文字数制限に注意")
        if event in ["ex42", eg.WINDOW_CLOSED]:#help
            eg.popup(f"Japanese_main.logとJapanese_sentence.logとEnglish_SWT.logを合体してJapanese_first.texを生成する。\nこのままでは正常にコンパイルできないので次に進む。")
        if event in ["ex52", eg.WINDOW_CLOSED]:#help
            eg.popup(f"Japanese_first.texをコンパイルできるようにいくつかの置換を行い、指定されたファイル名で保存する。\n実際にコンパイルしてみて、エラーが出たら人力で修整する。(コンパイラはpLaTeX(ptex2pdf))")

if __name__ == '__main__':
    main()