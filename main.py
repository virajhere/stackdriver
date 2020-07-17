
from google.cloud import logging
from flask import Flask, request

# Instantiates a client
logging_client = logging.Client()

# The name of the log to write to
log_name = 'demo'
# Selects the log to write to
logger = logging_client.logger(log_name)

app = Flask(__name__)

class StringProcessor():
    def __init__(self, string):
        self._string = string

    def Reverse(self):
        if self._string == '':
            return ''

        chars = [c for c in self._string]
        left = 0
        right = len(chars) - 1
        while True:
            tmp = chars[left]
            chars[left] = chars[right]
            chars[right] = tmp
            if left >= right:
                break
            left += 1
            right -= 1

        return ''.join(chars)

@app.route('/reverse_string', methods=['GET'])
def ReverseString():
    logger.log_text("INFO: Data is submitted by end user")
    try:
        s = str(request.args.get('string'))
    except Exception as e:
        print(e)
        return 'Not a valid string!'

    current = StringProcessor(s).Reverse()
    expected = s[::-1]
    return '''
        <table>
            <tr><th>Program Output:</th><th>{}</th></tr>
            <tr><th>Correct Output:</th><th>{}</th><tr>
        </table>
    '''.format(current, expected)


@app.route('/')
def Hello():
    """Return a friendly HTTP greeting."""
    return '''
        Hello! Enter a string to reverse it.
        <form method="get" action="reverse_string">
            <p><input type=text name=string value="abcd">
            <p><input type=submit>
        </form>
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
