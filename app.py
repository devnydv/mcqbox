from mcqbox import app
from mcqbox.frontend import frontend
from mcqbox.backend import backend



app.register_blueprint(backend) 
app.register_blueprint(frontend)

if __name__=="__main__":
    app.run(debug=True)