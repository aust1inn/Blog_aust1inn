from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author':'Austin Omondi',
        'title':'Flask Intro',
        'content':'Working with templates',
        'date_posted':'April 20,2022'
    },

    {
        'author':'Corey Schafer',
        'title':'Angular Intro',
        'content':'Working with Directives',
        'date_posted':'April 10,2022'
    }
]

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html' , posts=posts)

@app.route('/about')
def about():
    return render_template('about.html' , title="about")    

if __name__ == '__main__':
    app.run(debug = True)    