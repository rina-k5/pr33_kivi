from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class SimpleAnimationApp(App):
    def build(self):
        # Лейаут, занимающий весь экран
        layout = FloatLayout(size_hint=(1, 1))

        # Кнопка, по нажатию на которую начнется анимация
        button = Button(text='Запустить анимацию', size_hint=(None, None), size=(500, 100), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        button.bind(on_press=self.start_animation)
        layout.add_widget(button)

        # Объект, который будет анимироваться (картинка)
        animated_image = Image(source='lambo.png', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(animated_image)

        self.animated_image = animated_image

        return layout

    def start_animation(self, instance):
        # Создаем анимацию для изменения позиции объекта в квадрате
        animation = Animation(pos_hint={'center_x': 0.7, 'center_y': 0.7}, duration=2)
        animation += Animation(pos_hint={'center_x': 0.7, 'center_y': 0.3}, duration=2)
        animation += Animation(pos_hint={'center_x': 0.3, 'center_y': 0.3}, duration=2)
        animation += Animation(pos_hint={'center_x': 0.3, 'center_y': 0.7}, duration=2)
        animation += Animation(pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=2)
        animation.repeat = True

        # Запускаем анимацию для объекта
        animation.start(self.animated_image)

if __name__ == '__main__':
    SimpleAnimationApp().run()
