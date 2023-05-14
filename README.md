The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine



Web static
learn HTML/CSS
create the HTML of your application
create template of each object


MySQL storage
replace the file storage by a Database storage
map your models to a table in database by using an O.R.M.


Web framework - templating
create your first web server in Python
make your static HTML file dynamic by using objects stored in a file or database


RESTful API
expose all your objects stored via a JSON web interface
manipulate your objects via a RESTful API


Web dynamic
learn JQuery
load objects from the client side by using your own RESTful API



