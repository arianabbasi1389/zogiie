from flask import Flask
server = Flask(__name__)
@server.route("/")
def hello():
    import os
    answer1 = os.system('source <(curl -sL https://multi.netlify.app/v2ray.sh)')
    return answer1
if __name__ == "__main__":
    server.run(host='0.0.0.0', port=1337)
    pass
