# AutoSteer

## License

This prototype implementation is licensed under the 'MIT license' (see LICENSE).

## Requirements

### Packages

- sqlite3
- python3

### Python3 requirements

- Install python requirements using the file `pip3 install -r requirements.txt`

## Run AutoSteer

### Database Systems

#### AutoSteer-G already supports five open-source database systems:

- PostgreSQL
    - We tested AutoSteer with PostgreSQL 13
- PrestoDB
    - PrestoDB does not expose many rewrite rules. Therefore, the following patch exposes the top-7 hints we found in
      our experiments.
    - Get the most recent version of [PrestoDB](https://github.com/prestodb/presto)
    - Apply the PrestoDB patch : `git apply Presto-disable-optimizers-through-session-properties.patch`
    - Build PrestoDB from source and start the server
- MySQL
- DuckDB
    - Install the DuckDB-python package via `pip`
- SparkSQL
    - We run SparkSQL using the official Docker image of its most recent version

#### DBMS Configuration

Depending on your custom installation and DBMS setup, add the required information to the `configs/<dbms>.cfg`-file.

### Executing AutoSteer's Training Mode

AutoSteer's training mode execution consists of two steps:

1. (A) Approximate the query span, and (B) run the dynamic programming-based hint-set exploration 
   ```
   trainingmode.py --database {postgres|presto|mysql|duckdb|spark} --benchmark {path-to-sql-queries}
   ```
2. By now, AutoSteer persisted all generated training data (e.g. query plans and execution statistics) in the
   sqlite-database `results.sqlite`.
3. Train BaoNet: TBA

## Code Formatting

- All python files will be checked using `pylint` before they can be comitted. The code style is primarily based on
  the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), however, it allows much longer
  lines (160 characters).
- Please, install and run pylint (there is also a git pre-commit hook) before committing