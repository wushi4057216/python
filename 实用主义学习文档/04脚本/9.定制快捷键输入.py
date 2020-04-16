from pynput.keyboard import Listener
import time
import threading
import webbrowser

class ComboListener:

    def __init__(self):
        self.cur_keys = []
        # 修改keymap，快捷键组合对应的是URL
        self.keymap = {
            'gh': 'https://github.com/',
            'wk': 'https://www.wikipedia.org/'
        }
        self._run()

    def _on_press(self, key):
        try:
            self.cur_keys.append(key.char)

        except AttributeError:
            self.cur_keys.append(key.name)

    def _cleaner(self):
        while True:
            time.sleep(0.7)
            self.cur_keys.clear()

    def _run(self):
        l = Listener(on_press=self._on_press)
        l.daemon = True
        l.start()

        t = threading.Thread(target=self._cleaner)
        t.daemon = True
        t.start()

    def get_combo(self):
        if len(self.cur_keys) >= 2:
            combo = self.cur_keys[-2:]
            # [a,a,a,a]
            return combo

    # 修改解析快捷键的模块，当监测到特定快捷键组合，则利用webbrowser打开指定的URL
    def parsed_combo(self):
        combo = self.get_combo()
        if combo:
            key = ''.join(combo)
            if key in self.keymap.keys():
                # 使用上一课用到的webbrowser，打开一个URL
                webbrowser.open_new_tab(self.keymap[key])
                print("URL has been opened. {}".format(self.keymap[key]))
                # 当URL成功开启后，清空cur_keys，防止因程序运行过快而打开多个同样的页面
                self.cur_keys.clear()

if __name__ == "__main__":
    cl = ComboListener()
    while True:
        # 在while True循环中，只需要运行combo监测函数即可
        cl.parsed_combo()

