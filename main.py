from flask import Flask, request
app = Flask(__name__)
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
