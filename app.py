import models
import db
import settings
import utilities
import menu

def main_menu():
	print(settings.Greeting)

	while True:
		choice = menu.main_menu()
		if choice == 'Q':
			break
	
def main():
	models.Base.metadata.create_all(bind=db.engine)
	db.import_from_csv_to_db()
	
	if settings.DEBUG:
		print(settings.debug_warning)
		
	main_menu()
			
if __name__ == "__main__":
	main()
