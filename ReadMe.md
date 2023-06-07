AnimeWatch360
AnimeWatch360 is a command-line application that allows users to manage and track their anime-watching activities. With AnimeWatch360, you can browse a list of available anime, view anime details, update your favorite anime, add new anime, delete anime, and add or delete reviews.

Usage
To launch the AnimeWatch360 application, run the following command in the terminal:


Copy code
python app.py
The main menu will be displayed, presenting various options for interacting with the application. Simply enter the corresponding number to select an option.

Browse Anime
Selecting this option will display a list of available anime titles fetched from the database. You can browse through the titles and find the anime you're interested in.

View Anime Details
Enter the ID of a specific anime to view its details, including the title, genre, episode count, status, and description. Additionally, any reviews associated with the anime will be displayed.

Update Favorite Anime
You can update your favorite anime by providing your user ID and the new favorite anime title. The application will connect to the database, update your favorite anime, and confirm the successful update.

Add Anime
This option enables you to add a new anime to the database. You will be prompted to enter the title, description, genre, episode count, and status of the anime. The application will connect to the database, add the new anime, and display a success message.

Delete Anime
You can delete an anime from the database by entering its ID. The application will connect to the database, delete the specified anime, and confirm the successful deletion.

Add Review
You can add a review for a specific anime. You will be prompted to enter the anime ID, your user ID, rating (1-5), and a comment. The application will connect to the database, add the review, and display a success message.

Delete Review
This option allows you to delete a review by entering its ID. The application will connect to the database, delete the specified review, and confirm the successful deletion.

Exit
You can choose to exit the application at any time. The application will display a farewell message and terminate.

The AnimeWatch360 application provides a convenient and organized platform for managing anime-watching activities, tracking progress, and exploring the vast world of anime. Enjoy watching!
