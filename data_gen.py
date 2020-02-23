import csv
import numpy as np




def t_t_split(dataset_path, ratio = 0.85):

    with open('%s\\NPfile.csv'%(dataset_path), 'r') as NPfile:
        csvReader = csv.reader(NPfile)
        for line in csvReader:
            if line != []:
                NPDict[line[0]] = line[1]

    NPitems = list(NPDict.items())
    random.shuffle(NPitems)
    limit = int(ratio*len(NPitems))
            
    with open('%s\\train.csv'%(dataset_path),'w') as train:
        csv_writer = csv.writer(train)
        for i in range(limit):
            csv_writer.writerow(NPitems[i])

    with open('%s\\test.csv'%(dataset_path),'w') as test:
        csv_writer = csv.writer(test)
        for i in range(len(NPitems)-limit):
            csv_writer.writerow(NPitems[i])


class data_gen:

    def __init__(self, dataset_dir, batch_size):
        self.batch_size = batch_size
        self.dataset_dir = dataset_dir
        self.NList = []
        self.PList = []
        self.NPDict = dict()
        self.rawPList = []
        self.maxLogPrice = 0
        self.cur_index = 0

    def build_data(self):
        rawPList = []
        with open(self.dataset_dir, 'r') as NPfile:
            csvReader = csv.reader(NPfile)
            for line in csvReader:
                if line != []:
                    self.NPDict[line[0]] = line[1]
        NPDictItems = list(self.NPDict.items())

        for item in NPDictItems:

            # preparing number data for training

            strNums = item[0][4:]
            matNum = np.zeros((7, 10))
            if len(strNums) == 7:
                for i in range(7):
                    matNum[i][int(strNums[i])] = 1

            self.NList.append(matNum)

            # preparing price data for training

            rawPrice = int(item[1])/10000
            rawPrice = np.log10(rawPrice)
            rawPList.append(rawPrice)
        self.indexes = list(range(len(self.NList)))
        self.maxLogPrice = max(rawPList)
        for price in rawPList:
            self.PList.append(price/self.maxLogPrice)
        self.n = len(self.NList)

    def next_sample(self):
        self.cur_index += 1
        if self.cur_index >= len(self.NList):
            self.cur_index = 0
            random.shuffle(self.indexes)
        return self.NList[self.indexes[self.cur_index]], self.PList[self.indexes[self.cur_index]]

    def next_batch(self):
        while True:
            X_data = np.zeros([self.batch_size,7,10,1])  # 7*10 number array size
            Y_data = np.zeros([self.batch_size,1])
            x = np.expand_dims(self.next_sample()[0],axis=2)
            y = np.expand_dims(self.next_sample()[1],axis=0)
            for i in range(self.batch_size):
                X_data[i] = x
                Y_data[i] = y
            yield (X_data, Y_data)
