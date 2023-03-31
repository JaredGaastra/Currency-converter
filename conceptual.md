### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

The differences between python and Javascript or their overal use. Python is developing the routes and backend of the application. Python allows you to create routes with the decorators and within those routes you create defs which in turn allow the developer to render html pages, set values to key words that can pull value from html items such as forms and inputs. you can use Python to create a base html and copy that information with {%%} and with that syntax you can loop through information. syntax in Python also matters. Where as JS you are more focused on syntax. Within Python you pull in blocks of "advanced methods" from pip and flask.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

The first way you can try and get C without a crash is using the get() method. get if it does not find the key it will return none for ex:
my_dict = {"a": 1, "b": 2}
value_of_c = my_dict.get("c")
print(value_of_c) # this will print "None"

The second way would be using a try-except block; This will catch the KeyError that would be raised if you try to access a missing keu directly in the except block.
my_dict = {"a": 1, "b": 2}
try:
    value_of_c = my_dict["c"]
    print(value_of_c)
except KeyError:
    print("The key 'c' is not in the dictionary")


- What is a unit test?

  A unit test in python allows you to test a unit of code or a def of code. Usually written in a seperate file. It checks whether a given unit of code behaves as expected under various input conditions.

- What is an integration test?

  A integration test, tests if youre getting proper data or data back at all from an API or a certian frame work

- What is the role of web application framework, like Flask?

Flask is a framwork it handles web requests it takes a get or a post request then throws that request to the web server and pulls back readable html elements or json elements and converts it into readable and understanable information, prodices dynamic HTML, handles forms, cookies, connects to databases provides users login/log out capabilities, cache pages for performances

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  In general, if you have a small number of parameters that are required, using a parameter in route URL can make the URL more descriptive and easier to read. On the other hand, if you have many parameters or if the parameters are optional, using URL query parameters can make the URL less cluttered and easier to manage. There is also Caching and caching efficiency: If you use URL query parameters, caching the response of a request can be more efficient since you don't have to include the query parameter in the cache key. In contrast, if you use parameter in route URL, the entire URL, including the parameter, must be included in the cache key, which can make caching less efficient.
Security: Parameter in route URL can be more secure because sensitive information is not included in the query string, which can be visible to third-party tools, analytics services, or browser history. In contrast, URL query parameters are typically less secure because they are exposed in the URL.

- How do you collect data from a URL placeholder parameter using Flask?

you can collect data from a URL placeholder parameter using the <> syntax in the route definition. The values of these parameters can be accessed in the corresponding view function using the request object.
@app.route('/foods/<food_type>')
def get_food(food_type):
    # do something with food_type
    return f"You requested information about {food_type}"


- How do you collect data from the query string using Flask?

values of query string parameters are always strings, so you may need to convert them to the appropriate data type before using them
you can collect data from the query string using the request object. The query string is the part of the URL after the ? character, and it consists of a series of key-value pairs separated by &.

def search():
    query = request.args.get('q')
    limit = request.args.get('limit')
    # do something with query and limit
    return f"Search results for {query} (limit: {limit})"


- How do you collect data from the body of the request using Flask?

you can collect data from the body of a request using the request object. The body of the request typically contains data submitted by the user via a form or as JSON data in an AJAX request.

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a small piece of data that a website stores on a user's device (usually in their web browser) to remember information about the user or their browsing session. Cookies are commonly used to store user preferences, login status, shopping cart contents, and other information that the website needs to remember between requests.

- What is the session object in Flask?

n Flask, the session object is an instance of the session class that allows you to store data across requests. The session object is implemented using cookies and signed with a secret key that ensures the data stored in the session is not tampered with.

The session object behaves like a dictionary, where you can store and retrieve data using keys. You can use the session object to store user-specific data, such as user IDs, shopping cart contents, and user preferences, which can be accessed across multiple requests.

- What does Flask's `jsonify()` do?
jsonify() function is a utility function that serializes an object into a JSON-formatted string and returns a Flask Response object with the Content-Type header set to application/json.