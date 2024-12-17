from quart import Quart
from routes import Route
from quart_cors import cors

class BimbelAgape():
    def __init__(self) -> None:
        self.app = Quart(__name__)
        self.app_cors = cors(self.app, allow_origin="*")
        Route(self.app_cors)

    # def run(self, debug: bool = True, host: str = '0.0.0.0', port: int = 2323) -> None:
    #     self.app.run(debug=debug, host=host, port=port)

app = BimbelAgape().app_cors

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host='0.0.0.0', port=2323, reload=True, workers=1)