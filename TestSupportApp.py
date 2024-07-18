import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import datetime
import json

class TestSupportApp:
    def __init__(self, root):
        self.entries = self.load_entries()  # 保存されたエントリーを読み込む

        self.root = root
        self.root.title("Test Support App")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10, padx=10)

        self.add_button = tk.Button(self.frame, text="新しい用語/問題を追加する", command=self.add_entry)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.check_button = tk.Button(self.frame, text="理解した用語/問題にチェックをつける", command=self.mark_as_checked)
        self.check_button.grid(row=0, column=1, padx=5, pady=5)

        self.view_button = tk.Button(self.frame, text="未理解の用語/問題を表示する", command=self.view_unchecked_entries)
        self.view_button.grid(row=0, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="用語/問題を削除する", command=self.delete_entry)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

        self.quit_button = tk.Button(self.frame, text="終了する", command=self.save_and_quit)  # 終了時に保存する
        self.quit_button.grid(row=0, column=4, padx=5, pady=5)

        self.text_area = scrolledtext.ScrolledText(self.frame, width=80, height=20)
        self.text_area.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        # 初期データの表示
        self.view_unchecked_entries()

    def add_entry(self):
        term = simpledialog.askstring("用語/問題追加", "用語または問題の名前を入力してください:")
        if term:
            description = simpledialog.askstring("用語/問題追加", "詳細な説明を入力してください:")
            if description:
                entry = {
                    'term': term,
                    'description': description,
                    'added_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'checked': False
                }
                self.entries.append(entry)
                self.save_entries_to_file()  # エントリーを保存
                messagebox.showinfo("成功", "エントリーが追加されました。")
                self.view_unchecked_entries()  # 表示を更新

    def mark_as_checked(self):
        if not self.entries:
            messagebox.showinfo("情報", "追加されたエントリーがありません。")
            return

        entries_list = "\n".join([f"{i+1}. {entry['term']} - {entry['description']} - 追加日時: {entry['added_at']} - 理解済み: {entry['checked']}"
                                  for i, entry in enumerate(self.entries)])
        index = simpledialog.askinteger("チェックをつける", f"理解した用語/問題の番号を入力してください:\n\n{entries_list}")
        if index and 1 <= index <= len(self.entries):
            self.entries[index-1]['checked'] = True
            self.save_entries_to_file()  # エントリーを保存
            messagebox.showinfo("成功", "チェックがつけられました。")
            self.view_unchecked_entries()  # 表示を更新

    def view_unchecked_entries(self):
        unchecked_entries = [entry for entry in self.entries if not entry['checked']]
        if not unchecked_entries:
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, "未理解の用語/問題はありません。")
        else:
            unchecked_list = "\n".join([f"{i+1}. {entry['term']} - {entry['description']} - 追加日時: {entry['added_at']} - 理解済み: {entry['checked']}"
                                        for i, entry in enumerate(unchecked_entries)])
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, f"未理解の用語/問題の一覧:\n\n{unchecked_list}")

    def delete_entry(self):
        if not self.entries:
            messagebox.showinfo("情報", "削除するエントリーがありません。")
            return

        entries_list = "\n".join([f"{i+1}. {entry['term']} - {entry['description']} - 追加日時: {entry['added_at']} - 理解済み: {entry['checked']}"
                                  for i, entry in enumerate(self.entries)])
        index = simpledialog.askinteger("削除する", f"削除したいエントリーの番号を入力してください:\n\n{entries_list}")
        if index and 1 <= index <= len(self.entries):
            del self.entries[index-1]
            self.save_entries_to_file()  # エントリーを保存
            messagebox.showinfo("成功", "エントリーが削除されました。")
            self.view_unchecked_entries()  # 表示を更新

    def save_and_quit(self):
        self.save_entries_to_file()  # 終了時にエントリーを保存
        self.root.quit()

    def save_entries_to_file(self):
        with open('entries.json', 'w') as f:
            json.dump(self.entries, f, indent=4)

    def load_entries(self):
        try:
            with open('entries.json', 'r') as f:
                entries = json.load(f)
        except FileNotFoundError:
            entries = []
        return entries

if __name__ == "__main__":
    root = tk.Tk()
    app = TestSupportApp(root)
    root.mainloop()
