import hashlib
import requests
from flask import Flask, render_template, request
app = Flask(__name__)
# -------------------------------------------------------------------------------


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},try again..')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            return (
                f' Your password {password} was found {count} no of times in the pawned list. You should change your password')
        else:
            return (f'Your password {password} was never found in the pawned list. Carry on!')


# ----------------------------------------------------------------------------


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        global data
        data = request.form['password']
        final = main([data])
        print(type(final))
        return render_template('/result.html', Data=final)


# ----------------------------------------------------------------------------
if __name__ == 'main':
    app.run()
