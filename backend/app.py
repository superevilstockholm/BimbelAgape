from quart import Quart

class BimbelAgape():
    def __init__(self) -> None:
        self.app = Quart(__name__)

    def run(self, debug: bool = True, host: str = '0.0.0.0', port: int = 2323) -> None:
        self.app.run(debug=debug, host=host, port=port)

app = BimbelAgape()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host='127.0.0.1', port=2323, reload=True, workers=1)