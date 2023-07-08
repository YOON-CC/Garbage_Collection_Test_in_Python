import gc

def gc_stats():
    print("GC Collections:", gc.get_stats()[0]['collections'])
    print("GC Collected Objects:", gc.get_stats()[0]['collected'])
    print("GC Unreachable Objects:", gc.get_stats()[0]['uncollectable'])


gc.collect()
print("gc 통계 - gc 유발을 위한 객체 생성 x")
gc_stats()

##객체 생성
a = []
for _ in range(100000):
    a.append([0] * 10000)

gc.collect()
print("gc 통계 - gc 유발을 위한 객체 생성 O")
gc_stats()