from flask import Flask, request, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.route('/img/<filename>')
def get_img(filename):
    with open('/path/to/log.txt','a') as f:
        timestamp = datetime.strftime('%Y-%m-%d %H:%M:%S')
        f.write('{0} {1} {2}\n'.format(timestamp, request.remote_addr, filename))
    return send_from_directory('/path/to/img/', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

