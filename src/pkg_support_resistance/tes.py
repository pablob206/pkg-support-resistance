"""
0.005301878089085221
0.005424426984973252
0.005419226014055312


"""
from pkg_support_resistance import (
    VanillaSupportResistance,
    KMeansSupportResistance,
    DBSCANSupportResistance,
)
from pkg_support_resistance.data_set.data_extraction import sr_input_example
import timeit

# # Vanilla algorithms:
# sr_result: list[dict] = VanillaSupportResistance.exec_pipeline(input_data=sr_input_example, cluster_threshold=1)
# print(sr_result, len(sr_result))

execution_time = timeit.timeit(
    f"VanillaSupportResistance.exec_pipeline(input_data={sr_input_example}, cluster_threshold=1)",
    setup="from pkg_support_resistance import VanillaSupportResistance",
    number=1,
)
print(f"Tiempo de ejecución: {execution_time} segundos")
