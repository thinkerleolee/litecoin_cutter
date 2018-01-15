import login
import liter
import time
import threading

def miner(litecoin_addr):
    while True:
        try:
            login.login(litecoin_addr)
        except:
            print('error retry')
            time.sleep(1)
            continue

        for i in range(1, 6):
            time.sleep(1)
            try:
                liter.get_liter(litecoin_addr, i)
            except:
                print('error retry')
                time.sleep(1)
                continue

        time.sleep(60 * 6)

if __name__ == '__main__':
    a = threading.Thread(target=miner, args=('LLwvQrf8m2dLcDn9P55XvLFsSy6hLbFmmq',))
    b = threading.Thread(target=miner, args=('Lf3sAjb3cDi2Wyz5VUugfT9N6bVhYW1tPn',))
    c = threading.Thread(target=miner, args=('LZjv8gGATsUA7ttUs5RxRU64cfkqDPvLUT',))
    d = threading.Thread(target=miner, args=('LgFz5esrxdUpAKnyXgu6Beksji4YnvDdSV',))
    e = threading.Thread(target=miner, args=('LZa5ff4iWneoiKKk5tFC6GMPdfd6fyK2Cc',))
    f = threading.Thread(target=miner, args=('LhoXHW21whAgd1M1D9vXs2rfnn91qd6w9h',))
    g = threading.Thread(target=miner, args=('LhUH3dc8g3jCgAyPVkC3u5Pr3o7NRuL1n6',))
    h = threading.Thread(target=miner, args=('LMkYMpycq1bxN7xrL7RgfrxZesPN3uwqsw',))
    i = threading.Thread(target=miner, args=('La72GdEpAgi9xtknV7WKLs8M15sA4LTesS',))
    j = threading.Thread(target=miner, args=('LR8h97LgCSNDJsVREFjNdeSUhb9gCYGM1T',))
    k = threading.Thread(target=miner, args=('LUyfkJ3JpJSpAtLqPHNEJ9bHL17vSaebmS',))
    l = threading.Thread(target=miner, args=('LUPjyxv3CRbGMkag2xcQVbcy1H5jvyUyRy',))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()