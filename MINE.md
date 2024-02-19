

* sqlite에서 median을 하기 위한 extension 설치
```
# PYTHON_CONFIGURE_OPTS="--enable-loadable-sqlite-extensions" pyenv install 3.10.13
```

* training 데이터를 생성한다.
```
# python main.py --training --database trino --benchmark /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch
```

* dataset과 model을 생성한다.
```
# python main.py --inference --database trino --benchmark /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch --create_datasets --retrain
```

```
# python main.py --inference --database trino --benchmark /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch --retrain                  
Use CUDA: False
2024-02-19 15:27:13 INFO     Run AutoSteer's inference mode
2024-02-19 15:27:13 INFO     training samples: 319, test samples: 118
2024-02-19 15:27:13 INFO     training samples: 319, test samples: 118
2024-02-19 15:27:13 INFO     Initial input channels: 19
2024-02-19 15:27:14 INFO     Epoch 0    train. loss     0.3128
2024-02-19 15:27:14 INFO     Epoch 0    test loss       0.0725
2024-02-19 15:27:15 INFO     Epoch 1    train. loss     0.0720
2024-02-19 15:27:15 INFO     Epoch 1    test loss       0.1609
2024-02-19 15:27:15 INFO     Epoch 2    train. loss     0.0520
2024-02-19 15:27:15 INFO     Epoch 2    test loss       0.1574
2024-02-19 15:27:16 INFO     Epoch 3    train. loss     0.0387
2024-02-19 15:27:16 INFO     Epoch 3    test loss       0.1711
2024-02-19 15:27:17 INFO     Epoch 4    train. loss     0.0311
2024-02-19 15:27:17 INFO     Epoch 4    test loss       0.1728
2024-02-19 15:27:18 INFO     Epoch 5    train. loss     0.0284
2024-02-19 15:27:18 INFO     Epoch 5    test loss       0.1882
2024-02-19 15:27:18 INFO     Epoch 6    train. loss     0.0240
2024-02-19 15:27:18 INFO     Epoch 6    test loss       0.1924
2024-02-19 15:27:19 INFO     Epoch 7    train. loss     0.0207
2024-02-19 15:27:19 INFO     Epoch 7    test loss       0.1772
2024-02-19 15:27:20 INFO     Epoch 8    train. loss     0.0237
2024-02-19 15:27:20 INFO     Epoch 8    test loss       0.1791
2024-02-19 15:27:20 INFO     Epoch 9    train. loss     0.0171
2024-02-19 15:27:20 INFO     Epoch 9    test loss       0.1651
2024-02-19 15:27:21 INFO     Epoch 10   train. loss     0.0135
2024-02-19 15:27:21 INFO     Epoch 10   test loss       0.1823
2024-02-19 15:27:22 INFO     Epoch 11   train. loss     0.0135
2024-02-19 15:27:22 INFO     Epoch 11   test loss       0.1845
2024-02-19 15:27:23 INFO     Epoch 12   train. loss     0.0147
2024-02-19 15:27:23 INFO     Epoch 12   test loss       0.1923
2024-02-19 15:27:23 INFO     Epoch 13   train. loss     0.0102
2024-02-19 15:27:23 INFO     Epoch 13   test loss       0.1719
2024-02-19 15:27:24 INFO     Epoch 14   train. loss     0.0094
2024-02-19 15:27:24 INFO     Epoch 14   test loss       0.1951
2024-02-19 15:27:25 INFO     Epoch 15   train. loss     0.0106
2024-02-19 15:27:25 INFO     Epoch 15   test loss       0.1424
2024-02-19 15:27:25 INFO     Epoch 16   train. loss     0.0093
2024-02-19 15:27:25 INFO     Epoch 16   test loss       0.1875
2024-02-19 15:27:26 INFO     Epoch 17   train. loss     0.0100
2024-02-19 15:27:26 INFO     Epoch 17   test loss       0.1830
2024-02-19 15:27:27 INFO     Epoch 18   train. loss     0.0100
2024-02-19 15:27:27 INFO     Epoch 18   test loss       0.1888
2024-02-19 15:27:28 INFO     Epoch 19   train. loss     0.0093
2024-02-19 15:27:28 INFO     Epoch 19   test loss       0.1796
2024-02-19 15:27:28 INFO     Epoch 20   train. loss     0.0078
2024-02-19 15:27:28 INFO     Epoch 20   test loss       0.1697
2024-02-19 15:27:29 INFO     Epoch 21   train. loss     0.0079
2024-02-19 15:27:29 INFO     Epoch 21   test loss       0.2016
2024-02-19 15:27:30 INFO     Epoch 22   train. loss     0.0073
2024-02-19 15:27:30 INFO     Epoch 22   test loss       0.1755
2024-02-19 15:27:31 INFO     Epoch 23   train. loss     0.0072
2024-02-19 15:27:31 INFO     Epoch 23   test loss       0.1630
2024-02-19 15:27:31 INFO     Epoch 24   train. loss     0.0077
2024-02-19 15:27:31 INFO     Epoch 24   test loss       0.2028
2024-02-19 15:27:32 INFO     Epoch 25   train. loss     0.0079
2024-02-19 15:27:32 INFO     Epoch 25   test loss       0.1612
2024-02-19 15:27:33 INFO     Epoch 26   train. loss     0.0074
2024-02-19 15:27:33 INFO     Epoch 26   test loss       0.1549
2024-02-19 15:27:33 INFO     Epoch 27   train. loss     0.0061
2024-02-19 15:27:33 INFO     Epoch 27   test loss       0.1480
2024-02-19 15:27:34 INFO     Epoch 28   train. loss     0.0073
2024-02-19 15:27:34 INFO     Epoch 28   test loss       0.1796
2024-02-19 15:27:35 INFO     Epoch 29   train. loss     0.0062
2024-02-19 15:27:35 INFO     Epoch 29   test loss       0.1840
2024-02-19 15:27:36 INFO     Epoch 30   train. loss     0.0067
2024-02-19 15:27:36 INFO     Epoch 30   test loss       0.1717
2024-02-19 15:27:36 INFO     Epoch 31   train. loss     0.0060
2024-02-19 15:27:36 INFO     Epoch 31   test loss       0.1808
2024-02-19 15:27:37 INFO     Epoch 32   train. loss     0.0055
2024-02-19 15:27:37 INFO     Epoch 32   test loss       0.1711
2024-02-19 15:27:38 INFO     Epoch 33   train. loss     0.0059
2024-02-19 15:27:38 INFO     Epoch 33   test loss       0.1442
2024-02-19 15:27:39 INFO     Epoch 34   train. loss     0.0060
2024-02-19 15:27:39 INFO     Epoch 34   test loss       0.1762
2024-02-19 15:27:39 INFO     Epoch 35   train. loss     0.0057
2024-02-19 15:27:39 INFO     Epoch 35   test loss       0.1626
2024-02-19 15:27:40 INFO     Epoch 36   train. loss     0.0060
2024-02-19 15:27:40 INFO     Epoch 36   test loss       0.1960
2024-02-19 15:27:41 INFO     Epoch 37   train. loss     0.0054
2024-02-19 15:27:41 INFO     Epoch 37   test loss       0.1792
2024-02-19 15:27:41 INFO     Epoch 38   train. loss     0.0051
2024-02-19 15:27:41 INFO     Epoch 38   test loss       0.1987
2024-02-19 15:27:42 INFO     Epoch 39   train. loss     0.0056
2024-02-19 15:27:42 INFO     Epoch 39   test loss       0.1844
2024-02-19 15:27:43 INFO     Epoch 40   train. loss     0.0045
2024-02-19 15:27:43 INFO     Epoch 40   test loss       0.1420
2024-02-19 15:27:44 INFO     Epoch 41   train. loss     0.0047
2024-02-19 15:27:44 INFO     Epoch 41   test loss       0.1634
2024-02-19 15:27:44 INFO     Epoch 42   train. loss     0.0057
2024-02-19 15:27:44 INFO     Epoch 42   test loss       0.1714
2024-02-19 15:27:45 INFO     Epoch 43   train. loss     0.0048
2024-02-19 15:27:45 INFO     Epoch 43   test loss       0.1713
2024-02-19 15:27:46 INFO     Epoch 44   train. loss     0.0050
2024-02-19 15:27:46 INFO     Epoch 44   test loss       0.1647
2024-02-19 15:27:46 INFO     Epoch 45   train. loss     0.0051
2024-02-19 15:27:46 INFO     Epoch 45   test loss       0.1733
2024-02-19 15:27:47 INFO     Epoch 46   train. loss     0.0049
2024-02-19 15:27:47 INFO     Epoch 46   test loss       0.1652
2024-02-19 15:27:48 INFO     Epoch 47   train. loss     0.0039
2024-02-19 15:27:48 INFO     Epoch 47   test loss       0.1792
2024-02-19 15:27:49 INFO     Epoch 48   train. loss     0.0045
2024-02-19 15:27:49 INFO     Epoch 48   test loss       0.1758
2024-02-19 15:27:49 INFO     Epoch 49   train. loss     0.0040
2024-02-19 15:27:49 INFO     Epoch 49   test loss       0.1486
2024-02-19 15:27:50 INFO     Epoch 50   train. loss     0.0047
2024-02-19 15:27:50 INFO     Epoch 50   test loss       0.1625
2024-02-19 15:27:51 INFO     Epoch 51   train. loss     0.0043
2024-02-19 15:27:51 INFO     Epoch 51   test loss       0.1534
2024-02-19 15:27:52 INFO     Epoch 52   train. loss     0.0042
2024-02-19 15:27:52 INFO     Epoch 52   test loss       0.1761
2024-02-19 15:27:52 INFO     Epoch 53   train. loss     0.0039
2024-02-19 15:27:52 INFO     Epoch 53   test loss       0.1645
2024-02-19 15:27:53 INFO     Epoch 54   train. loss     0.0036
2024-02-19 15:27:53 INFO     Epoch 54   test loss       0.1781
2024-02-19 15:27:54 INFO     Epoch 55   train. loss     0.0048
2024-02-19 15:27:54 INFO     Epoch 55   test loss       0.1602
2024-02-19 15:27:54 INFO     Epoch 56   train. loss     0.0044
2024-02-19 15:27:54 INFO     Epoch 56   test loss       0.1581
2024-02-19 15:27:54 INFO     Stopped training from convergence condition at epoch 56
2024-02-19 15:27:55 INFO     training_loss: [0.31276654470711945, 0.07201164551079273, 0.05196949141100049, 0.03872177670709789, 0.03112309444695711, 0.02842859080992639, 0.024041742319241166, 0.020703082112595438, 0.023702027602121235, 0.017136943899095057, 0.013451573811471463, 0.01354407323524356, 0.014680134877562524, 0.010212788765784353, 0.00939101497642696, 0.01060460419394076, 0.009305348852649331, 0.009973489574622362, 0.010009545780485496, 0.009256986260879785, 0.0077782584819942715, 0.007895169011317194, 0.0072527157259173695, 0.0071935513988137245, 0.0076568918768316506, 0.007863333984278142, 0.007420987472869456, 0.006088321842253208, 0.007306096400134266, 0.00617357601877302, 0.0066683995071798565, 0.005968407483305782, 0.0054615091881714765, 0.005920646851882339, 0.006014099152525887, 0.0056839945493265985, 0.006005229183938354, 0.005410517985001207, 0.005112300638575107, 0.00563171518733725, 0.0045079541916493325, 0.004713920608628542, 0.005711742833955214, 0.00483002740656957, 0.0050292921543587, 0.0051015532691963015, 0.004896292655030265, 0.003949591802665964, 0.0044580654241144655, 0.003960438899230212, 0.004693282477091998, 0.0042903657827992, 0.004235501529183239, 0.003912947146454826, 0.0035983564041089265, 0.0047657514340244235, 0.004367617523530498]
2024-02-19 15:27:55 INFO     test_loss: [0.07247269712388515, 0.1609488446265459, 0.15740648191422224, 0.17108980752527714, 0.17282929457724094, 0.18819093331694603, 0.19235103391110897, 0.17724926490336657, 0.17905197478830814, 0.16513105668127537, 0.1823496576398611, 0.18453615345060825, 0.1922515258193016, 0.17189845442771912, 0.19511354342103004, 0.14241038914769888, 0.1875363029539585, 0.1829562969505787, 0.18877789191901684, 0.1795903816819191, 0.16967958211898804, 0.20164993777871132, 0.1754876673221588, 0.16299869492650032, 0.2028419766575098, 0.161194559186697, 0.15490572713315487, 0.14798489399254322, 0.17964860145002604, 0.1839909665286541, 0.1716841198503971, 0.18081476166844368, 0.1710511241108179, 0.1442073890939355, 0.17620121501386166, 0.1625961847603321, 0.19604001194238663, 0.17923064157366753, 0.19869565404951572, 0.18436961993575096, 0.14203739259392023, 0.16339262574911118, 0.1714426577091217, 0.17134314216673374, 0.1646856851875782, 0.1733128447085619, 0.1651684483513236, 0.1791501920670271, 0.1758097168058157, 0.14856813475489616, 0.16250640898942947, 0.1533534023910761, 0.17610069550573826, 0.1644886638969183, 0.1780535951256752, 0.16016955953091383, 0.1580779505893588]

2024-02-19 15:27:55 INFO     Load Bao regression model from directory nn/model/trino_model ...
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/10.sql
2024-02-19 15:27:55 INFO     y: 55500.00        55500.00        56000.00        56000.00        56500.00        56500.00        57000.00        57000.00        57500.00        57500.00        57500.00        57500.00        58000.00 58000.00 58000.00        58000.00        58000.00        58500.00        59500.00        60000.00        60500.00        60500.00        60500.00        60500.00        61000.00        61500.00        61500.00        61500.00        61500.00  63000.00        63500.00        63500.00        63500.00        64500.00        65500.00        65500.00        66500.00        66500.00        67500.00        68000.00        69000.00        77000.00        78000.00
2024-02-19 15:27:55 INFO     ŷ: 241485.62       228195.23       200604.00       241485.62       200604.00       200604.00       228195.23       241485.62       241485.62       228195.23       241485.62       188610.70       200604.00241485.62        241485.62       200604.00       193832.38       200604.00       241485.62       241485.62       241485.62       241485.62       241485.62       241485.62       241485.62       228195.23       188610.70       228195.23188610.70        241485.62       241485.62       188610.70       241485.62       200604.00       200604.00       228195.23       241485.62       241485.62       228195.23       200604.00       200604.00       200604.00       241485.62
2024-02-19 15:27:55 INFO     min predicted index: 11 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 57500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/10.sql, query_id: 2, optimizer_config: 44, disabled_rules: None, walltime: 78000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/10.sql, query_id: 2, optimizer_config: 102, disabled_rules: optimize_hash_generation,prune_project_columns,prune_tablescan_columns, walltime: 57500.0
2024-02-19 15:27:55 INFO     y[0]: 55500.0
2024-02-19 15:27:55 INFO     best choice -> 0.7115384615384616
2024-02-19 15:27:55 INFO     good choice -> 0.7371794871794872
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/11.sql
2024-02-19 15:27:55 INFO     y: 52000.00        52500.00        55500.00        56000.00        56500.00        56500.00        57500.00        60000.00        64000.00        65500.00        69000.00
2024-02-19 15:27:55 INFO     ŷ: 258660.84       258654.42       258660.84       258660.84       258654.42       258660.84       258654.42       258654.42       258654.42       274183.59       237690.05
2024-02-19 15:27:55 INFO     min predicted index: 10 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 69000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/11.sql, query_id: 3, optimizer_config: 109, disabled_rules: None, walltime: 60000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/11.sql, query_id: 3, optimizer_config: 116, disabled_rules: prune_tablescan_columns, walltime: 69000.0
2024-02-19 15:27:55 INFO     y[0]: 52000.0
2024-02-19 15:27:55 INFO     best choice -> 0.8666666666666667
2024-02-19 15:27:55 INFO     bad choice -> 1.15
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/18.sql
2024-02-19 15:27:55 INFO     y: 44000.00        46000.00        46000.00        47000.00        47500.00        49000.00        49000.00        49500.00        49500.00        51500.00        51500.00        53000.00        53000.00 53500.00 53500.00        54500.00        54500.00        55000.00        55000.00        56000.00        56000.00        56500.00        57500.00        58500.00        69500.00        70500.00        71000.00        72000.00        73000.00  73500.00        74500.00        75000.00        75000.00        76000.00        77500.00        78500.00        79000.00        79000.00        79500.00        81500.00        82500.00        86000.00        86500.00
2024-02-19 15:27:55 INFO     ŷ: 136573.95       198852.58       141509.52       162932.86       157063.64       136573.95       175870.67       171579.17       147850.27       162216.86       146975.14       155185.38       146975.14172355.55        171579.17       157063.64       162216.86       172355.55       172355.55       199036.05       135328.62       199036.05       172355.55       146975.14       166335.25       192381.17       206835.34       212828.70201852.55        195356.91       192381.17       212808.20       212828.70       206835.34       188348.62       212828.70       212808.20       206835.34       212808.20       206852.50       212808.20       206852.50       192381.17
2024-02-19 15:27:55 INFO     min predicted index: 20 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 56000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/18.sql, query_id: 10, optimizer_config: 229, disabled_rules: None, walltime: 86000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/18.sql, query_id: 10, optimizer_config: 285, disabled_rules: optimize_hash_generation,prune_filter_columns,prune_tablescan_columns, walltime: 56000.0
2024-02-19 15:27:55 INFO     y[0]: 44000.0
2024-02-19 15:27:55 INFO     best choice -> 0.5116279069767442
2024-02-19 15:27:55 INFO     good choice -> 0.6511627906976745
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/19.sql
2024-02-19 15:27:55 INFO     y: 73000.00        73000.00        73000.00        74000.00        75000.00        76000.00        77500.00        77500.00        78500.00        78500.00        80500.00        80500.00        83000.00 84500.00 89000.00        932500.00       936000.00       939500.00       943500.00       963500.00       967000.00
2024-02-19 15:27:55 INFO     ŷ: 166772.70       166772.70       166772.70       159800.62       177399.55       177399.55       177399.55       159800.62       177399.55       159801.55       166772.70       177399.55       159801.55177399.55        177399.55       161110.05       148774.88       161110.05       148774.88       161140.00       161140.00
2024-02-19 15:27:55 INFO     min predicted index: 16 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 936000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/19.sql, query_id: 11, optimizer_config: 294, disabled_rules: None, walltime: 967000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/19.sql, query_id: 11, optimizer_config: 317, disabled_rules: prune_tablescan_columns,simplify_expressions, walltime: 936000.0
2024-02-19 15:27:55 INFO     y[0]: 73000.0
2024-02-19 15:27:55 INFO     best choice -> 0.07549120992761117
2024-02-19 15:27:55 INFO     good choice -> 0.96794208893485
2024-02-19 15:27:55 INFO     Load Bao regression model from directory nn/model/trino_model ...
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/1.sql
2024-02-19 15:27:55 INFO     y: 26000.00        26500.00        28000.00        28000.00        28500.00        28500.00        29500.00        30000.00        30000.00        30500.00        30500.00        31000.00        32000.00 32500.00 33000.00        33500.00        35000.00        39500.00        40500.00        42000.00        46500.00        62000.00
2024-02-19 15:27:55 INFO     ŷ: 135568.89       158333.11       158333.11       135568.89       158333.11       158333.11       158548.42       135568.89       135568.89       135568.89       135568.89       158548.42       114847.27158333.11        135568.89       158333.11       132607.75       135197.05       132607.75       158333.11       135197.05       158333.11
2024-02-19 15:27:55 INFO     min predicted index: 12 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 32000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/1.sql, query_id: 1, optimizer_config: 1, disabled_rules: None, walltime: 62000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/1.sql, query_id: 1, optimizer_config: 37, disabled_rules: optimize_hash_generation,prune_project_columns,prune_tablescan_columns, walltime: 32000.0
2024-02-19 15:27:55 INFO     y[0]: 26000.0
2024-02-19 15:27:55 INFO     best choice -> 0.41935483870967744
2024-02-19 15:27:55 INFO     good choice -> 0.5161290322580645
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/12.sql
2024-02-19 15:27:55 INFO     y: 35500.00        36000.00        36000.00        36500.00        36500.00        37500.00        38000.00        38000.00        39000.00        39000.00        39000.00        39500.00        39500.00 39500.00 39500.00        41000.00        41000.00        41000.00        41500.00        42000.00        42500.00        42500.00        43500.00        45500.00        46500.00        52000.00        57000.00        60500.00
2024-02-19 15:27:55 INFO     ŷ: 134203.28       152042.50       151057.39       178856.92       151057.39       151057.39       152042.50       151057.39       152042.50       152042.50       163703.36       178856.92       178856.92178856.92        178856.92       178856.92       178856.92       134203.28       152042.50       178856.92       152042.50       134203.28       178856.92       178856.92       178856.92       152042.50       178856.92       178856.92
2024-02-19 15:27:55 INFO     min predicted index: 0 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 35500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/12.sql, query_id: 4, optimizer_config: 128, disabled_rules: None, walltime: 57000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/12.sql, query_id: 4, optimizer_config: 148, disabled_rules: optimize_hash_generation,prune_tablescan_columns, walltime: 35500.0
2024-02-19 15:27:55 INFO     y[0]: 35500.0
2024-02-19 15:27:55 INFO     best choice -> 0.6228070175438597
2024-02-19 15:27:55 INFO     good choice -> 0.6228070175438597
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/13.sql
2024-02-19 15:27:55 INFO     y: 165000.00       210000.00       231500.00       235000.00       264500.00       273500.00       279500.00
2024-02-19 15:27:55 INFO     ŷ: 351784.78       351784.78       396318.72       396318.72       308420.94       396318.72       396318.72
2024-02-19 15:27:55 INFO     min predicted index: 4 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 264500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/13.sql, query_id: 5, optimizer_config: 172, disabled_rules: None, walltime: 235000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/13.sql, query_id: 5, optimizer_config: 176, disabled_rules: optimize_hash_generation, walltime: 264500.0
2024-02-19 15:27:55 INFO     y[0]: 165000.0
2024-02-19 15:27:55 INFO     best choice -> 0.7021276595744681
2024-02-19 15:27:55 INFO     bad choice -> 1.125531914893617
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/14.sql
2024-02-19 15:27:55 INFO     y: 70000.00        72000.00        72000.00        74000.00        74000.00        77500.00        79000.00
2024-02-19 15:27:55 INFO     ŷ: 235571.02       235571.02       235571.02       235571.02       225340.80       213564.11       235571.02
2024-02-19 15:27:55 INFO     min predicted index: 5 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 77500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/14.sql, query_id: 6, optimizer_config: 182, disabled_rules: None, walltime: 72000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/14.sql, query_id: 6, optimizer_config: 189, disabled_rules: prune_tablescan_columns, walltime: 77500.0
2024-02-19 15:27:55 INFO     y[0]: 70000.0
2024-02-19 15:27:55 INFO     best choice -> 0.9722222222222222
2024-02-19 15:27:55 INFO     bad choice -> 1.0763888888888888
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/15.sql
2024-02-19 15:27:55 INFO     y: 49000.00        51500.00        51500.00        52000.00        52000.00        53000.00        54000.00        54500.00        56500.00        58000.00        58500.00        59000.00        64500.00
2024-02-19 15:27:55 INFO     ŷ: 183611.45       183566.98       183611.45       149575.98       149575.98       149575.98       183611.45       183611.45       183611.45       152710.53       183611.45       183566.98       183611.45
2024-02-19 15:27:55 INFO     min predicted index: 3 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 52000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/15.sql, query_id: 7, optimizer_config: 191, disabled_rules: None, walltime: 54500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/15.sql, query_id: 7, optimizer_config: 195, disabled_rules: optimize_hash_generation, walltime: 52000.0
2024-02-19 15:27:55 INFO     y[0]: 49000.0
2024-02-19 15:27:55 INFO     best choice -> 0.8990825688073395
2024-02-19 15:27:55 INFO     good choice -> 0.9541284403669725
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/16.sql
2024-02-19 15:27:55 INFO     y: 163000.00       212000.00       244500.00       263500.00       291500.00       292500.00       296500.00       300000.00
2024-02-19 15:27:55 INFO     ŷ: 455158.97       430808.44       462073.69       551045.75       496941.22       522993.38       593708.62       551015.81
2024-02-19 15:27:55 INFO     min predicted index: 1 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 212000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/16.sql, query_id: 8, optimizer_config: 206, disabled_rules: None, walltime: 263500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/16.sql, query_id: 8, optimizer_config: 213, disabled_rules: prune_tablescan_columns, walltime: 212000.0
2024-02-19 15:27:55 INFO     y[0]: 163000.0
2024-02-19 15:27:55 INFO     best choice -> 0.618595825426945
2024-02-19 15:27:55 INFO     good choice -> 0.8045540796963947
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/17.sql
2024-02-19 15:27:55 INFO     y: 65500.00        67500.00        68000.00        69000.00        71500.00        73000.00        73500.00        76500.00
2024-02-19 15:27:55 INFO     ŷ: 202758.56       202758.56       195116.34       208353.44       223574.81       212622.38       188581.20       202759.92
2024-02-19 15:27:55 INFO     min predicted index: 6 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 73500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/17.sql, query_id: 9, optimizer_config: 216, disabled_rules: None, walltime: 71500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/17.sql, query_id: 9, optimizer_config: 220, disabled_rules: optimize_hash_generation, walltime: 73500.0
2024-02-19 15:27:55 INFO     y[0]: 65500.0
2024-02-19 15:27:55 INFO     best choice -> 0.916083916083916
2024-02-19 15:27:55 INFO     bad choice -> 1.027972027972028
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/2.sql
2024-02-19 15:27:55 INFO     y: 307500.00       308500.00       310000.00       311000.00       312000.00       312000.00       312000.00       312500.00       312500.00       314000.00       316000.00       316500.00       318500.00319000.00        322000.00       322000.00       322000.00       322000.00       322000.00       324000.00       326000.00       328500.00       328500.00       330000.00       330500.00       335500.00       354500.00
2024-02-19 15:27:55 INFO     ŷ: 560273.00       576218.56       576296.62       552294.75       550352.50       567478.81       579759.56       576296.62       564321.12       576218.56       579678.88       567478.81       550352.50579759.56        583846.06       552294.75       591928.88       583846.06       564321.12       557843.44       584409.25       563534.31       579678.88       593594.25       584409.25       591928.88       593594.25
2024-02-19 15:27:55 INFO     min predicted index: 4 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 312000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/2.sql, query_id: 12, optimizer_config: 337, disabled_rules: None, walltime: 354500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/2.sql, query_id: 12, optimizer_config: 352, disabled_rules: optimize_hash_generation,prune_project_columns, walltime: 312000.0
2024-02-19 15:27:55 INFO     y[0]: 307500.0
2024-02-19 15:27:55 INFO     best choice -> 0.8674188998589563
2024-02-19 15:27:55 INFO     good choice -> 0.8801128349788434
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/20.sql
2024-02-19 15:27:55 INFO     y: 98000.00        100500.00       106500.00       107000.00       111000.00       111000.00       111500.00       112000.00       112000.00       112500.00       113500.00       118500.00       123000.00
2024-02-19 15:27:55 INFO     ŷ: 197644.45       205133.17       197282.14       194639.27       210542.83       232389.28       223469.72       233277.25       233277.25       194639.27       179242.14       223485.92       216450.73
2024-02-19 15:27:55 INFO     min predicted index: 10 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 113500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/20.sql, query_id: 13, optimizer_config: 381, disabled_rules: None, walltime: 112000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/20.sql, query_id: 13, optimizer_config: 394, disabled_rules: optimize_hash_generation,prune_filter_columns, walltime: 113500.0
2024-02-19 15:27:55 INFO     y[0]: 98000.0
2024-02-19 15:27:55 INFO     best choice -> 0.875
2024-02-19 15:27:55 INFO     bad choice -> 1.0133928571428572
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/21.sql
2024-02-19 15:27:55 INFO     y: 68000.00        68500.00        69000.00        72500.00        72500.00        73000.00        74000.00        74000.00        74500.00        74500.00        75000.00        75500.00        77000.00 77500.00 77500.00        78500.00        79000.00        79000.00        79500.00        80000.00        80000.00        81000.00        81500.00        81500.00        82500.00        83000.00        83500.00        83500.00        84500.00  84500.00        85000.00        85000.00        86500.00        88000.00        88500.00        88500.00        90000.00        90000.00        90500.00        93000.00        96000.00        97000.00        97000.00
2024-02-19 15:27:55 INFO     ŷ: 196967.81       162766.36       196967.81       191002.59       178612.31       178612.31       162766.36       196967.81       162766.36       162766.36       191002.59       193249.48       196967.81199651.81        179913.83       178612.31       199651.81       205255.48       193249.48       179913.83       193249.48       191002.59       193249.48       172571.67       191002.59       179913.83       175114.36       199651.81193249.48        189376.36       193249.48       175114.36       181492.55       196522.19       175114.36       196522.19       193249.48       181492.55       181492.55       181492.55       175593.47       205255.48       196522.19
2024-02-19 15:27:55 INFO     min predicted index: 1 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 68500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/21.sql, query_id: 14, optimizer_config: 402, disabled_rules: None, walltime: 97000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/21.sql, query_id: 14, optimizer_config: 425, disabled_rules: optimize_hash_generation,simplify_expressions, walltime: 68500.0
2024-02-19 15:27:55 INFO     y[0]: 68000.0
2024-02-19 15:27:55 INFO     best choice -> 0.7010309278350515
2024-02-19 15:27:55 INFO     good choice -> 0.7061855670103093
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/22.sql
2024-02-19 15:27:55 INFO     y: 59000.00        59500.00        60000.00        60500.00        61000.00        68000.00        68000.00
2024-02-19 15:27:55 INFO     ŷ: 201122.94       172120.00       195502.66       192555.92       195512.91       195512.91       195512.91
2024-02-19 15:27:55 INFO     min predicted index: 1 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 59500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/22.sql, query_id: 15, optimizer_config: 466, disabled_rules: None, walltime: 59000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/22.sql, query_id: 15, optimizer_config: 470, disabled_rules: optimize_hash_generation, walltime: 59500.0
2024-02-19 15:27:55 INFO     y[0]: 59000.0
2024-02-19 15:27:55 INFO     best choice -> 1.0
2024-02-19 15:27:55 INFO     bad choice -> 1.0084745762711864
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/3.sql
2024-02-19 15:27:55 INFO     y: 47000.00        47500.00        48000.00        48500.00        50000.00        50500.00        50500.00        51000.00        52000.00        52000.00        52000.00        52500.00        52500.00 54000.00 58500.00        59500.00        60000.00        61000.00        61500.00        62500.00        66500.00
2024-02-19 15:27:55 INFO     ŷ: 182167.28       192741.84       192741.84       192741.84       192741.84       182167.28       192741.84       182167.28       192741.84       182167.28       182167.28       192741.84       192741.84192741.84        182167.28       192741.84       192741.84       192741.84       192741.84       180560.98       192741.84
2024-02-19 15:27:55 INFO     min predicted index: 19 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 62500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/3.sql, query_id: 16, optimizer_config: 475, disabled_rules: None, walltime: 61500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/3.sql, query_id: 16, optimizer_config: 479, disabled_rules: optimize_hash_generation, walltime: 62500.0
2024-02-19 15:27:55 INFO     y[0]: 47000.0
2024-02-19 15:27:55 INFO     best choice -> 0.7642276422764228
2024-02-19 15:27:55 INFO     bad choice -> 1.016260162601626
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/4.sql
2024-02-19 15:27:55 INFO     y: 42000.00        44500.00        45000.00        45000.00        45000.00        45500.00        46000.00        46500.00        47500.00        48500.00        49000.00        50000.00        51000.00 52500.00 57000.00
2024-02-19 15:27:55 INFO     ŷ: 180905.53       180905.53       180905.53       180905.53       132547.45       132547.45       180905.53       132547.45       132547.45       180905.53       202021.83       156446.38       132547.45180905.53        201991.39
2024-02-19 15:27:55 INFO     min predicted index: 4 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 45000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/4.sql, query_id: 17, optimizer_config: 514, disabled_rules: None, walltime: 49000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/4.sql, query_id: 17, optimizer_config: 530, disabled_rules: optimize_hash_generation,prune_filter_columns, walltime: 45000.0
2024-02-19 15:27:55 INFO     y[0]: 42000.0
2024-02-19 15:27:55 INFO     best choice -> 0.8571428571428571
2024-02-19 15:27:55 INFO     good choice -> 0.9183673469387755
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/5.sql
2024-02-19 15:27:55 INFO     y: 90000.00        93000.00        93000.00        95000.00        95500.00        98500.00        100500.00       100500.00       101000.00       101500.00       117000.00
2024-02-19 15:27:55 INFO     ŷ: 228537.81       246540.84       228537.81       246540.84       246540.84       246540.84       246540.84       202052.66       246540.84       246540.84       246540.84
2024-02-19 15:27:55 INFO     min predicted index: 7 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 100500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/5.sql, query_id: 18, optimizer_config: 538, disabled_rules: None, walltime: 100500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/5.sql, query_id: 18, optimizer_config: 542, disabled_rules: optimize_hash_generation, walltime: 100500.0
2024-02-19 15:27:55 INFO     y[0]: 90000.0
2024-02-19 15:27:55 INFO     best choice -> 0.8955223880597015
2024-02-19 15:27:55 INFO     bad choice -> 1.0
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/6.sql
2024-02-19 15:27:55 INFO     y: 19000.00        19000.00        22000.00        22000.00        24000.00        30500.00
2024-02-19 15:27:55 INFO     ŷ: 154018.97       154018.97       154018.97       154018.97       154018.97       151490.77
2024-02-19 15:27:55 INFO     min predicted index: 5 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 30500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/6.sql, query_id: 19, optimizer_config: 555, disabled_rules: None, walltime: 22000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/6.sql, query_id: 19, optimizer_config: 562, disabled_rules: prune_tablescan_columns, walltime: 30500.0
2024-02-19 15:27:55 INFO     y[0]: 19000.0
2024-02-19 15:27:55 INFO     best choice -> 0.8636363636363636
2024-02-19 15:27:55 INFO     bad choice -> 1.3863636363636365
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/7.sql
2024-02-19 15:27:55 INFO     y: 78500.00        79000.00        79500.00        80000.00        80000.00        80000.00        80500.00        81000.00        82000.00        82000.00        82000.00        82500.00        82500.00 83000.00 84000.00        84500.00        84500.00        84500.00        85000.00        85000.00        86000.00        86000.00        86000.00        86000.00        86000.00        86500.00        87000.00        87500.00        87500.00  87500.00        87500.00        88000.00        88000.00        88000.00        90000.00        92000.00        93500.00        94000.00        94500.00        94500.00        95500.00        97500.00        100500.00
2024-02-19 15:27:55 INFO     ŷ: 187880.92       219935.69       211894.25       219935.69       211894.25       187885.58       219935.69       211894.25       185840.50       188062.88       208689.72       215538.61       188062.88185840.50        191660.94       219935.69       190952.69       219935.69       211894.25       211894.25       185840.50       185840.50       215538.61       208689.72       190952.69       191660.94       211894.25       219935.69219935.69        219935.69       211894.25       219935.69       211894.25       219935.69       215538.61       191660.94       215538.61       211894.25       190952.69       219935.69       190806.88       188062.88       208689.72
2024-02-19 15:27:55 INFO     min predicted index: 8 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 82000.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/7.sql, query_id: 20, optimizer_config: 565, disabled_rules: None, walltime: 94000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/7.sql, query_id: 20, optimizer_config: 586, disabled_rules: optimize_hash_generation,prune_project_columns, walltime: 82000.0
2024-02-19 15:27:55 INFO     y[0]: 78500.0
2024-02-19 15:27:55 INFO     best choice -> 0.8351063829787234
2024-02-19 15:27:55 INFO     good choice -> 0.8723404255319149
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/8.sql
2024-02-19 15:27:55 INFO     y: 203500.00       204000.00       207500.00       208000.00       213000.00       213500.00       214500.00       215000.00       215000.00       215500.00       217500.00       218000.00       218000.00218000.00        219500.00       220000.00       220000.00       221000.00       223500.00       224000.00       225000.00       225000.00       225500.00       225500.00       229500.00       244500.00       252000.00       253000.00260000.00        260000.00       260500.00       266000.00       279500.00
2024-02-19 15:27:55 INFO     ŷ: 434338.06       422253.88       422253.88       439390.00       439390.00       420508.19       422253.88       439390.00       422253.88       434338.06       422253.88       422253.88       422253.88429305.28        422253.88       434338.06       429305.28       439390.00       429305.28       422253.88       422253.88       422253.88       399967.97       399967.97       399967.97       399967.97       442609.91       422604.75442609.91        442609.91       422604.75       422604.75       422604.75
2024-02-19 15:27:55 INFO     min predicted index: 22 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 225500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/8.sql, query_id: 21, optimizer_config: 630, disabled_rules: None, walltime: 279500.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/8.sql, query_id: 21, optimizer_config: 659, disabled_rules: prune_tablescan_columns,simplify_expressions, walltime: 225500.0
2024-02-19 15:27:55 INFO     y[0]: 203500.0
2024-02-19 15:27:55 INFO     best choice -> 0.7280858676207513
2024-02-19 15:27:55 INFO     good choice -> 0.8067978533094812
2024-02-19 15:27:55 INFO     Preprocess data for query /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/9.sql
2024-02-19 15:27:55 INFO     y: 121000.00       124000.00       131000.00       135000.00       138000.00       142500.00       144000.00
2024-02-19 15:27:55 INFO     ŷ: 308664.00       308664.00       277962.47       308664.00       308664.00       175354.17       308664.00
2024-02-19 15:27:55 INFO     min predicted index: 5 (smaller is better)
2024-02-19 15:27:55 INFO     performance_from_model: 142500.0
2024-02-19 15:27:55 INFO     default_plan: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/9.sql, query_id: 22, optimizer_config: 693, disabled_rules: None, walltime: 124000.0
2024-02-19 15:27:55 INFO     plans[min_prediction_index]: query_path: /Users/songgane/Dev/src/github/query-optimizer/Auto-Steer/benchmark/queries/tpch/9.sql, query_id: 22, optimizer_config: 700, disabled_rules: prune_tablescan_columns, walltime: 142500.0
2024-02-19 15:27:55 INFO     y[0]: 121000.0
2024-02-19 15:27:55 INFO     best choice -> 0.9758064516129032
2024-02-19 15:27:55 INFO     bad choice -> 1.1491935483870968
```

* FIXME: Presto-disable-optimizers-through-session-properties.patch의 내용 중 추가되는 property의 기본값이 false를 설정하고 있다.
        patch 이전에는 기본값으로 true가 설정되고, patch에서는 기본값으로 false를 설정한다.

join_distribution_type|AUTOMATIC|Join distribution type. Possible values: [BROADCAST, PARTITIONED, AUTOMATIC]
join_reordering_strategy|AUTOMATIC|Join reordering strategy. Possible values: [NONE, ELIMINATE_CROSS_JOINS, AUTOMATIC]