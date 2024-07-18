# TestSupportApp.py
import datetime

class TestSupportApp:
    def __init__(self):
        self.entries = []

    def add_entry(self, term, description):
        entry = {
            'term': term,
            'description': description,
            'added_at': datetime.datetime.now(),
            'checked': False
        }
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

    def mark_as_checked(self, index):
        if 0 <= index < len(self.entries):
            self.entries[index]['checked'] = True

    def get_unchecked_entries(self):
        return [entry for entry in self.entries if not entry['checked']]

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]

def main():
    app = TestSupportApp()

    while True:
        print("1. 新しい用語/問題を追加する")
        print("2. 理解した用語/問題にチェックをつける")
        print("3. 未理解の用語/問題を表示する")
        print("4. 用語/問題を削除する")
        print("5. 終了する")
        choice = input("選択肢を入力してください: ")

        if choice == '1':
            term = input("用語または問題の名前を入力してください: ")
            description = input("詳細な説明を入力してください: ")
            app.add_entry(term, description)
            print("エントリーが追加されました。")

        elif choice == '2':
            entries = app.get_entries()
            if not entries:
                print("追加されたエントリーがありません。")
            else:
                print("理解した用語/問題の一覧:")
                for i, entry in enumerate(entries):
                    print(f"{i+1}. {entry['term']} - {entry['description']} - "
                          f"追加日時: {entry['added_at']} - 理解済み: {entry['checked']}")
                index = int(input("チェックをつけたいエントリーの番号を選択してください: ")) - 1
                app.mark_as_checked(index)
                print("チェックがつけられました。")

        elif choice == '3':
            unchecked_entries = app.get_unchecked_entries()
            if not unchecked_entries:
                print("未理解の用語/問題はありません。")
            else:
                print("未理解の用語/問題の一覧:")
                for i, entry in enumerate(unchecked_entries):
                    print(f"{i+1}. {entry['term']} - {entry['description']} - "
                          f"追加日時: {entry['added_at']} - 理解済み: {entry['checked']}")

        elif choice == '4':
            entries = app.get_entries()
            if not entries:
                print("削除するエントリーがありません。")
            else:
                print("削除する用語/問題の一覧:")
                for i, entry in enumerate(entries):
                    print(f"{i+1}. {entry['term']} - {entry['description']} - "
                          f"追加日時: {entry['added_at']} - 理解済み: {entry['checked']}")
                index = int(input("削除したいエントリーの番号を選択してください: ")) - 1
                app.delete_entry(index)
                print("エントリーが削除されました。")

        elif choice == '5':
            print("アプリケーションを終了します。")
            break

        else:
            print("無効な選択です。もう一度選択してください。")

if __name__ == "__main__":
    main()
