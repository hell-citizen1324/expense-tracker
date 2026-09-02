import threading
import time

import uvicorn
import webview

from main import app


def start_server():
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )


server_thread = threading.Thread(
    target=start_server,
    daemon=True
)

server_thread.start()


time.sleep(1)


webview.create_window(
    "Expense Tracker",
    "http://127.0.0.1:8000",
    width=1000,
    height=700
)

webview.start()
