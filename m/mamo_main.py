from PyQt5.QWidgets import QApplication

app = QApplication([])


from memo_app import app
from memo_data import Form, FormView

from memo_main_layout import layout_main, btn_card, btn_form, wdgt_edit, wdgt_card
from memo_card_layout import (
    # app, layout_card, - это больше не нужно!
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result)

from memo_edit_layout import (txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)
main_width, main_height = 800, 450 # начальные размеры главного окна

text_wrong = '''<font color="red">Неверно</font>'''
text_correct = '''<font color="green">Верно</font>'''

# пока еще работаем с одним вопросом, а не списком вопросов. Создаем:
frm = Form('Кому на Руси жить хорошо?', 'Программистам', 'Дворянам', 'Крестьянам', 'Соединившимся пролетариям')

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)  # перемешиваем варианты ответа
# связываем эту информацию с формой ответа на вопрос:
frm_card = FormView(frm, lb_Question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])

# связываем эту информацию с формой редактирования вопроса:
frm_edit = FormView(frm, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)

def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    # по-хорошему имеет смысл сделать наследника FormModel c этой функцией, потому что тут есть завязки и на интерфейс, и на данные...
    correct = frm_card.answer.isChecked() # в этом радиобаттоне лежит наш ответик!

if correct:
        # ответ верный, запишем
        lb_Result.setText(text_correct) # надпись "верно" или "неверно"
        lb_Correct.setText(frm_card.answer.text()) # это приходится делать вручную
        show_result()

else:
        incorrect = frm_card.wrong_answer1.isChecked() or frm_card.wrong_answer2.isChecked() or frm_card.wrong_answer3.isChecked()
        if incorrect:
            # ответ неверный, запишем и отразим в статистике
            lb_Result.setText(text_wrong) # надпись "верно" или "неверно"
            lb_Correct.setText(frm_card.answer.text()) # это приходится делать вручную
            show_result()

def click_OK(self):
    # пока что проверяем вопрос, если мы в режиме вопроса, иначе ничего
    if btn_OK.text() != 'Следующий':
        check_result()

def show_card():
    # показать вопросы
    wdgt_edit.hide()
    wdgt_card.show()

def show_form():
    # редактировать вопросы
    wdgt_card.hide()
    wdgt_edit.show()

btn_card.clicked.connect(show_card)
btn_form.clicked.connect(show_form)
btn_OK.clicked.connect(click_OK)

win_card = QWidget()
win_card.resize(main_width, main_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_main)
# show_data() вместо этого используем методы объектов, связывающих формы с данными:
frm_card.show()
frm_edit.show()
show_question()
show_card()

win_card.show()
app.exec_()