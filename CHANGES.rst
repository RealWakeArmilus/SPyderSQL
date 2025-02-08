==========
Changelog
==========


0.3.0 (2025-02-08)
==================

🏆 What makes this class efficient and safe?
✅ Prevents memory leaks

Uses async with for cursors, preventing leaks.
Automatically closes the connection (await db.close()).
Manages the connection without creating new connections for each request.
✅ Flexible

You can get data one row at a time (fetch_stream), if there is a lot of data.
Supports bulk execution (execute_many), which is faster when inserting large data.
✅ Simple and readable

Works with aiosqlite.Row, allowing you to access fields as a dictionary (row["name"]).

----

This class solves all the main problems of aiosqlite: ✔ Safe connections (no memory leaks).
✔ Flexibility (fetchone, fetchall, fetch_stream methods).
✔ Suitable for FastAPI and asynchronous services.
✔ Optimization of work with SQLite (bulk inserts, lazy queries).

🔥 Ready to use in any asynchronous project! 🚀


----


Features
--------

- Class SecurityAsyncSQLite




0.2.0 (2025-01-01) 🎉🎉🎉 HAPPY NEW YEAR 🎉🎉🎉
==================

Features
--------

- Add AsyncSQLite.py
- more flexible and advanced functionality
- add request WHERE
- add request LIMIT
- add request ORDER BY
- add request UPDATE
- add request DELETE
- add async EXECUTE
- add async EXECUTEMANY
- add async FETCH ONE

Misc
--------

- Fixed Bug
- more secure queries from SQL-injections


0.1.3 (2024-12-21)
==================

Debug
--------

- Insert SQL-request

Misc
-----

- Fixed design of the project
- Added __meta__.py
- Added directory .client


0.1.2 (2024-12-13)
==================

Features
--------

- Added SQLite
- Added TypesSQLite

Misc
-----

- Fixed design of the project
- Added __meta__.py
- Added directory .client
