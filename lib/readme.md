# CRUD operations using SQLAlchemy:

1. Create (Insert):
   - Create an instance of the model class.
   - Add the instance to a session using `session.add()`.
   - Commit the session using `session.commit()` to persist the changes.

2. Read (Query):
   - Create a session using `Session()`.
   - Query the desired data using `session.query(Model)`.
   - Use methods such as `all()`, `first()`, `filter()`, or `filter_by()` to retrieve the data.
   - Iterate over the results or access specific attributes of the queried objects.
   - Close the session using `session.close()`.

3. Update:
   - Create a session using `Session()`.
   - Query the object to be updated using `session.query(Model).filter_by(condition).first()`.
   - Modify the attributes of the queried object.
   - Commit the session using `session.commit()` to persist the changes.
   - Close the session using `session.close()`.

4. Delete:
   - Create a session using `Session()`.
   - Query the object to be deleted using `session.query(Model).filter_by(condition).first()`.
   - Delete the object using `session.delete(obj)`.
   - Commit the session using `session.commit()` to persist the changes.
   - Close the session using `session.close()`.

Remember to replace `Model` with the appropriate model class name and adapt the code according to your specific database schema and requirements.


# List of methods

# Query Methods:
- `all()`: Retrieves all objects that match the query.
- `first()`: Retrieves the first object that matches the query.
- `filter()`: Filters the query based on specified conditions.
- `filter_by()`: Filters the query based on keyword arguments.
- `order_by()`: Orders the query results based on specified columns.
- `join()`: Performs an SQL join with another table.
- `group_by()`: Groups the query results based on specified columns.
- `distinct()`: Returns only distinct (unique) results.
- `limit()`: Limits the number of results returned.
- `offset()`: Skips a specified number of results.
- `count()`: Returns the count of matching records.

# Update Methods:
- `update()`: Updates the records that match specified conditions with new values.
- `values()`: Sets the values to be updated in the `update()` method.

# Delete Methods:
- `delete()`: Deletes the records that match specified conditions.

# Relationship Methods:
- `relationship()`: Defines a relationship between two models.
- `backref()`: Specifies a back-reference to the relationship.

# Transaction Methods:
- `commit()`: Commits the session and persists the changes to the database.
- `rollback()`: Rolls back the session, undoing any uncommitted changes.

# Session Methods:
- `add()`: Adds an object to the session.
- `add_all()`: Adds a list of objects to the session.
- `merge()`: Merges the state of an object into the session.
- `expunge()`: Removes an object from the session.
- `flush()`: Flushes any pending changes to the database.
- `query()`: Begins a new query.

