import gc
import psutil
import timeit

def garbage_dummy():
    # 가비지 객체 생성
    for a in range(1000000):
        a = [1] * 100

def run_with_gc():
    gc.enable() 
    before = psutil.Process().memory_info().rss
    garbage_dummy()
    gc.collect()
    after = psutil.Process().memory_info().rss
    execution_time = timeit.timeit(gc.collect, number=1)

    print("GC 없음")
    print("메모리 사용 전 : ", before)
    print("메모리 사용 후 : ", after)
    print("실행시간 : ", execution_time)

def run_without_gc():
    gc.disable() 
    before = psutil.Process().memory_info().rss
    garbage_dummy()
    after = before
    execution_time = 0

    print("GC 없음")
    print("메모리 사용 전 : ", before)
    print("메모리 사용 후 : ", after)
    print("실행시간 : ", execution_time)

##함수 실행
run_with_gc()
run_without_gc()