

* sqlite에서 median을 하기 위한 extension 설치
```
PYTHON_CONFIGURE_OPTS="--enable-loadable-sqlite-extensions" pyenv install 3.10.13
```

* training 데이터를 생성한다.
```
python main.py --training --database trino --benchmark /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch
```

* dataset과 model을 생성한다.
```
python main.py --inference --database trino --benchmark /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch --create_datasets --retrain
```