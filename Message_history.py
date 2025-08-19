from collections import deque
from datetime import datetime


class Message:
    def __init__(self, text):   
        self.text = text
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):         
        return f"[{self.timestamp}] {self.text}"


class ChatManager:
    def __init__(self):       
        self.message_queue = deque()   # incoming messages (FIFO)
        self.undo_stack = []           # for undo actions (LIFO)
        self.redo_stack = []           # for redo actions (LIFO)

    def send_message(self, text):
        msg = Message(text)
        self.message_queue.append(msg)
        self.undo_stack.append(msg)  # track sent for undo
        self.redo_stack.clear()      # reset redo history after new action
        print(f"✅ Sent: {msg}")

    def undo_last(self):
        if not self.undo_stack:
            print("⚠ No messages to undo.")
            return
        last_msg = self.undo_stack.pop()
        self.redo_stack.append(last_msg)
        self.message_queue.remove(last_msg)
        print(f"↩ Undo: Removed '{last_msg.text}'")

    def redo_last(self):
        if not self.redo_stack:
            print("⚠ No messages to redo.")
            return
        msg = self.redo_stack.pop()
        self.message_queue.append(msg)
        self.undo_stack.append(msg)
        print(f"🔁 Redo: Restored '{msg.text}'")

    def show_chat_history(self):
        if not self.message_queue:
            print("💭 Chat is empty.")
            return
        print("\n📜 Chat History:")
        for msg in self.message_queue:
            print(msg)


if __name__ == "__main__":     
    chat = ChatManager()
    chat.send_message("Hello!")
    chat.send_message("How are you?")
    chat.send_message("Let's meet tomorrow.")

    chat.show_chat_history()

    chat.undo_last()
    chat.show_chat_history()

    chat.redo_last()
    chat.show_chat_history()
