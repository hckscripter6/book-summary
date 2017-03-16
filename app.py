from config import app, db
from posts import views, forms, models
from authentication import views, forms, models

#from authentication import views, models

app.debug = True
	
if __name__ == "__main__":
	app.run()
	

