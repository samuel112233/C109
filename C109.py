import pandas as pd 
import statistics 
import csv
df=pd.read_csv('height-weight.csv')
heightList=df['Height(Inches)'].to_list()
weightList=df['Weight(Pounds)'].to_list()

hMean=statistics.mean(heightList) 
wMean=statistics.mean(weightList)

hMedian=statistics.median(heightList) 
wMedian=statistics.median(weightList)

hMode=statistics.mode(heightList) 
wMode=statistics.mode(weightList)

hStd=statistics.stdev(heightList) 
wStd=statistics.stdev(weightList)

print('Mean,Median,Mode,Std of height is {} {} {} {}'.format(hMean,hMedian,hMode,hStd))
print('Mean,Median,Mode,Std of weight is {} {} {} {}'.format(wMean,wMedian,wMode,wStd))

h1StdStart,h1StdEnd=hMean-hStd,hMean+hStd
h2StdStart,h2StdEnd=hMean-2*hStd,hMean+2*hStd
h3StdStart,h3StdEnd=hMean-3*hStd,hMean+3*hStd

heightWith1std=[result for result in heightList if result>h1StdStart and result<h1StdEnd]
heightWith2std=[result for result in heightList if result>h2StdStart and result<h2StdEnd]
heightWith3std=[result for result in heightList if result>h3StdStart and result<h3StdEnd]

print('{}% of data for height lies within 1std'.format(len(heightWith1std)*100/len(heightList)))
print('{}% of data for height lies within 2std'.format(len(heightWith2std)*100/len(heightList)))
print('{}% of data for height lies within 3std'.format(len(heightWith3std)*100/len(heightList)))


w1StdStart,w1StdEnd=wMean-wStd,wMean+wStd
w2StdStart,w2StdEnd=wMean-2*wStd,wMean+2*wStd
w3StdStart,w3StdEnd=wMean-3*wStd,wMean+3*wStd

weightWith1std=[result for result in weightList if result>w1StdStart and result<w1StdEnd]
weightWith2std=[result for result in weightList if result>w2StdStart and result<w2StdEnd]
weightWith3std=[result for result in weightList if result>w3StdStart and result<w3StdEnd]

print('{}% of data for weight lies within 1std'.format(len(weightWith1std)*100/len(weightList)))
print('{}% of data for weight lies within 2std'.format(len(weightWith2std)*100/len(weightList)))
print('{}% of data for weight lies within 3std'.format(len(weightWith3std)*100/len(weightList)))