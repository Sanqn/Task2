👨‍💻 About me
Alex Davidchik
image
# 👨‍💻 Alex Davidchik

# 🧐 Find Me)
* 💻 linkedin: https://www.linkedin.com/in/davidchik/
* 📧 email: alex.davidchik@gmail.com


# Test task 2.
1. Initially, you need to track traffic from www.wildberries.ru and find HTTP
a request that sends data about the brand and name in JSON format
article. Product page example:
https://www.wildberries.ru/catalog/73512949/detail.aspx
2. Next, you need to implement an API that accepts an xlsx file with
articles (articles must be entered line by line in the first column) or
one article (not in the file, but only one value). The API should have
two inputs: a file or one value, one thing must be transferred.
3. The API must interact asynchronously with the found HTTP request in
the first paragraph and receive data about the product card. From the received data
need to make a PyDantic object.
4. The successful result of the API is the return of data about the brand and
article name in JSON format. Example: information about one article -
{"article": 123, "brand": "brand", "title": "Title"}; articles from file - [{"article": 1,
"brand": "Brand1", "title": "Title1"}, {"article": 2, "brand": "Brand2", "title": "Title2"}]

# Installation and implementation

1. Create a folder where the application will be stored
2. Create a virtual environment in your folder
3. Download the application from the link - https://github.com/Sanqn/Task2.git
   (in the terminal of your ide, enter the command 'git clone https://github.com/Sanqn/Task2.git')
4. For the program to work correctly, go to the directory containing the manage.py file and
   pip install -r requirements.txt install all dependencies.
5. In task2/settings.py, in the DATABASES section, specify the Postgres database settings
6. Perform database migrations with the command python manage.py migrate
7. Start the server with python manage.py runserver and follow the link
   Starting development server at http://127.0.0.1:8000/
8. Follow the link indicated on the "wbdata" page: "http://127.0.0.1:8000/wbdata/"
9. Upload the xlsx file (for example, upload the test_file.xlsx file) or in the window (article) specify
   a value of this type: 73512949 and press post, wait for a response.

   ![Image text](https://i.ibb.co/hC1fKbq/Screen1.png)
10. If you upload a file with a different extension, a warning will appear.
11. The received data is stored in the database, if the next request the articles are repeated, 
    the data is not added to the database.
