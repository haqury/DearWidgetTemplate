import SpeachToTextWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class Widget(QWidget):
    def __init__(self, widget_id):
        super().__init__()
        self.setStyleSheet("""QWidget {background-color: rgba(0, 0, 0,    4);}""")
        self.widget_id = widget_id
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel(f"Widget {self.widget_id}")
        layout.addWidget(self.label)
        self.setLayout(layout)

class WidgetManager:
    def __init__(self):
        self.widgets = {}

    def add_widget(self, widget_id, widget):
        self.widgets[widget_id] = widget

    def get_widget(self, widget_id):
        return self.widgets.get(widget_id)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_manager = WidgetManager()

        # Создание и добавление виджетов в менеджер
        widget1 = Widget(1)
        widget2 = Widget(2)
        speach = SpeachToTextWidget.SpeachToTextWidget()
        self.widget_manager.add_widget(1, widget1)
        self.widget_manager.add_widget(2, widget2)
        self.widget_manager.add_widget(3, speach)

        speach.resize(500, 150)
        speach.show()
        speach.move(500, 400)

        # Прячем виджеты на разных экранах (можно использовать методы move для позиционирования на разных экранах)
        widget1.move(-1000, -1000)
        widget2.move(1920, -1000)  # Примерный сдвиг для второго экрана

    def show_widget(self, widget_id):
        widget = self.widget_manager.get_widget(widget_id)
        if widget:
            # Показываем виджет по запросу
            #widget.move(100, 100)  # Примерное положение на основном экране
            widget.show()
        else:
            print(f"Виджет с ID {widget_id} не найден.")
