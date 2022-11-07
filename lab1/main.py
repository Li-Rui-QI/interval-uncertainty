import Solution as te

if __name__=="__main__":

    EPS = 1e-4
    task = te.Solution('data/Канал_1_700nm_2mm.csv', 'data/Канал_2_700nm_2mm.csv', 'data/ch1.txt',
                           'data/ch2.txt', 1, EPS, False, True, 'results/')
    task.loadData()
    task.findOctaves()
    task.plot()



