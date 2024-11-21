# apis/app.py
from apis import thomas_app

app = thomas_app()

if __name__ == '__main__':
    app.run(debug=True)
