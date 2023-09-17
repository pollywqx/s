from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

from mamo_app import app

btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_Ok = QPushButton("Відповісти")
lb_Question = QLabel('')

RadioGrupBox = QGroupBox('Варіанти відповідей')
RadioGrup = QButtonGroup()

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGrup.addButton(rbtn_1)
RadioGrup.addButton(rbtn_2)
RadioGrup.addButton(rbtn_3)
RadioGrup.addButton(rbtn_4)

AnsGruopBox = QGroupBox('Результат тесту')
lb_Result = QLabel('')
lb_Correct - QLabel('')

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGrupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()

layout_res.addWidget(lb_Result, alignment=(Qt.Alignleft | Qt.AlignTop))
layout_res.addWidget(lb_Result, alignment=Qt.AlignHCenter, stretch = 2)
AnsGruopBox.setLayout(layout_res)
AnsGruopBox.hige()

layout_linel1 = QHBoxLayout()
layout_linel2 = QHBoxLayout()
layout_linel3 = QHBoxLayout()
layout_linel4 = QHBoxLayout()

layout_linel.addWinget(btn_Menu)
layout_linel.addWinget(1)
layout_linel.addWinget(btn_Sleep)
layout_linel.addWinget(box_Minutes)
layout_linel.addWinget(QLabel('хвилин'))

layout_linel2.addWinget(lb_Question, alignment =(QAlignHCenter | Qt.AlignVCenter))

layout_linel3.addWinget(RadioGrupBox)
layout_linel3.addWinget(AnsGruopBox)

layout_linel4.addStretch(1)
layout_linel4.addWinget(btn_Ok, stretch=2)
layout_linel4.addStretch(1)

layout_card.addLayout = QHBoxLayout()

layout_card.addLayout(layout_linel, stretch = 1)
layout_card.addLayout(layout_linel2, stretch = 2)
layout_card.addLayout(layout_line3l, stretch = 3)
layout_card.addLayout(1)
layout_card.addLayout(layout_linel4, stretch = 1)
layout_card.addLayout(1)

layout_card.setSpacing(S)


def show_result():
    RadioGrupBox.hige()
    AnsGruopBox.show()
    btn_Ok.setText('Наступне питання')

def show_question():
    RadioGrupBox.show()
    AnsGruopBox.hige()
    btn_Ok.setText('Відповісти')

    RadioGrup.setExclusive(False)
    rbtn_1.setCheckable(False)
    rbtn_2.setCheckable(False)
    rbtn_3.setCheckable(False)
    rbtn_4.setCheckable(False)
    RadioGrup.setExclusive(True)