import logging

from flask import Flask, request

# Enable cloud debugger
try:
    import googleclouddebugger
    googleclouddebugger.enable()
except ImportError:
    pass

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


# There is a bug in the code.
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
